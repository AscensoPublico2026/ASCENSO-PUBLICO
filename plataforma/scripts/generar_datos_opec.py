# /// script
# requires-python = ">=3.10"
# dependencies = ["openpyxl>=3.1,<4"]
# ///
"""Convierte el consolidado SIMO de Excel a datos optimizados para la web.

Uso desde plataforma/:
    uv run scripts/generar_datos_opec.py --fecha 2026-07-15
"""

from __future__ import annotations

import argparse
import html
import json
import re
import unicodedata
from datetime import date
from pathlib import Path
from typing import Any

from openpyxl import load_workbook

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_FILE = REPO_ROOT / "Empleos_SIMO_ESEs_2026_clae-2.xlsx"
INDEX_FILE = REPO_ROOT / "plataforma" / "public" / "data" / "opec-index.json"
META_FILE = REPO_ROOT / "plataforma" / "data" / "opec-meta.json"
DETAILS_DIR = REPO_ROOT / "plataforma" / "public" / "data" / "opec-details"
DETAIL_SHARDS = 32
SHEET_NAME = "Empleos SIMO"

# Dato confirmado directamente por Ascenso Público el 15 de julio de 2026.
CORRECCIONES = {
    245015: {"Total vacantes": 5, "Disponibles": 5},
}

PROCESS_LABELS = {
    "CONCURSO_ABIERTO": "Abierto",
    "CONCURSO_ABIERTO_DISCAPACIDAD": "Abierto",
    "CONCURSO_CERRADO_ASCENSOS": "Ascenso",
    "CONCURSO_CERRADO_ASCENSOS_DISCAPACIDAD": "Ascenso",
}

STUDY_LABELS = {
    "primaria-laboral": "Primaria + formación laboral",
    "secundaria-aprobada": "4 o 5 años de bachillerato aprobados",
    "bachiller-solo": "Solo título de bachiller",
    "bachiller-curso": "Bachiller + curso o certificación",
    "tecnico-laboral": "Técnico laboral o auxiliar",
    "tecnico-tecnologo": "Técnico profesional o tecnólogo",
    "universitario-sin-titulo": "Estudios universitarios sin título",
    "profesional": "Título profesional universitario",
    "posgrado": "Título profesional + posgrado",
    "curso-especifico": "Curso o certificación específica",
}


def texto(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def limpiar_html(value: Any) -> str:
    raw = texto(value)
    raw = re.sub(r"<br\s*/?>", " ", raw, flags=re.IGNORECASE)
    raw = re.sub(r"<[^>]+>", "", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip(" ,")


def normalizar_busqueda(value: Any) -> str:
    normalized = unicodedata.normalize("NFD", limpiar_html(value).lower())
    normalized = "".join(char for char in normalized if unicodedata.category(char) != "Mn")
    return re.sub(r"[^a-z0-9]+", " ", normalized).strip()


def numero_entero(value: Any) -> int:
    if value is None or value == "":
        return 0
    return int(float(value))


def clasificar_estudio(value: Any) -> tuple[str, str]:
    """Devuelve una categoría educativa exhaustiva y una etiqueta comprensible.

    La categoría describe la formación mínima explícita del requisito, pero no
    reemplaza la lectura del texto oficial (que puede incluir disciplinas o cursos).
    """
    requirement = normalizar_busqueda(value).upper()
    has_primary = "TITULO DE PRIMARIA" in requirement
    has_bachelor = "BACHILLERATO" in requirement or bool(
        re.search(r"\bBACHILLER\b", requirement)
    )
    has_job_training = (
        "EDUCACION PARA EL TRABAJO" in requirement
        or "FORMACION LABORAL" in requirement
    )
    has_technical_professional = (
        "TECNICA PROFESIONAL" in requirement
        or "FORMACION TECNICA PROFESIONAL" in requirement
    )
    has_technology = (
        "TITULO DE TECNOLOGICA" in requirement
        or "TECNOLOGIA EN" in requirement
    )
    has_professional_degree = bool(
        re.search(
            r"(?:TITULO DE|PENSUM ACADEMICO DE EDUCACION SUPERIOR DE) PROFESIONAL\b",
            requirement,
        )
    )
    has_partial_university = bool(
        re.search(
            r"APROBACION DE .*?(?:ANOS|SEMESTRES).*?DE PROFESIONAL\b",
            requirement,
        )
    )
    has_postgraduate = any(
        marker in requirement
        for marker in ("POSTGRADO", "ESPECIALIZACION", "MAESTRIA", "DOCTORADO")
    )
    bachelor_only = bool(
        re.fullmatch(r"(?:FORMACION BASICA )?TITULO DE BACHILLERATO", requirement)
    )
    has_partial_secondary = bool(
        re.search(r"APROBACION DE .*?ANOS.*?DE BACHILLERATO\b", requirement)
    )

    if has_primary:
        category = "primaria-laboral"
    elif has_postgraduate:
        category = "posgrado"
    elif has_job_training:
        category = "tecnico-laboral"
    elif has_technical_professional or has_technology:
        category = "tecnico-tecnologo"
    elif has_professional_degree:
        category = "profesional"
    elif has_partial_university:
        category = "universitario-sin-titulo"
    elif has_partial_secondary:
        category = "secundaria-aprobada"
    elif bachelor_only:
        category = "bachiller-solo"
    elif has_bachelor:
        category = "bachiller-curso"
    else:
        category = "curso-especifico"

    return category, STUDY_LABELS[category]


def resumir_requisito(value: Any, max_length: int = 170) -> str:
    requirement = limpiar_html(value)
    if len(requirement) <= max_length:
        return requirement
    shortened = requirement[: max_length - 1].rsplit(" ", 1)[0]
    return f"{shortened}…"


def clasificar_requisitos_adicionales(value: Any) -> tuple[list[str], list[str]]:
    requirement = normalizar_busqueda(value).upper()
    if not requirement:
        return [], []

    keys: list[str] = []
    labels: list[str] = []
    rules = (
        ("rethus", "ReTHUS", ("RETHUS", "TALENTO HUMANO EN SALUD")),
        (
            "tarjeta-profesional",
            "Tarjeta o matrícula profesional",
            ("TARJETA O MATRICULA PROFESIONAL",),
        ),
        (
            "licencia-conduccion",
            "Licencia de conducción",
            ("LICENCIA DE CONDUCCION",),
        ),
        (
            "licencia-sst",
            "Licencia en seguridad y salud en el trabajo",
            ("LICENCIA VIGENTE EN SEGURIDAD Y SALUD", "LICENCIA VIGENTE EN SEGURIDAD Y"),
        ),
        (
            "registro-archivistas",
            "Registro profesional de archivistas",
            ("REGISTRO UNICO PROFESIONAL DE ARCHIVISTAS",),
        ),
        ("soporte-vital", "Soporte vital básico", ("SOPORTE VITAL BASICO",)),
        ("radioproteccion", "Carné de radioprotección", ("RADIO PROTECCION",)),
        ("antecedentes-contador", "Antecedentes de contador", ("ANTECEDENTES DE CONTADOR",)),
        ("cedula", "Cédula de ciudadanía", ("CEDULA DE CIUDADANIA",)),
    )
    for key, label, markers in rules:
        if any(marker in requirement for marker in markers):
            keys.append(key)
            labels.append(label)

    if not labels:
        return ["otro"], ["Otro requisito adicional"]
    return keys, labels


def experiencia_meses(value: Any) -> int | None:
    requirement = limpiar_html(value)
    if re.search(r"\b(?:no requiere|sin)\s+experiencia\b", requirement, re.IGNORECASE):
        return 0

    amounts: list[int] = []
    for amount, unit in re.findall(
        r"\((\d+)\)\s*(año(?:s)?|mes(?:es)?)\b", requirement, flags=re.IGNORECASE
    ):
        months = int(amount) * (12 if unit.lower().startswith("año") else 1)
        amounts.append(months)

    if not amounts:
        return None

    # En alternativas separadas por "O" se usa la exigencia de menor duración.
    # En requisitos simultáneos con "Y", la experiencia relacionada suele estar
    # contenida en la experiencia total; por ello se usa el mayor plazo, no la suma.
    has_alternative = bool(re.search(r"(?:^|[,;\s])O(?:[,;\s]|$)", requirement, re.IGNORECASE))
    return min(amounts) if has_alternative else max(amounts)


def lista_funciones(value: Any) -> list[str]:
    raw = str(value or "")
    return [limpiar_html(item) for item in raw.split("||") if limpiar_html(item)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fecha",
        default=date.today().isoformat(),
        help="Fecha pública de actualización en formato AAAA-MM-DD.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"No se encontró el consolidado: {SOURCE_FILE}")

    workbook = load_workbook(SOURCE_FILE, read_only=True, data_only=True)
    sheet = workbook[SHEET_NAME]
    row_iterator = sheet.iter_rows(values_only=True)
    headers = [texto(value) for value in next(row_iterator)]

    index: list[dict[str, Any]] = []
    details: dict[str, dict[str, Any]] = {}
    seen: set[int] = set()
    unparsed_experience: list[int] = []

    for values in row_iterator:
        row = dict(zip(headers, values))
        opec = numero_entero(row["OPEC"])
        if not opec:
            continue
        if opec in seen:
            raise ValueError(f"OPEC duplicada: {opec}")
        seen.add(opec)

        for field, corrected_value in CORRECCIONES.get(opec, {}).items():
            row[field] = corrected_value

        experience = limpiar_html(row["Requisito experiencia"])
        months = experiencia_meses(experience)
        if months is None:
            unparsed_experience.append(opec)

        process = texto(row["Tipo proceso"])
        modality = PROCESS_LABELS.get(process)
        if modality is None:
            raise ValueError(f"Tipo de proceso desconocido en OPEC {opec}: {process}")

        study = limpiar_html(row["Requisito estudio"])
        study_level, study_summary = clasificar_estudio(study)
        additional_requirement = limpiar_html(row["Requisito otros"])
        additional_keys, additional_labels = clasificar_requisitos_adicionales(
            additional_requirement
        )
        denomination = texto(row["Denominación"])
        entity = texto(row["Entidad"])
        department = texto(row["Departamento"])
        municipality = texto(row["Municipio"])
        level = texto(row["Nivel"])
        vacancies = numero_entero(row["Total vacantes"])
        available = numero_entero(row["Disponibles"])

        search_text = normalizar_busqueda(
            " ".join(
                [
                    str(opec),
                    denomination,
                    entity,
                    department,
                    municipality,
                    level,
                    texto(row["Código empleo"]),
                    texto(row["Dependencia"]),
                    study,
                    experience,
                    "sin experiencia" if months == 0 else "",
                ]
            )
        )

        summary = {
            "opec": opec,
            "denominacion": denomination,
            "nivel": level,
            "grado": texto(row["Grado"]),
            "codigo": texto(row["Código empleo"]),
            "salario": numero_entero(row["Asignación salarial"]),
            "vigenciaSalario": numero_entero(row["Vigencia salarial"]),
            "entidad": entity,
            "departamento": department,
            "municipio": municipality,
            "vacantes": vacancies,
            "disponibles": available,
            "modalidad": modality,
            "discapacidad": texto(row["Reserva discapacidad"]).lower() == "sí",
            "sinExperiencia": months == 0,
            "experienciaMeses": months,
            "nivelEstudio": study_level,
            "estudioResumen": study_summary,
            "estudioDetalleCorto": resumir_requisito(study),
            "requisitosAdicionales": additional_keys,
            "requisitosAdicionalesResumen": additional_labels,
            "busqueda": search_text,
        }
        index.append(summary)

        details[str(opec)] = {
            **{key: value for key, value in summary.items() if key != "busqueda"},
            "nit": texto(row["NIT"]),
            "tipoEntidad": texto(row["Tipo entidad"]),
            "convocatoria": texto(row["Convocatoria"]),
            "anio": numero_entero(row["Año"]),
            "tipoProceso": process,
            "dependencia": texto(row["Dependencia"]),
            "concursoAscenso": texto(row["Concurso ascenso"]).lower() == "sí",
            "proposito": limpiar_html(row["Propósito"]),
            "funciones": lista_funciones(row["Funciones"]),
            "requisitoEstudio": study,
            "requisitoExperiencia": experience,
            "requisitoOtros": additional_requirement,
        }

    index.sort(key=lambda item: item["opec"])

    total_vacancies = sum(item["vacantes"] for item in index)
    open_jobs = [item for item in index if item["modalidad"] == "Abierto"]
    meta = {
        "convocatoria": "Empresas Sociales del Estado 2026",
        "fechaActualizacion": args.fecha,
        "totalOpec": len(index),
        "totalVacantes": total_vacancies,
        "opecAbiertas": len(open_jobs),
        "vacantesAbiertas": sum(item["vacantes"] for item in open_jobs),
        "entidades": len({item["entidad"] for item in index}),
        "departamentos": len({item["departamento"] for item in index}),
        "municipios": len({item["municipio"] for item in index}),
        "sinExperiencia": sum(item["sinExperiencia"] for item in open_jobs),
        "fuente": "Consolidado de empleos SIMO para Empresas Sociales del Estado",
    }

    if not index:
        raise ValueError("El consolidado no contiene OPEC")
    if len(index) != len(details):
        raise ValueError("El índice y los detalles no tienen la misma cantidad de OPEC")
    if any(item["vacantes"] <= 0 for item in index):
        raise ValueError("Todas las OPEC deben tener al menos una vacante")
    if details["245015"]["vacantes"] != 5 or details["245015"]["disponibles"] != 5:
        raise ValueError("La corrección confirmada para la OPEC 245015 no fue aplicada")
    if unparsed_experience:
        raise ValueError(
            "No se pudo interpretar la experiencia de estas OPEC: "
            + ", ".join(map(str, unparsed_experience))
        )

    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
    META_FILE.parent.mkdir(parents=True, exist_ok=True)
    DETAILS_DIR.mkdir(parents=True, exist_ok=True)
    for old_shard in DETAILS_DIR.glob("*.json"):
        old_shard.unlink()

    INDEX_FILE.write_text(
        json.dumps({"meta": meta, "empleos": index}, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    META_FILE.write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    shards: list[dict[str, dict[str, Any]]] = [dict() for _ in range(DETAIL_SHARDS)]
    for opec, detail in details.items():
        shards[int(opec) % DETAIL_SHARDS][opec] = detail
    for shard_number, shard in enumerate(shards):
        shard_file = DETAILS_DIR / f"{shard_number:02d}.json"
        shard_file.write_text(
            json.dumps({"empleos": shard}, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )

    detail_size = sum(path.stat().st_size for path in DETAILS_DIR.glob("*.json"))
    print(f"Índice: {INDEX_FILE} ({INDEX_FILE.stat().st_size / 1024:.1f} KiB)")
    print(
        f"Detalles: {DETAIL_SHARDS} fragmentos en {DETAILS_DIR} "
        f"({detail_size / 1024:.1f} KiB en total)"
    )
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

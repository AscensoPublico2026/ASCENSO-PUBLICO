"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useRef, useState, type RefObject } from "react";
import {
  formatOpecDate,
  getOpecDetailUrl,
  type OpecDetail,
  type OpecDetailShard,
  type OpecIndexPayload,
  type OpecSummary,
} from "@/lib/opec";

const PAGE_SIZE = 12;
const currency = new Intl.NumberFormat("es-CO", {
  style: "currency",
  currency: "COP",
  maximumFractionDigits: 0,
});

function normalize(value: string): string {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function matchesSearch(job: OpecSummary, normalizedQuery: string): boolean {
  const terms = normalizedQuery.split(" ").filter(Boolean);
  if (!terms.length) return true;

  const tokens = job.busqueda.split(" ");
  return terms.every((term) => {
    if (/^\d+$/.test(term)) return String(job.opec).startsWith(term);
    if (tokens.includes(term)) return true;
    // Permite búsquedas naturales como "enfer" o "admin" sin convertir
    // fragmentos cortos como "cali" en coincidencias con "calidad".
    return term.length >= 5 && tokens.some((token) => token.startsWith(term));
  });
}

const FOCUSABLE_SELECTOR = [
  "a[href]",
  "button:not([disabled])",
  "input:not([disabled])",
  "select:not([disabled])",
  "textarea:not([disabled])",
  "[tabindex]:not([tabindex='-1'])",
].join(",");

function useFocusTrap(
  active: boolean,
  containerRef: RefObject<HTMLElement>,
  initialFocusRef: RefObject<HTMLElement>,
  onEscape: () => void,
) {
  useEffect(() => {
    if (!active) return;
    const previousFocus = document.activeElement as HTMLElement | null;
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    requestAnimationFrame(() => initialFocusRef.current?.focus());

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        event.preventDefault();
        onEscape();
        return;
      }
      if (event.key !== "Tab" || !containerRef.current) return;
      const focusable = Array.from(
        containerRef.current.querySelectorAll<HTMLElement>(FOCUSABLE_SELECTOR),
      ).filter((element) => !element.hasAttribute("disabled"));
      if (!focusable.length) {
        event.preventDefault();
        containerRef.current.focus();
        return;
      }
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    };

    document.addEventListener("keydown", onKeyDown);
    return () => {
      document.body.style.overflow = previousOverflow;
      document.removeEventListener("keydown", onKeyDown);
      requestAnimationFrame(() => previousFocus?.focus());
    };
  }, [active, containerRef, initialFocusRef, onEscape]);
}

function formatExperience(months: number | null): string {
  if (months === 0) return "Sin experiencia";
  if (months === null) return "Ver requisito";
  if (months === 12) return "1 año de experiencia";
  if (months % 12 === 0) return `${months / 12} años de experiencia`;
  return `${months} meses de experiencia`;
}

function formatAdditionalRequirements(job: OpecSummary): string {
  if (!job.requisitosAdicionalesResumen.length) return "Sin requisito adicional registrado";
  const visible = job.requisitosAdicionalesResumen.slice(0, 2).join(" + ");
  const remaining = job.requisitosAdicionalesResumen.length - 2;
  return remaining > 0 ? `${visible} +${remaining}` : visible;
}

function SearchIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <circle cx="11" cy="11" r="7" />
      <path d="m20 20-4-4" />
    </svg>
  );
}

function CloseIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <path d="M6 6l12 12M18 6 6 18" />
    </svg>
  );
}

function CopyIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden="true">
      <rect x="8" y="8" width="11" height="11" rx="2" />
      <path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2" />
    </svg>
  );
}

function EmptyIcon() {
  return (
    <svg viewBox="0 0 64 64" aria-hidden="true">
      <circle cx="28" cy="28" r="18" />
      <path d="m42 42 13 13M20 28h16M28 20v16" />
    </svg>
  );
}

interface FiltersProps {
  departments: string[];
  municipalities: string[];
  department: string;
  municipality: string;
  level: string;
  education: string;
  experience: string;
  additionalRequirement: string;
  minimumSalary: string;
  disability: boolean;
  onDepartment: (value: string) => void;
  onMunicipality: (value: string) => void;
  onLevel: (value: string) => void;
  onEducation: (value: string) => void;
  onExperience: (value: string) => void;
  onAdditionalRequirement: (value: string) => void;
  onMinimumSalary: (value: string) => void;
  onDisability: (value: boolean) => void;
  onReset: () => void;
}

function Filters({
  departments,
  municipalities,
  department,
  municipality,
  level,
  education,
  experience,
  additionalRequirement,
  minimumSalary,
  disability,
  onDepartment,
  onMunicipality,
  onLevel,
  onEducation,
  onExperience,
  onAdditionalRequirement,
  onMinimumSalary,
  onDisability,
  onReset,
}: FiltersProps) {
  return (
    <div className="opec-filter-fields">
      <div className="opec-filter-head">
        <div>
          <span className="opec-filter-kicker">Personaliza tu búsqueda</span>
          <h2 id="opec-filters-title">Filtros</h2>
        </div>
        <button type="button" className="opec-reset" onClick={onReset}>Limpiar</button>
      </div>

      <label className="opec-field">
        <span>Departamento</span>
        <select value={department} onChange={(event) => onDepartment(event.target.value)}>
          <option value="">Todos los departamentos</option>
          {departments.map((item) => <option key={item} value={item}>{item}</option>)}
        </select>
      </label>

      <label className="opec-field">
        <span>Municipio</span>
        <select value={municipality} onChange={(event) => onMunicipality(event.target.value)}>
          <option value="">Todos los municipios</option>
          {municipalities.map((item) => <option key={item} value={item}>{item}</option>)}
        </select>
      </label>

      <label className="opec-field">
        <span>Nivel del empleo</span>
        <select value={level} onChange={(event) => onLevel(event.target.value)}>
          <option value="">Todos los niveles</option>
          <option value="Asistencial">Asistencial</option>
          <option value="Técnico">Técnico</option>
          <option value="Profesional">Profesional</option>
        </select>
      </label>

      <label className="opec-field opec-field-highlight">
        <span>Formación requerida</span>
        <select value={education} onChange={(event) => onEducation(event.target.value)}>
          <option value="">Cualquier nivel de estudios</option>
          <option value="primaria-laboral">Primaria + formación laboral</option>
          <option value="secundaria-aprobada">4 o 5 años de bachillerato aprobados</option>
          <option value="bachiller-solo">Solo título de bachiller</option>
          <option value="bachiller-curso">Bachiller + curso o certificación</option>
          <option value="tecnico-laboral">Técnico laboral o auxiliar</option>
          <option value="tecnico-tecnologo">Técnico profesional o tecnólogo</option>
          <option value="universitario-sin-titulo">Estudios universitarios sin título</option>
          <option value="profesional">Título profesional universitario</option>
          <option value="posgrado">Título profesional + posgrado</option>
          <option value="curso-especifico">Curso o certificación específica</option>
        </select>
        <small>Clasificación orientativa. Revisa siempre el requisito completo.</small>
      </label>

      <label className="opec-field">
        <span>Experiencia requerida</span>
        <select value={experience} onChange={(event) => onExperience(event.target.value)}>
          <option value="">Cualquier experiencia</option>
          <option value="0">Sin experiencia</option>
          <option value="6">Hasta 6 meses</option>
          <option value="12">Hasta 12 meses</option>
          <option value="24">Hasta 24 meses</option>
          <option value="36">Hasta 36 meses</option>
          <option value="37+">Más de 36 meses</option>
        </select>
      </label>

      <label className="opec-field">
        <span>Requisito adicional</span>
        <select value={additionalRequirement} onChange={(event) => onAdditionalRequirement(event.target.value)}>
          <option value="">Cualquier requisito adicional</option>
          <option value="none">Sin requisito adicional registrado</option>
          <option value="rethus">Requiere ReTHUS</option>
          <option value="tarjeta-profesional">Tarjeta o matrícula profesional</option>
          <option value="licencia-conduccion">Licencia de conducción</option>
          <option value="licencia-sst">Licencia en seguridad y salud</option>
          <option value="registro-archivistas">Registro profesional de archivistas</option>
          <option value="soporte-vital">Certificado de soporte vital básico</option>
          <option value="radioproteccion">Carné de radioprotección</option>
          <option value="antecedentes-contador">Antecedentes de contador</option>
          <option value="cedula">Cédula de ciudadanía</option>
          <option value="otro">Otro requisito adicional</option>
        </select>
      </label>

      <label className="opec-field">
        <span>Salario desde</span>
        <select value={minimumSalary} onChange={(event) => onMinimumSalary(event.target.value)}>
          <option value="">Cualquier salario</option>
          <option value="2000000">$2.000.000</option>
          <option value="3000000">$3.000.000</option>
          <option value="4000000">$4.000.000</option>
          <option value="5000000">$5.000.000</option>
          <option value="7000000">$7.000.000</option>
          <option value="10000000">$10.000.000</option>
        </select>
      </label>

      <label className="opec-check">
        <input
          type="checkbox"
          checked={disability}
          onChange={(event) => onDisability(event.target.checked)}
        />
        <span className="opec-check-box" aria-hidden="true">✓</span>
        <span><strong>Reserva para discapacidad</strong><small>Mostrar únicamente empleos con reserva.</small></span>
      </label>
    </div>
  );
}

function JobCard({ job, onOpen, onCopy, copied }: {
  job: OpecSummary;
  onOpen: (job: OpecSummary) => void;
  onCopy: (opec: number) => void;
  copied: boolean;
}) {
  return (
    <article className="opec-card">
      <div className="opec-card-top">
        <div className="opec-badges">
          <span className={`opec-level opec-level-${normalize(job.nivel)}`}>{job.nivel}</span>
          {job.sinExperiencia && <span className="opec-badge-success">Sin experiencia</span>}
          {job.discapacidad && <span className="opec-badge-access">Reserva discapacidad</span>}
        </div>
        <button
          type="button"
          className={`opec-copy-mini${copied ? " copied" : ""}`}
          onClick={() => onCopy(job.opec)}
          aria-label={`Copiar número OPEC ${job.opec}`}
        >
          <CopyIcon /> {copied ? "Copiada" : `OPEC ${job.opec}`}
        </button>
      </div>

      <h3>{job.denominacion}</h3>
      <p className="opec-entity">{job.entidad}</p>

      <div className="opec-requirement-snapshot">
        <span className="opec-snapshot-title">Requisitos a simple vista</span>
        <div>
          <span className="opec-snapshot-icon" aria-hidden="true">🎓</span>
          <p>
            <small>Estudios</small>
            <strong>{job.estudioResumen}</strong>
            <span className="opec-study-excerpt">{job.estudioDetalleCorto}</span>
          </p>
        </div>
        <div>
          <span className="opec-snapshot-icon" aria-hidden="true">💼</span>
          <p><small>Experiencia</small><strong>{formatExperience(job.experienciaMeses)}</strong></p>
        </div>
        <div className={job.requisitosAdicionales.length ? "has-extra" : ""}>
          <span className="opec-snapshot-icon" aria-hidden="true">📋</span>
          <p>
            <small>Otros requisitos</small>
            <strong
              title={job.requisitosAdicionalesResumen.join(", ") || undefined}
              aria-label={job.requisitosAdicionalesResumen.join(", ") || "Sin requisito adicional registrado"}
            >
              {formatAdditionalRequirements(job)}
            </strong>
          </p>
        </div>
      </div>

      <div className="opec-card-data">
        <div><span className="opec-data-icon" aria-hidden="true">⌖</span><span><small>Ubicación</small>{job.municipio}, {job.departamento}</span></div>
        <div><span className="opec-data-icon" aria-hidden="true">$</span><span><small>Asignación salarial</small>{currency.format(job.salario)}</span></div>
        <div><span className="opec-data-icon" aria-hidden="true">◎</span><span><small>Vacantes</small>{job.vacantes} {job.vacantes === 1 ? "vacante" : "vacantes"}</span></div>
      </div>

      <div className="opec-card-foot">
        <span className={`opec-modality ${job.modalidad === "Abierto" ? "open" : "promotion"}`}>
          <i /> Concurso {job.modalidad.toLowerCase()}
        </span>
        <button type="button" className="opec-detail-button" onClick={() => onOpen(job)}>
          Ver empleo completo <span aria-hidden="true">→</span>
        </button>
      </div>
    </article>
  );
}

function DetailModal({ job, detail, loading, error, copied, onClose, onCopy }: {
  job: OpecSummary;
  detail: OpecDetail | null;
  loading: boolean;
  error: string;
  copied: boolean;
  onClose: () => void;
  onCopy: (opec: number) => void;
}) {
  const modalRef = useRef<HTMLElement>(null);
  const closeButtonRef = useRef<HTMLButtonElement>(null);
  useFocusTrap(true, modalRef, closeButtonRef, onClose);

  return (
    <div className="opec-modal-backdrop" role="presentation" onMouseDown={(event) => {
      if (event.target === event.currentTarget) onClose();
    }}>
      <section ref={modalRef} className="opec-modal" role="dialog" aria-modal="true" aria-labelledby="opec-modal-title" tabIndex={-1}>
        <div className="opec-modal-head">
          <div>
            <span className="opec-modal-eyebrow">OPEC {job.opec} · Concurso {job.modalidad.toLowerCase()}</span>
            <h2 id="opec-modal-title">{job.denominacion}</h2>
            <p>{job.entidad}</p>
          </div>
          <button ref={closeButtonRef} type="button" className="opec-modal-close" onClick={onClose} aria-label="Cerrar detalle">
            <CloseIcon />
          </button>
        </div>

        <div className="opec-modal-summary">
          <div><small>Ubicación</small><strong>{job.municipio}, {job.departamento}</strong></div>
          <div><small>Salario</small><strong>{currency.format(job.salario)}</strong></div>
          <div><small>Experiencia</small><strong>{formatExperience(job.experienciaMeses)}</strong></div>
          <div><small>Vacantes</small><strong>{job.vacantes}</strong></div>
        </div>

        <div className="opec-modal-body">
          {loading && (
            <div className="opec-detail-loading" role="status">
              <span className="opec-spinner" /> Cargando información completa…
            </div>
          )}
          {error && <div className="opec-detail-error">{error}</div>}
          {detail && (
            <>
              <div className="opec-detail-section opec-requirements">
                <span className="opec-section-label">¿Qué necesitas para aplicar?</span>
                <h3>Requisitos del empleo</h3>
                <div className="opec-requirement-grid">
                  <div><span aria-hidden="true">🎓</span><p><strong>Estudios</strong>{detail.requisitoEstudio}</p></div>
                  <div><span aria-hidden="true">💼</span><p><strong>Experiencia</strong>{detail.requisitoExperiencia}</p></div>
                  {detail.requisitoOtros && <div><span aria-hidden="true">📋</span><p><strong>Otros requisitos</strong>{detail.requisitoOtros}</p></div>}
                </div>
              </div>

              <div className="opec-detail-section">
                <span className="opec-section-label">Tu misión en el cargo</span>
                <h3>Propósito principal</h3>
                <p>{detail.proposito}</p>
              </div>

              <details className="opec-functions">
                <summary>Ver las {detail.funciones.length} funciones del empleo <span aria-hidden="true">⌄</span></summary>
                <ol>
                  {detail.funciones.map((item, index) => <li key={`${index}-${item.slice(0, 24)}`}>{item}</li>)}
                </ol>
              </details>

              <div className="opec-technical">
                <span><small>Código</small>{detail.codigo}</span>
                <span><small>Grado</small>{detail.grado}</span>
                <span><small>Dependencia</small>{detail.dependencia}</span>
                <span><small>Vigencia salarial</small>{detail.vigenciaSalario}</span>
              </div>
            </>
          )}
        </div>

        <div className="opec-modal-actions">
          <button type="button" className={`opec-copy-button${copied ? " copied" : ""}`} onClick={() => onCopy(job.opec)}>
            <CopyIcon /> {copied ? "OPEC copiada" : `Copiar OPEC ${job.opec}`}
          </button>
          <a href="https://simo.cnsc.gov.co/" target="_blank" rel="noopener noreferrer" className="opec-simo-button">
            Ir a SIMO <span aria-hidden="true">↗</span>
          </a>
          <Link href="/comprar" className="opec-course-link">Prepararme para este cargo</Link>
        </div>
        <p className="opec-modal-note">Copia el número, abre SIMO y úsalo en la búsqueda de oferta pública. Confirma allí los datos antes de inscribirte.</p>
      </section>
    </div>
  );
}

export default function BuscadorOpec() {
  const [payload, setPayload] = useState<OpecIndexPayload | null>(null);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");
  const [query, setQuery] = useState("");
  const [modality, setModality] = useState("Abierto");
  const [department, setDepartment] = useState("");
  const [municipality, setMunicipality] = useState("");
  const [level, setLevel] = useState("");
  const [education, setEducation] = useState("");
  const [experience, setExperience] = useState("");
  const [additionalRequirement, setAdditionalRequirement] = useState("");
  const [minimumSalary, setMinimumSalary] = useState("");
  const [disability, setDisability] = useState(false);
  const [sort, setSort] = useState("relevance");
  const [visibleCount, setVisibleCount] = useState(PAGE_SIZE);
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [selected, setSelected] = useState<OpecSummary | null>(null);
  const [detail, setDetail] = useState<OpecDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);
  const [detailError, setDetailError] = useState("");
  const [copiedOpec, setCopiedOpec] = useState<number | null>(null);
  const detailCache = useRef(new Map<number, OpecDetail>());
  const detailRequest = useRef<{ opec: number; controller: AbortController } | null>(null);
  const filtersRef = useRef<HTMLElement>(null);
  const filterCloseRef = useRef<HTMLButtonElement>(null);

  const closeDetail = useCallback(() => {
    detailRequest.current?.controller.abort();
    detailRequest.current = null;
    setSelected(null);
    setDetailLoading(false);
  }, []);

  const closeFilters = useCallback(() => setFiltersOpen(false), []);
  useFocusTrap(filtersOpen, filtersRef, filterCloseRef, closeFilters);

  useEffect(() => {
    const controller = new AbortController();
    fetch("/data/opec-index.json", { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error("No fue posible cargar las vacantes.");
        return response.json() as Promise<OpecIndexPayload>;
      })
      .then((data) => setPayload(data))
      .catch((error: Error) => {
        if (error.name !== "AbortError") setLoadError(error.message);
      })
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, []);

  useEffect(() => {
    const desktop = window.matchMedia("(min-width: 821px)");
    const closeDrawerOnDesktop = (event: MediaQueryListEvent) => {
      if (event.matches) setFiltersOpen(false);
    };
    desktop.addEventListener("change", closeDrawerOnDesktop);
    return () => desktop.removeEventListener("change", closeDrawerOnDesktop);
  }, []);

  useEffect(() => {
    setVisibleCount(PAGE_SIZE);
  }, [query, modality, department, municipality, level, education, experience, additionalRequirement, minimumSalary, disability, sort]);

  const jobs = payload?.empleos ?? [];
  const departments = useMemo(
    () => Array.from(new Set(jobs.map((job) => job.departamento))).sort((a, b) => a.localeCompare(b, "es")),
    [jobs]
  );
  const municipalities = useMemo(
    () => Array.from(new Set(
      jobs.filter((job) => !department || job.departamento === department).map((job) => job.municipio)
    )).sort((a, b) => a.localeCompare(b, "es")),
    [jobs, department]
  );

  const filteredJobs = useMemo(() => {
    const normalizedQuery = normalize(query);
    const terms = normalizedQuery.split(" ").filter(Boolean);
    const salary = minimumSalary ? Number(minimumSalary) : 0;

    const result = jobs.filter((job) => {
      if (modality && job.modalidad !== modality) return false;
      if (department && job.departamento !== department) return false;
      if (municipality && job.municipio !== municipality) return false;
      if (level && job.nivel !== level) return false;
      if (education && job.nivelEstudio !== education) return false;
      if (additionalRequirement === "none" && job.requisitosAdicionales.length) return false;
      if (
        additionalRequirement
        && additionalRequirement !== "none"
        && !job.requisitosAdicionales.some((requirement) => requirement === additionalRequirement)
      ) return false;
      if (salary && job.salario < salary) return false;
      if (disability && !job.discapacidad) return false;
      if (experience === "0" && job.experienciaMeses !== 0) return false;
      if (["6", "12", "24", "36"].includes(experience)) {
        const maximum = Number(experience);
        if (job.experienciaMeses === null || job.experienciaMeses > maximum) return false;
      }
      if (experience === "37+" && (job.experienciaMeses === null || job.experienciaMeses <= 36)) return false;
      if (!matchesSearch(job, normalizedQuery)) return false;
      return true;
    });

    return result.sort((a, b) => {
      if (sort === "salary-desc") return b.salario - a.salario;
      if (sort === "salary-asc") return a.salario - b.salario;
      if (sort === "vacancies") return b.vacantes - a.vacantes || b.salario - a.salario;
      if (sort === "experience") {
        return (a.experienciaMeses ?? 999) - (b.experienciaMeses ?? 999) || b.salario - a.salario;
      }
      if (terms.length) {
        const normalizedDenominationA = normalize(a.denominacion);
        const normalizedDenominationB = normalize(b.denominacion);
        const score = (item: OpecSummary, denomination: string) => {
          let value = 0;
          if (String(item.opec) === normalizedQuery) value += 100;
          if (denomination.startsWith(normalizedQuery)) value += 40;
          if (denomination.includes(normalizedQuery)) value += 20;
          return value;
        };
        const difference = score(b, normalizedDenominationB) - score(a, normalizedDenominationA);
        if (difference) return difference;
      }
      return b.vacantes - a.vacantes || b.salario - a.salario;
    });
  }, [jobs, query, modality, department, municipality, level, education, experience, additionalRequirement, minimumSalary, disability, sort]);

  const activeFilters = [
    department,
    municipality,
    level,
    education,
    experience,
    additionalRequirement,
    minimumSalary,
    disability ? "disability" : "",
  ].filter(Boolean).length;

  function resetFilters() {
    setDepartment("");
    setMunicipality("");
    setLevel("");
    setEducation("");
    setExperience("");
    setAdditionalRequirement("");
    setMinimumSalary("");
    setDisability(false);
  }

  async function copyOpec(opec: number) {
    try {
      await navigator.clipboard.writeText(String(opec));
      setCopiedOpec(opec);
      window.setTimeout(() => setCopiedOpec((current) => current === opec ? null : current), 1800);
    } catch {
      setCopiedOpec(null);
    }
  }

  async function openDetail(job: OpecSummary) {
    detailRequest.current?.controller.abort();
    detailRequest.current = null;
    setSelected(job);
    setDetailError("");

    const cached = detailCache.current.get(job.opec);
    if (cached) {
      setDetail(cached);
      setDetailLoading(false);
      return;
    }

    const controller = new AbortController();
    detailRequest.current = { opec: job.opec, controller };
    setDetail(null);
    setDetailLoading(true);
    try {
      const response = await fetch(getOpecDetailUrl(job.opec), { signal: controller.signal });
      if (!response.ok) throw new Error("No pudimos cargar el detalle. Intenta nuevamente.");
      const shard = await response.json() as OpecDetailShard;
      const selectedDetail = shard.empleos[String(job.opec)];
      if (!selectedDetail) throw new Error("No encontramos el detalle de esta OPEC.");
      detailCache.current.set(job.opec, selectedDetail);
      if (detailRequest.current?.opec === job.opec) setDetail(selectedDetail);
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") return;
      if (detailRequest.current?.opec === job.opec) {
        setDetailError(error instanceof Error ? error.message : "Ocurrió un error inesperado.");
      }
    } finally {
      if (detailRequest.current?.opec === job.opec) {
        detailRequest.current = null;
        setDetailLoading(false);
      }
    }
  }

  return (
    <>
      <div className="opec-search-shell">
        <div className="opec-search-main">
          <div className="opec-search-box">
            <SearchIcon />
            <label htmlFor="opec-query" className="sr-only">Buscar por OPEC, cargo, profesión, entidad o ciudad</label>
            <input
              id="opec-query"
              type="search"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Busca por OPEC, cargo, profesión, entidad o ciudad…"
              autoComplete="off"
            />
            {query && <button type="button" onClick={() => setQuery("")} aria-label="Borrar búsqueda"><CloseIcon /></button>}
          </div>
          <button
            type="button"
            className="opec-mobile-filter"
            onClick={() => setFiltersOpen(!filtersOpen)}
            aria-expanded={filtersOpen}
            aria-controls="opec-filter-panel"
          >
            <span aria-hidden="true">☷</span> Filtros {activeFilters > 0 && <b>{activeFilters}</b>}
          </button>
        </div>

        <div className="opec-quick-row">
          <span>Tipo de concurso:</span>
          <div className="opec-segmented" role="group" aria-label="Tipo de concurso">
            <button type="button" aria-pressed={modality === "Abierto"} className={modality === "Abierto" ? "active" : ""} onClick={() => setModality("Abierto")}>Abierto</button>
            <button type="button" aria-pressed={modality === "Ascenso"} className={modality === "Ascenso" ? "active" : ""} onClick={() => setModality("Ascenso")}>Ascenso</button>
            <button type="button" aria-pressed={modality === ""} className={modality === "" ? "active" : ""} onClick={() => setModality("")}>Todos</button>
          </div>
          <button
            type="button"
            aria-pressed={experience === "0"}
            className={`opec-no-experience${experience === "0" ? " active" : ""}`}
            onClick={() => setExperience(experience === "0" ? "" : "0")}
          >
            <span aria-hidden="true">✓</span> Sin experiencia
          </button>
          <button
            type="button"
            aria-pressed={education === "bachiller-solo"}
            className={`opec-quick-study${education === "bachiller-solo" ? " active" : ""}`}
            onClick={() => setEducation(education === "bachiller-solo" ? "" : "bachiller-solo")}
          >
            <span aria-hidden="true">🎓</span> Solo bachiller
          </button>
        </div>
      </div>

      <div className="opec-layout">
        <aside
          ref={filtersRef}
          id="opec-filter-panel"
          className={`opec-filters${filtersOpen ? " mobile-open" : ""}`}
          aria-label="Filtros de vacantes"
          role={filtersOpen ? "dialog" : "complementary"}
          aria-modal={filtersOpen ? true : undefined}
          aria-labelledby="opec-filters-title"
          tabIndex={filtersOpen ? -1 : undefined}
        >
          <button
            ref={filterCloseRef}
            type="button"
            className="opec-filter-close"
            onClick={closeFilters}
            aria-label="Cerrar filtros"
          >×</button>
          <Filters
            departments={departments}
            municipalities={municipalities}
            department={department}
            municipality={municipality}
            level={level}
            education={education}
            experience={experience}
            additionalRequirement={additionalRequirement}
            minimumSalary={minimumSalary}
            disability={disability}
            onDepartment={(value) => { setDepartment(value); setMunicipality(""); }}
            onMunicipality={setMunicipality}
            onLevel={setLevel}
            onEducation={setEducation}
            onExperience={setExperience}
            onAdditionalRequirement={setAdditionalRequirement}
            onMinimumSalary={setMinimumSalary}
            onDisability={setDisability}
            onReset={resetFilters}
          />
          <button type="button" className="opec-apply-mobile" onClick={closeFilters}>Ver {filteredJobs.length.toLocaleString("es-CO")} resultados</button>
        </aside>

        <section className="opec-results" aria-live="polite" aria-busy={loading}>
          <div className="opec-results-head">
            <div>
              <span className="opec-result-count">
                {loading ? "Consultando vacantes…" : `${filteredJobs.length.toLocaleString("es-CO")} ${filteredJobs.length === 1 ? "oportunidad encontrada" : "oportunidades encontradas"}`}
              </span>
              {!loading && payload && <small>Datos actualizados al {formatOpecDate(payload.meta.fechaActualizacion)}</small>}
            </div>
            <label className="opec-sort">
              <span>Ordenar por</span>
              <select value={sort} onChange={(event) => setSort(event.target.value)}>
                <option value="relevance">Más relevantes</option>
                <option value="vacancies">Más vacantes</option>
                <option value="experience">Menor experiencia</option>
                <option value="salary-desc">Mayor salario</option>
                <option value="salary-asc">Menor salario</option>
              </select>
            </label>
          </div>

          {loading && (
            <div className="opec-loading-grid" role="status">
              {[1, 2, 3, 4].map((item) => <div className="opec-card-skeleton" key={item}><i /><i /><i /><i /></div>)}
              <span className="sr-only">Cargando vacantes</span>
            </div>
          )}

          {loadError && (
            <div className="opec-empty"><EmptyIcon /><h3>No pudimos cargar las vacantes</h3><p>{loadError}</p><button type="button" onClick={() => window.location.reload()}>Intentar nuevamente</button></div>
          )}

          {!loading && !loadError && filteredJobs.length === 0 && (
            <div className="opec-empty">
              <EmptyIcon />
              <h3>No encontramos coincidencias</h3>
              <p>Prueba con otra palabra o elimina algunos filtros para ampliar los resultados.</p>
              <button type="button" onClick={() => { setQuery(""); resetFilters(); setModality("Abierto"); }}>Limpiar búsqueda</button>
            </div>
          )}

          {!loading && filteredJobs.length > 0 && (
            <>
              <div className="opec-grid">
                {filteredJobs.slice(0, visibleCount).map((job) => (
                  <JobCard key={job.opec} job={job} onOpen={openDetail} onCopy={copyOpec} copied={copiedOpec === job.opec} />
                ))}
              </div>
              {visibleCount < filteredJobs.length && (
                <div className="opec-load-more">
                  <button type="button" onClick={() => setVisibleCount((count) => count + PAGE_SIZE)}>Ver más oportunidades</button>
                  <span>Mostrando {Math.min(visibleCount, filteredJobs.length)} de {filteredJobs.length.toLocaleString("es-CO")}</span>
                </div>
              )}
            </>
          )}
        </section>
      </div>

      {selected && (
        <DetailModal
          job={selected}
          detail={detail}
          loading={detailLoading}
          error={detailError}
          copied={copiedOpec === selected.opec}
          onClose={closeDetail}
          onCopy={copyOpec}
        />
      )}
    </>
  );
}

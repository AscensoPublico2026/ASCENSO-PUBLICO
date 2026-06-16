/**
 * Catálogo de guías de la BIBLIOTECA (fuente: biblioteca/biblioteca.json).
 *
 * Este módulo lee la copia de `biblioteca.json` incluida en el deploy
 * (plataforma/lib/biblioteca.json) y la normaliza al modelo que usa la
 * base de datos (tabla `guias_curso`, enum `tipo_guia`).
 *
 * Sirve para que el admin pueda ASIGNAR una guía existente a un curso
 * por su CÓDIGO (desplegable), sin volver a subir el HTML: el archivo ya
 * vive en el bucket `guias` de Storage (subido vía /api/admin/seed-guias).
 *
 * ⚠️ MANTENER SINCRONIZADO: cuando se actualice /biblioteca/biblioteca.json
 * (al crear/registrar una guía nueva), copiarlo a plataforma/lib/biblioteca.json
 * (ver scripts/sync-biblioteca.sh) para que la plataforma la reconozca.
 */

import bibliotecaJson from "./biblioteca.json";

// Tipos del enum de la BD (schema.sql: tipo_guia)
export type TipoGuiaDB = "general" | "nivel" | "funcional" | "bonus" | "simulacro";

export interface GuiaCatalogo {
  codigo: string;
  titulo: string;
  /** Día sugerido en el plan (puede ajustarse por cliente). */
  diaSugerido: number | null;
  /** Tipo normalizado para la BD (enum tipo_guia). */
  tipo: TipoGuiaDB;
  /** Biblioteca/categoría original (Introducción, General, Por Nivel, Funcional, ...). */
  biblioteca: string;
  /** Nivel (Asistencial | Técnico | Profesional) o null si aplica a todos. */
  nivel: string | null;
  estado: string;
  /** Ruta del objeto en el bucket `guias` de Storage (ej. "guias/FUN-ALM-01-...html"). */
  archivoPath: string | null;
  reutilizable: boolean;
}

interface BibliotecaEntry {
  codigo: string;
  dia: number | null;
  titulo: string;
  biblioteca: string;
  nivel: string | null;
  tipo: string;
  estado: string;
  archivo: string | null;
  reutilizable?: boolean;
}

// Mapeo: biblioteca/categoría → enum tipo_guia de la BD.
function mapTipoDB(biblioteca: string): TipoGuiaDB {
  switch (biblioteca) {
    case "Funcional":
      return "funcional";
    case "Simulacro Final":
      return "simulacro";
    case "Bonus":
      return "bonus";
    case "Por Nivel":
      return "nivel";
    // "Introducción", "General", "Por Entidad" → se muestran en el Plan de estudio.
    default:
      return "general";
  }
}

const raw = (bibliotecaJson as { guias: BibliotecaEntry[] }).guias || [];

export const CATALOGO_GUIAS: GuiaCatalogo[] = raw.map((g) => ({
  codigo: g.codigo,
  titulo: g.titulo,
  diaSugerido: g.dia ?? null,
  tipo: mapTipoDB(g.biblioteca),
  biblioteca: g.biblioteca,
  nivel: g.nivel ?? null,
  estado: g.estado,
  archivoPath: g.archivo ?? null,
  reutilizable: g.reutilizable ?? false,
}));

/** Busca una guía del catálogo por su código (ej. "FUN-ALM-01"). */
export function getGuiaCatalogo(codigo: string): GuiaCatalogo | undefined {
  return CATALOGO_GUIAS.find((g) => g.codigo === codigo);
}

/**
 * Guías publicadas que YA tienen su HTML disponible en Storage
 * (estado "publicada" + archivo). Son las que pueden subirse al bucket
 * y asignarse a un curso por código.
 */
export function guiasPublicadasConArchivo(): GuiaCatalogo[] {
  return CATALOGO_GUIAS.filter((g) => g.estado === "publicada" && !!g.archivoPath);
}

/**
 * Guías que el admin asigna manualmente desde el desplegable:
 * funcionales y simulacro (las generales/nivel/bonus se auto-cargan al comprar).
 * Devuelve solo las publicadas y con archivo en Storage.
 */
export function guiasAsignables(): GuiaCatalogo[] {
  return guiasPublicadasConArchivo()
    .filter((g) => g.tipo === "funcional" || g.tipo === "simulacro")
    .sort((a, b) => {
      // Funcionales primero (por código), simulacro al final.
      if (a.tipo !== b.tipo) return a.tipo === "simulacro" ? 1 : -1;
      return a.codigo.localeCompare(b.codigo);
    });
}

/** Lista de nombres de archivo (basename) de todas las guías publicadas con archivo. */
export function archivosSeed(): string[] {
  return guiasPublicadasConArchivo()
    .map((g) => (g.archivoPath ? g.archivoPath.replace(/^guias\//, "") : ""))
    .filter(Boolean);
}

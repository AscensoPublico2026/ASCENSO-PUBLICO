export type OpecModalidad = "Abierto" | "Ascenso";
export type OpecTipoReferencia = "OPEC" | "Código";
export type OpecNivelEstudio =
  | "primaria-laboral"
  | "secundaria-aprobada"
  | "bachiller-solo"
  | "bachiller-curso"
  | "tecnico-laboral"
  | "tecnico-tecnologo"
  | "universitario-sin-titulo"
  | "profesional"
  | "posgrado"
  | "curso-especifico";

export type OpecRequisitoAdicional =
  | "rethus"
  | "tarjeta-profesional"
  | "licencia-conduccion"
  | "licencia-sst"
  | "registro-archivistas"
  | "soporte-vital"
  | "radioproteccion"
  | "antecedentes-contador"
  | "cedula"
  | "otro";

export interface OpecConvocatoriaMeta {
  id: string;
  nombre: string;
  totalOpec: number;
  totalVacantes: number;
}

export interface OpecMeta {
  convocatoria: string;
  fechaActualizacion: string;
  totalOpec: number;
  totalVacantes: number;
  opecAbiertas: number;
  vacantesAbiertas: number;
  entidades: number;
  departamentos: number;
  municipios: number;
  sinExperiencia: number;
  totalConvocatorias: number;
  convocatorias: OpecConvocatoriaMeta[];
  fuente: string;
}

export interface OpecSummary {
  id: string;
  referencia: string;
  tipoReferencia: OpecTipoReferencia;
  convocatoriaId: string;
  convocatoriaNombre: string;
  denominacion: string;
  nivel: string;
  grado: string;
  codigo: string;
  salario: number;
  vigenciaSalario: number;
  entidad: string;
  departamento: string;
  municipio: string;
  vacantes: number;
  disponibles: number;
  modalidad: OpecModalidad;
  discapacidad: boolean;
  sinExperiencia: boolean;
  experienciaMeses: number | null;
  nivelEstudio: OpecNivelEstudio;
  estudioResumen: string;
  estudioDetalleCorto: string;
  requisitosAdicionales: OpecRequisitoAdicional[];
  requisitosAdicionalesResumen: string[];
  perfilFormacion: string;
  perfilExperiencia: string;
  perfilFunciones: string;
  busqueda: string;
}

export interface OpecDetail
  extends Omit<
    OpecSummary,
    "busqueda" | "perfilFormacion" | "perfilExperiencia" | "perfilFunciones"
  > {
  nit: string;
  tipoEntidad: string;
  convocatoriaDetalle: string;
  anio: number;
  tipoProceso: string;
  dependencia: string;
  concursoAscenso: boolean;
  proposito: string;
  funciones: string[];
  requisitoEstudio: string;
  requisitoExperiencia: string;
  requisitoOtros: string;
  urlOficial: string;
}

export interface OpecIndexPayload {
  meta: OpecMeta;
  empleos: OpecSummary[];
}

export interface OpecDetailShard {
  empleos: Record<string, OpecDetail>;
}

export const OPEC_DETAIL_SHARDS = 32;

export function getOpecDetailUrl(id: string): string {
  const value = Array.from(id).reduce((total, character) => total + character.charCodeAt(0), 0);
  const shard = String(value % OPEC_DETAIL_SHARDS).padStart(2, "0");
  return `/data/opec-details/${shard}.json`;
}

export function formatOpecDate(isoDate: string): string {
  return new Intl.DateTimeFormat("es-CO", {
    day: "numeric",
    month: "long",
    year: "numeric",
    timeZone: "America/Bogota",
  }).format(new Date(`${isoDate}T12:00:00-05:00`));
}

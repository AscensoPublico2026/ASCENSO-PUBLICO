export type OpecModalidad = "Abierto" | "Ascenso";
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
  fuente: string;
}

export interface OpecSummary {
  opec: number;
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
  busqueda: string;
}

export interface OpecDetail extends Omit<OpecSummary, "busqueda"> {
  nit: string;
  tipoEntidad: string;
  convocatoria: string;
  anio: number;
  tipoProceso: string;
  dependencia: string;
  concursoAscenso: boolean;
  proposito: string;
  funciones: string[];
  requisitoEstudio: string;
  requisitoExperiencia: string;
  requisitoOtros: string;
}

export interface OpecIndexPayload {
  meta: OpecMeta;
  empleos: OpecSummary[];
}

export interface OpecDetailShard {
  empleos: Record<string, OpecDetail>;
}

export const OPEC_DETAIL_SHARDS = 32;

export function getOpecDetailUrl(opec: number): string {
  const shard = String(opec % OPEC_DETAIL_SHARDS).padStart(2, "0");
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

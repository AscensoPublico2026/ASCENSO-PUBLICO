"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useRef, useState, type RefObject } from "react";
import {
  formatOpecDate,
  getOpecDetailUrl,
  type OpecConvocatoriaMeta,
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

const PROFILE_STOP_WORDS = new Set([
  "actualmente", "ademas", "anos", "año", "años", "busco", "como", "con", "cuento",
  "de", "del", "desde", "donde", "durante", "el", "ella", "en", "entre", "esta", "este",
  "experiencia", "formacion", "he", "la", "las", "los", "me", "meses", "mi", "mis", "para",
  "perfil", "por", "profesional", "que", "quiero", "sin", "soy", "tengo", "trabajado", "trabaje",
  "trabajo", "un", "una", "y",
]);

const SYNONYM_GROUPS = [
  ["abogado", "abogada", "derecho", "juridico", "juridica", "legal"],
  ["administrador", "administradora", "administracion", "administrativo", "administrativa"],
  ["contador", "contadora", "contaduria", "contable", "contabilidad"],
  ["ingeniero", "ingeniera", "ingenieria"],
  ["sistemas", "software", "programacion", "informatica", "tecnologia", "tic"],
  ["enfermero", "enfermera", "enfermeria"],
  ["medico", "medica", "medicina", "clinico", "clinica"],
  ["psicologo", "psicologa", "psicologia"],
  ["economista", "economia", "economico", "economica"],
  ["archivo", "archivista", "archivistica", "documental"],
  ["finanzas", "financiero", "financiera", "presupuesto", "tesoreria"],
  ["talento", "humano", "recursos", "nomina", "personal"],
  ["servicio", "ciudadano", "usuario", "atencion", "pqrs"],
  ["salud", "sanitario", "sanitaria", "hospital", "asistencial"],
  ["contratacion", "contratos", "contractual"],
  ["planeacion", "planificacion", "proyectos"],
  ["auditoria", "control", "riesgos"],
  ["comunicador", "comunicadora", "comunicacion", "periodismo"],
  ["trabajador", "trabajadora", "social", "sociologia"],
  ["tecnico", "tecnica", "tecnologo", "tecnologa"],
  ["bachiller", "bachillerato", "secundaria"],
];

function normalize(value: string): string {
  return value
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function splitValues(value: string): string[] {
  return value.split("|").map((item) => item.trim()).filter(Boolean);
}

function tokenMatches(text: string, alias: string): boolean {
  const tokens = text.split(" ");
  return tokens.includes(alias) || (alias.length >= 5 && tokens.some((token) => token.startsWith(alias)));
}

function aliasesFor(term: string): string[] {
  const group = SYNONYM_GROUPS.find((items) => items.includes(term));
  return group ?? [term];
}

function profileTerms(query: string): string[] {
  return Array.from(new Set(
    normalize(query)
      .split(" ")
      .filter((term) => term.length >= 3 && !PROFILE_STOP_WORDS.has(term) && !/^\d+$/.test(term)),
  ));
}

function educationRankFromProfile(query: string): number | null {
  const normalized = normalize(query);
  if (/doctorado|maestria|especializacion|especialista|posgrado/.test(normalized)) return 9;
  if (/abogad|administrador|contador|ingenier|medic|enfermer|psicolog|economista|arquitect|universitari|profesion/.test(normalized)) return 8;
  if (/tecnolog/.test(normalized)) return 6;
  if (/tecnic/.test(normalized)) return 5;
  if (/bachiller|secundaria/.test(normalized)) return 3;
  if (/primaria/.test(normalized)) return 1;
  return null;
}

function educationRankFromJob(job: OpecSummary): number {
  const ranks: Record<OpecSummary["nivelEstudio"], number> = {
    "primaria-laboral": 1,
    "secundaria-aprobada": 2,
    "bachiller-solo": 3,
    "bachiller-curso": 4,
    "tecnico-laboral": 5,
    "tecnico-tecnologo": 6,
    "universitario-sin-titulo": 7,
    profesional: 8,
    posgrado: 9,
    "curso-especifico": 4,
  };
  return ranks[job.nivelEstudio];
}

function experienceFromProfile(query: string): number | null {
  const normalized = normalize(query);
  const matches = Array.from(normalized.matchAll(/(\d+)\s*(anos?|mes(?:es)?)/g));
  if (!matches.length) return /sin experiencia/.test(normalized) ? 0 : null;
  return Math.max(...matches.map((match) => Number(match[1]) * (match[2].startsWith("ano") ? 12 : 1)));
}

interface SmartMatch {
  score: number;
  compatibility: number;
  reasons: string[];
}

function scoreProfile(job: OpecSummary, query: string): SmartMatch | null {
  const normalizedQuery = normalize(query);
  if (!normalizedQuery) return null;
  if (normalizedQuery === normalize(job.referencia)) {
    return { score: 500, compatibility: 99, reasons: [`Coincide exactamente con ${job.tipoReferencia}`] };
  }

  const terms = profileTerms(query);
  if (!terms.length) return null;
  let score = 0;
  let matchedTerms = 0;
  let denominationMatches = 0;
  let educationMatches = 0;
  let functionMatches = 0;

  for (const term of terms) {
    const aliases = aliasesFor(term);
    const inDenomination = aliases.some((alias) => tokenMatches(normalize(job.denominacion), alias));
    const inEducation = aliases.some((alias) => tokenMatches(job.perfilFormacion, alias));
    const inFunctions = aliases.some((alias) => tokenMatches(job.perfilFunciones, alias));
    const inGeneral = aliases.some((alias) => tokenMatches(job.busqueda, alias));
    const best = inDenomination ? 14 : inEducation ? 11 : inFunctions ? 7 : inGeneral ? 3 : 0;
    if (best) {
      score += best;
      matchedTerms += 1;
      if (inDenomination) denominationMatches += 1;
      if (inEducation) educationMatches += 1;
      if (inFunctions) functionMatches += 1;
    }
  }

  const coverage = matchedTerms / terms.length;
  if (!matchedTerms || (score < 8 && coverage < 0.2)) return null;
  score += coverage * 22;

  const reasons: string[] = [];
  if (educationMatches) reasons.push("Formación relacionada");
  if (denominationMatches) reasons.push("Cargo afín a tu perfil");
  if (functionMatches) reasons.push("Funciones relacionadas");

  const profileEducationRank = educationRankFromProfile(query);
  if (profileEducationRank !== null) {
    if (profileEducationRank >= educationRankFromJob(job)) {
      score += 10;
      reasons.push("Nivel de estudios compatible");
    } else {
      score -= 16;
    }
  }

  const profileExperience = experienceFromProfile(query);
  if (profileExperience !== null && job.experienciaMeses !== null) {
    if (profileExperience >= job.experienciaMeses) {
      score += 12;
      reasons.push("Experiencia suficiente");
    } else {
      score -= Math.min(18, (job.experienciaMeses - profileExperience) / 2);
    }
  }

  if (score <= 0) return null;
  const compatibility = Math.max(35, Math.min(99, Math.round(38 + coverage * 34 + Math.min(score, 45) * 0.55)));
  return { score, compatibility, reasons: Array.from(new Set(reasons)).slice(0, 3) };
}

function matchesSearch(job: OpecSummary, normalizedQuery: string): boolean {
  const terms = normalizedQuery.split(" ").filter(Boolean);
  if (!terms.length) return true;
  return terms.every((term) => {
    if (/^\d+$/.test(term)) return normalize(job.referencia).startsWith(term);
    if (tokenMatches(job.busqueda, term)) return true;
    return aliasesFor(term).some((alias) => tokenMatches(job.busqueda, alias));
  });
}

const FOCUSABLE_SELECTOR = [
  "a[href]", "button:not([disabled])", "input:not([disabled])", "select:not([disabled])",
  "textarea:not([disabled])", "[tabindex]:not([tabindex='-1'])",
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
      const focusable = Array.from(containerRef.current.querySelectorAll<HTMLElement>(FOCUSABLE_SELECTOR))
        .filter((element) => !element.hasAttribute("disabled"));
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
  return <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7" /><path d="m20 20-4-4" /></svg>;
}
function CloseIcon() {
  return <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18" /></svg>;
}
function CopyIcon() {
  return <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="11" height="11" rx="2" /><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2" /></svg>;
}
function EmptyIcon() {
  return <svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="28" cy="28" r="18" /><path d="m42 42 13 13M20 28h16M28 20v16" /></svg>;
}

interface FiltersProps {
  convocatorias: OpecConvocatoriaMeta[];
  departments: string[];
  municipalities: string[];
  levels: string[];
  convocatoria: string;
  department: string;
  municipality: string;
  level: string;
  education: string;
  experience: string;
  additionalRequirement: string;
  minimumSalary: string;
  disability: boolean;
  onConvocatoria: (value: string) => void;
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
  convocatorias, departments, municipalities, levels, convocatoria, department, municipality,
  level, education, experience, additionalRequirement, minimumSalary, disability, onConvocatoria,
  onDepartment, onMunicipality, onLevel, onEducation, onExperience, onAdditionalRequirement,
  onMinimumSalary, onDisability, onReset,
}: FiltersProps) {
  return (
    <div className="opec-filter-fields">
      <div className="opec-filter-head">
        <div><span className="opec-filter-kicker">Personaliza tu búsqueda</span><h2 id="opec-filters-title">Filtros</h2></div>
        <button type="button" className="opec-reset" onClick={onReset}>Limpiar</button>
      </div>
      <label className="opec-field opec-field-highlight">
        <span>Convocatoria</span>
        <select value={convocatoria} onChange={(event) => onConvocatoria(event.target.value)}>
          <option value="">Todas las convocatorias</option>
          {convocatorias.map((item) => <option key={item.id} value={item.id}>{item.nombre}</option>)}
        </select>
      </label>
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
          {levels.map((item) => <option key={item} value={item}>{item}</option>)}
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
          <option value="0">Sin experiencia</option><option value="6">Hasta 6 meses</option>
          <option value="12">Hasta 12 meses</option><option value="24">Hasta 24 meses</option>
          <option value="36">Hasta 36 meses</option><option value="37+">Más de 36 meses</option>
        </select>
      </label>
      <label className="opec-field">
        <span>Requisito adicional</span>
        <select value={additionalRequirement} onChange={(event) => onAdditionalRequirement(event.target.value)}>
          <option value="">Cualquier requisito adicional</option><option value="none">Sin requisito adicional registrado</option>
          <option value="rethus">Requiere ReTHUS</option><option value="tarjeta-profesional">Tarjeta o matrícula profesional</option>
          <option value="licencia-conduccion">Licencia de conducción</option><option value="licencia-sst">Licencia en seguridad y salud</option>
          <option value="registro-archivistas">Registro profesional de archivistas</option><option value="soporte-vital">Certificado de soporte vital básico</option>
          <option value="radioproteccion">Carné de radioprotección</option><option value="antecedentes-contador">Antecedentes de contador</option>
          <option value="cedula">Cédula de ciudadanía</option><option value="otro">Otro requisito adicional</option>
        </select>
      </label>
      <label className="opec-field">
        <span>Salario desde</span>
        <select value={minimumSalary} onChange={(event) => onMinimumSalary(event.target.value)}>
          <option value="">Cualquier salario</option><option value="2000000">$2.000.000</option>
          <option value="3000000">$3.000.000</option><option value="4000000">$4.000.000</option>
          <option value="5000000">$5.000.000</option><option value="7000000">$7.000.000</option>
          <option value="10000000">$10.000.000</option>
        </select>
      </label>
      <label className="opec-check">
        <input type="checkbox" checked={disability} onChange={(event) => onDisability(event.target.checked)} />
        <span className="opec-check-box" aria-hidden="true">✓</span>
        <span><strong>Reserva para discapacidad</strong><small>Mostrar únicamente empleos con reserva.</small></span>
      </label>
    </div>
  );
}

function JobCard({ job, match, onOpen, onCopy, copied }: {
  job: OpecSummary;
  match?: SmartMatch;
  onOpen: (job: OpecSummary) => void;
  onCopy: (job: OpecSummary) => void;
  copied: boolean;
}) {
  return (
    <article className="opec-card">
      <div className="opec-callout-row">
        <span className={`opec-callout opec-callout-${job.convocatoriaId}`}>{job.convocatoriaNombre}</span>
        {match && <span className="opec-match-score">{match.compatibility}% afinidad</span>}
      </div>
      <div className="opec-card-top">
        <div className="opec-badges">
          <span className={`opec-level opec-level-${normalize(job.nivel)}`}>{job.nivel}</span>
          {job.sinExperiencia && <span className="opec-badge-success">Sin experiencia</span>}
          {job.discapacidad && <span className="opec-badge-access">Reserva discapacidad</span>}
        </div>
        <button type="button" className={`opec-copy-mini${copied ? " copied" : ""}`} onClick={() => onCopy(job)} aria-label={`Copiar ${job.tipoReferencia} ${job.referencia}`}>
          <CopyIcon /> {copied ? "Copiado" : `${job.tipoReferencia} ${job.referencia}`}
        </button>
      </div>
      <h3>{job.denominacion}</h3>
      <p className="opec-entity">{job.entidad}</p>
      {match && match.reasons.length > 0 && (
        <div className="opec-match-reasons" aria-label="Razones de afinidad">
          {match.reasons.map((reason) => <span key={reason}>✓ {reason}</span>)}
        </div>
      )}
      <div className="opec-requirement-snapshot">
        <span className="opec-snapshot-title">Requisitos a simple vista</span>
        <div><span className="opec-snapshot-icon" aria-hidden="true">🎓</span><p><small>Estudios</small><strong>{job.estudioResumen}</strong><span className="opec-study-excerpt">{job.estudioDetalleCorto}</span></p></div>
        <div><span className="opec-snapshot-icon" aria-hidden="true">💼</span><p><small>Experiencia</small><strong>{formatExperience(job.experienciaMeses)}</strong></p></div>
        <div className={job.requisitosAdicionales.length ? "has-extra" : ""}>
          <span className="opec-snapshot-icon" aria-hidden="true">📋</span>
          <p><small>Otros requisitos</small><strong title={job.requisitosAdicionalesResumen.join(", ") || undefined}>{formatAdditionalRequirements(job)}</strong></p>
        </div>
      </div>
      <div className="opec-card-data">
        <div><span className="opec-data-icon" aria-hidden="true">⌖</span><span><small>Ubicación</small>{job.municipio}, {job.departamento}</span></div>
        <div><span className="opec-data-icon" aria-hidden="true">$</span><span><small>Asignación salarial</small>{currency.format(job.salario)}</span></div>
        <div><span className="opec-data-icon" aria-hidden="true">◎</span><span><small>Vacantes</small>{job.vacantes} {job.vacantes === 1 ? "vacante" : "vacantes"}</span></div>
      </div>
      <div className="opec-card-foot">
        <span className={`opec-modality ${job.modalidad === "Abierto" ? "open" : "promotion"}`}><i /> Concurso {job.modalidad.toLowerCase()}</span>
        <button type="button" className="opec-detail-button" onClick={() => onOpen(job)}>Ver empleo completo <span aria-hidden="true">→</span></button>
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
  onCopy: (job: OpecSummary) => void;
}) {
  const modalRef = useRef<HTMLElement>(null);
  const closeButtonRef = useRef<HTMLButtonElement>(null);
  useFocusTrap(true, modalRef, closeButtonRef, onClose);
  return (
    <div className="opec-modal-backdrop" role="presentation" onMouseDown={(event) => { if (event.target === event.currentTarget) onClose(); }}>
      <section ref={modalRef} className="opec-modal" role="dialog" aria-modal="true" aria-labelledby="opec-modal-title" tabIndex={-1}>
        <div className="opec-modal-head">
          <div>
            <span className="opec-modal-eyebrow">{job.convocatoriaNombre} · {job.tipoReferencia} {job.referencia}</span>
            <h2 id="opec-modal-title">{job.denominacion}</h2><p>{job.entidad}</p>
          </div>
          <button ref={closeButtonRef} type="button" className="opec-modal-close" onClick={onClose} aria-label="Cerrar detalle"><CloseIcon /></button>
        </div>
        <div className="opec-modal-summary">
          <div><small>Ubicación</small><strong>{job.municipio}, {job.departamento}</strong></div>
          <div><small>Salario</small><strong>{currency.format(job.salario)}</strong></div>
          <div><small>Experiencia</small><strong>{formatExperience(job.experienciaMeses)}</strong></div>
          <div><small>Vacantes</small><strong>{job.vacantes}</strong></div>
        </div>
        <div className="opec-modal-body">
          {loading && <div className="opec-detail-loading" role="status"><span className="opec-spinner" /> Cargando información completa…</div>}
          {error && <div className="opec-detail-error">{error}</div>}
          {detail && <>
            <div className="opec-detail-section opec-requirements">
              <span className="opec-section-label">¿Qué necesitas para aplicar?</span><h3>Requisitos del empleo</h3>
              <div className="opec-requirement-grid">
                <div><span aria-hidden="true">🎓</span><p><strong>Estudios</strong>{detail.requisitoEstudio || "No especificado en el consolidado"}</p></div>
                <div><span aria-hidden="true">💼</span><p><strong>Experiencia</strong>{detail.requisitoExperiencia || "No especificada en el consolidado"}</p></div>
                {detail.requisitoOtros && <div><span aria-hidden="true">📋</span><p><strong>Otros requisitos</strong>{detail.requisitoOtros}</p></div>}
              </div>
            </div>
            <div className="opec-detail-section"><span className="opec-section-label">Tu misión en el cargo</span><h3>Propósito principal</h3><p>{detail.proposito}</p></div>
            {detail.funciones.length > 0 && <details className="opec-functions"><summary>Ver las {detail.funciones.length} funciones del empleo <span aria-hidden="true">⌄</span></summary><ol>{detail.funciones.map((item, index) => <li key={`${index}-${item.slice(0, 24)}`}>{item}</li>)}</ol></details>}
            <div className="opec-technical">
              <span><small>Código del empleo</small>{detail.codigo || "No especificado"}</span><span><small>Grado</small>{detail.grado || "No especificado"}</span>
              <span><small>Dependencia</small>{detail.dependencia || "No especificada"}</span><span><small>Vigencia salarial</small>{detail.vigenciaSalario || "No especificada"}</span>
            </div>
          </>}
        </div>
        <div className="opec-modal-actions">
          <button type="button" className={`opec-copy-button${copied ? " copied" : ""}`} onClick={() => onCopy(job)}><CopyIcon /> {copied ? `${job.tipoReferencia} copiado` : `Copiar ${job.tipoReferencia} ${job.referencia}`}</button>
          {detail?.urlOficial && <a href={detail.urlOficial} target="_blank" rel="noopener noreferrer" className="opec-simo-button">Ir al sitio oficial <span aria-hidden="true">↗</span></a>}
          <Link href="/comprar" className="opec-course-link">Prepararme para este cargo</Link>
        </div>
        <p className="opec-modal-note">Confirma los requisitos, fechas y disponibilidad en el canal oficial antes de inscribirte.</p>
      </section>
    </div>
  );
}

export default function BuscadorOpec() {
  const [payload, setPayload] = useState<OpecIndexPayload | null>(null);
  const [loading, setLoading] = useState(true);
  const [loadError, setLoadError] = useState("");
  const [searchMode, setSearchMode] = useState<"smart" | "filters">("smart");
  const [query, setQuery] = useState("");
  const [convocatoria, setConvocatoria] = useState("");
  const [modality, setModality] = useState("");
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
  const [copiedId, setCopiedId] = useState<string | null>(null);
  const detailCache = useRef(new Map<string, OpecDetail>());
  const detailRequest = useRef<{ id: string; controller: AbortController } | null>(null);
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
      .then((response) => { if (!response.ok) throw new Error("No fue posible cargar las vacantes."); return response.json() as Promise<OpecIndexPayload>; })
      .then(setPayload)
      .catch((error: Error) => { if (error.name !== "AbortError") setLoadError(error.message); })
      .finally(() => setLoading(false));
    return () => controller.abort();
  }, []);

  useEffect(() => {
    const desktop = window.matchMedia("(min-width: 821px)");
    const closeDrawerOnDesktop = (event: MediaQueryListEvent) => { if (event.matches) setFiltersOpen(false); };
    desktop.addEventListener("change", closeDrawerOnDesktop);
    return () => desktop.removeEventListener("change", closeDrawerOnDesktop);
  }, []);

  useEffect(() => { setVisibleCount(PAGE_SIZE); }, [searchMode, query, convocatoria, modality, department, municipality, level, education, experience, additionalRequirement, minimumSalary, disability, sort]);

  const jobs = payload?.empleos ?? [];
  const convocatorias = payload?.meta.convocatorias ?? [];
  const jobsInCall = useMemo(() => jobs.filter((job) => !convocatoria || job.convocatoriaId === convocatoria), [jobs, convocatoria]);
  const departments = useMemo(() => Array.from(new Set(jobsInCall.flatMap((job) => splitValues(job.departamento)).filter((item) => item !== "No especificado"))).sort((a, b) => a.localeCompare(b, "es")), [jobsInCall]);
  const municipalities = useMemo(() => Array.from(new Set(jobsInCall.filter((job) => !department || splitValues(job.departamento).includes(department)).flatMap((job) => splitValues(job.municipio)).filter((item) => item !== "No especificado"))).sort((a, b) => a.localeCompare(b, "es")), [jobsInCall, department]);
  const levels = useMemo(() => Array.from(new Set(jobsInCall.map((job) => job.nivel))).sort((a, b) => a.localeCompare(b, "es")), [jobsInCall]);

  const filteredJobs = useMemo(() => {
    const normalizedQuery = normalize(query);
    const terms = normalizedQuery.split(" ").filter(Boolean);
    const salary = minimumSalary ? Number(minimumSalary) : 0;
    const base = jobs.filter((job) => {
      if (convocatoria && job.convocatoriaId !== convocatoria) return false;
      if (searchMode === "smart") return true;
      if (modality && job.modalidad !== modality) return false;
      if (department && !splitValues(job.departamento).includes(department)) return false;
      if (municipality && !splitValues(job.municipio).includes(municipality)) return false;
      if (level && job.nivel !== level) return false;
      if (education && job.nivelEstudio !== education) return false;
      if (additionalRequirement === "none" && job.requisitosAdicionales.length) return false;
      if (additionalRequirement && additionalRequirement !== "none" && !job.requisitosAdicionales.includes(additionalRequirement as never)) return false;
      if (salary && job.salario < salary) return false;
      if (disability && !job.discapacidad) return false;
      if (experience === "0" && job.experienciaMeses !== 0) return false;
      if (["6", "12", "24", "36"].includes(experience)) {
        const maximum = Number(experience);
        if (job.experienciaMeses === null || job.experienciaMeses > maximum) return false;
      }
      if (experience === "37+" && (job.experienciaMeses === null || job.experienciaMeses <= 36)) return false;
      return matchesSearch(job, normalizedQuery);
    });

    const ranked = searchMode === "smart"
      ? base.map((job) => ({ job, match: scoreProfile(job, query) })).filter((item): item is { job: OpecSummary; match: SmartMatch } => item.match !== null)
      : base.map((job) => ({ job, match: undefined }));

    return ranked.sort((a, b) => {
      if (searchMode === "smart") return (b.match?.score ?? 0) - (a.match?.score ?? 0) || b.job.vacantes - a.job.vacantes;
      if (sort === "salary-desc") return b.job.salario - a.job.salario;
      if (sort === "salary-asc") return a.job.salario - b.job.salario;
      if (sort === "vacancies") return b.job.vacantes - a.job.vacantes || b.job.salario - a.job.salario;
      if (sort === "experience") return (a.job.experienciaMeses ?? 999) - (b.job.experienciaMeses ?? 999) || b.job.salario - a.job.salario;
      if (terms.length) {
        const score = (item: OpecSummary) => String(item.referencia) === normalizedQuery ? 100 : normalize(item.denominacion).includes(normalizedQuery) ? 30 : 0;
        const difference = score(b.job) - score(a.job);
        if (difference) return difference;
      }
      return b.job.vacantes - a.job.vacantes || b.job.salario - a.job.salario;
    });
  }, [jobs, searchMode, query, convocatoria, modality, department, municipality, level, education, experience, additionalRequirement, minimumSalary, disability, sort]);

  const activeFilters = [convocatoria, department, municipality, level, education, experience, additionalRequirement, minimumSalary, disability ? "disability" : ""].filter(Boolean).length;
  function resetFilters() {
    setConvocatoria(""); setDepartment(""); setMunicipality(""); setLevel(""); setEducation("");
    setExperience(""); setAdditionalRequirement(""); setMinimumSalary(""); setDisability(false);
  }
  function changeMode(mode: "smart" | "filters") {
    setSearchMode(mode); setQuery(""); setFiltersOpen(false); setSort("relevance");
  }
  async function copyReference(job: OpecSummary) {
    try {
      await navigator.clipboard.writeText(job.referencia);
      setCopiedId(job.id);
      window.setTimeout(() => setCopiedId((current) => current === job.id ? null : current), 1800);
    } catch { setCopiedId(null); }
  }
  async function openDetail(job: OpecSummary) {
    detailRequest.current?.controller.abort();
    detailRequest.current = null;
    setSelected(job); setDetailError("");
    const cached = detailCache.current.get(job.id);
    if (cached) { setDetail(cached); setDetailLoading(false); return; }
    const controller = new AbortController();
    detailRequest.current = { id: job.id, controller };
    setDetail(null); setDetailLoading(true);
    try {
      const response = await fetch(getOpecDetailUrl(job.id), { signal: controller.signal });
      if (!response.ok) throw new Error("No pudimos cargar el detalle. Intenta nuevamente.");
      const shard = await response.json() as OpecDetailShard;
      const selectedDetail = shard.empleos[job.id];
      if (!selectedDetail) throw new Error("No encontramos el detalle de esta vacante.");
      detailCache.current.set(job.id, selectedDetail);
      if (detailRequest.current?.id === job.id) setDetail(selectedDetail);
    } catch (error) {
      if (error instanceof Error && error.name === "AbortError") return;
      if (detailRequest.current?.id === job.id) setDetailError(error instanceof Error ? error.message : "Ocurrió un error inesperado.");
    } finally {
      if (detailRequest.current?.id === job.id) { detailRequest.current = null; setDetailLoading(false); }
    }
  }

  const smartReady = searchMode === "filters" || profileTerms(query).length > 0 || /^\s*[\d-]+\s*$/.test(query);
  return <>
    <div className="opec-mode-switch" role="tablist" aria-label="Tipo de búsqueda">
      <button type="button" role="tab" aria-selected={searchMode === "smart"} className={searchMode === "smart" ? "active" : ""} onClick={() => changeMode("smart")}><span aria-hidden="true">✦</span><strong>Búsqueda inteligente</strong><small>Describe tu formación y experiencia</small></button>
      <button type="button" role="tab" aria-selected={searchMode === "filters"} className={searchMode === "filters" ? "active" : ""} onClick={() => changeMode("filters")}><span aria-hidden="true">☷</span><strong>Búsqueda con filtros</strong><small>Elige convocatoria y criterios</small></button>
    </div>

    <div className={`opec-search-shell${searchMode === "smart" ? " smart" : ""}`}>
      {searchMode === "smart" ? <>
        <label htmlFor="opec-profile" className="opec-smart-label"><span>Cuéntanos tu perfil</span><small>Puedes escribir una frase o pegar una descripción completa.</small></label>
        <div className="opec-smart-box">
          <SearchIcon />
          <textarea id="opec-profile" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Ejemplo: Soy administradora de empresas, tengo 4 años de experiencia en talento humano, nómina y contratación…" rows={4} />
          {query && <button type="button" onClick={() => setQuery("")} aria-label="Borrar perfil"><CloseIcon /></button>}
        </div>
        <div className="opec-smart-foot">
          <label><span>Buscar en</span><select value={convocatoria} onChange={(event) => setConvocatoria(event.target.value)}><option value="">Todas las convocatorias</option>{convocatorias.map((item) => <option key={item.id} value={item.id}>{item.nombre}</option>)}</select></label>
          <p><span aria-hidden="true">i</span> La afinidad es orientativa. Siempre verifica los requisitos completos.</p>
        </div>
      </> : <>
        <div className="opec-search-main">
          <div className="opec-search-box"><SearchIcon /><label htmlFor="opec-query" className="sr-only">Buscar por OPEC, código, cargo, profesión, entidad o ciudad</label><input id="opec-query" type="search" value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Busca por OPEC, código, cargo, profesión, entidad o ciudad…" autoComplete="off" />{query && <button type="button" onClick={() => setQuery("")} aria-label="Borrar búsqueda"><CloseIcon /></button>}</div>
          <button type="button" className="opec-mobile-filter" onClick={() => setFiltersOpen(!filtersOpen)} aria-expanded={filtersOpen} aria-controls="opec-filter-panel"><span aria-hidden="true">☷</span> Filtros {activeFilters > 0 && <b>{activeFilters}</b>}</button>
        </div>
        <div className="opec-quick-row">
          <span>Tipo de concurso:</span>
          <div className="opec-segmented" role="group" aria-label="Tipo de concurso">
            <button type="button" aria-pressed={modality === "Abierto"} className={modality === "Abierto" ? "active" : ""} onClick={() => setModality("Abierto")}>Abierto</button>
            <button type="button" aria-pressed={modality === "Ascenso"} className={modality === "Ascenso" ? "active" : ""} onClick={() => setModality("Ascenso")}>Ascenso</button>
            <button type="button" aria-pressed={modality === ""} className={modality === "" ? "active" : ""} onClick={() => setModality("")}>Todos</button>
          </div>
          <button type="button" aria-pressed={experience === "0"} className={`opec-no-experience${experience === "0" ? " active" : ""}`} onClick={() => setExperience(experience === "0" ? "" : "0")}><span aria-hidden="true">✓</span> Sin experiencia</button>
          <button type="button" aria-pressed={education === "bachiller-solo"} className={`opec-quick-study${education === "bachiller-solo" ? " active" : ""}`} onClick={() => setEducation(education === "bachiller-solo" ? "" : "bachiller-solo")}><span aria-hidden="true">🎓</span> Solo bachiller</button>
        </div>
      </>}
    </div>

    <div className={`opec-layout${searchMode === "smart" ? " smart-mode" : ""}`}>
      {searchMode === "filters" && <aside ref={filtersRef} id="opec-filter-panel" className={`opec-filters${filtersOpen ? " mobile-open" : ""}`} aria-label="Filtros de vacantes" role={filtersOpen ? "dialog" : "complementary"} aria-modal={filtersOpen ? true : undefined} aria-labelledby="opec-filters-title" tabIndex={filtersOpen ? -1 : undefined}>
        <button ref={filterCloseRef} type="button" className="opec-filter-close" onClick={closeFilters} aria-label="Cerrar filtros">×</button>
        <Filters convocatorias={convocatorias} departments={departments} municipalities={municipalities} levels={levels} convocatoria={convocatoria} department={department} municipality={municipality} level={level} education={education} experience={experience} additionalRequirement={additionalRequirement} minimumSalary={minimumSalary} disability={disability} onConvocatoria={(value) => { setConvocatoria(value); setDepartment(""); setMunicipality(""); }} onDepartment={(value) => { setDepartment(value); setMunicipality(""); }} onMunicipality={setMunicipality} onLevel={setLevel} onEducation={setEducation} onExperience={setExperience} onAdditionalRequirement={setAdditionalRequirement} onMinimumSalary={setMinimumSalary} onDisability={setDisability} onReset={resetFilters} />
        <button type="button" className="opec-apply-mobile" onClick={closeFilters}>Ver {filteredJobs.length.toLocaleString("es-CO")} resultados</button>
      </aside>}

      <section className="opec-results" aria-live="polite" aria-busy={loading}>
        <div className="opec-results-head">
          <div><span className="opec-result-count">{loading ? "Consultando vacantes…" : !smartReady ? "Describe tu perfil para comenzar" : `${filteredJobs.length.toLocaleString("es-CO")} ${filteredJobs.length === 1 ? "oportunidad encontrada" : "oportunidades encontradas"}`}</span>{!loading && payload && <small>{searchMode === "smart" ? "Ordenadas por afinidad con tu perfil" : `Datos actualizados al ${formatOpecDate(payload.meta.fechaActualizacion)}`}</small>}</div>
          {searchMode === "filters" && <label className="opec-sort"><span>Ordenar por</span><select value={sort} onChange={(event) => setSort(event.target.value)}><option value="relevance">Más relevantes</option><option value="vacancies">Más vacantes</option><option value="experience">Menor experiencia</option><option value="salary-desc">Mayor salario</option><option value="salary-asc">Menor salario</option></select></label>}
        </div>
        {loading && <div className="opec-loading-grid" role="status">{[1, 2, 3, 4].map((item) => <div className="opec-card-skeleton" key={item}><i /><i /><i /><i /></div>)}<span className="sr-only">Cargando vacantes</span></div>}
        {loadError && <div className="opec-empty"><EmptyIcon /><h3>No pudimos cargar las vacantes</h3><p>{loadError}</p><button type="button" onClick={() => window.location.reload()}>Intentar nuevamente</button></div>}
        {!loading && !loadError && !smartReady && <div className="opec-smart-empty"><span aria-hidden="true">✦</span><h3>Escribe tu perfil en tus propias palabras</h3><p>Incluye tu formación, experiencia, áreas de conocimiento y el tipo de trabajo que has realizado.</p><div><button type="button" onClick={() => setQuery("Soy profesional en derecho con 3 años de experiencia jurídica y en contratación")}>Perfil jurídico</button><button type="button" onClick={() => setQuery("Soy bachiller con experiencia en archivo, atención al ciudadano y herramientas de oficina")}>Perfil administrativo</button><button type="button" onClick={() => setQuery("Soy ingeniero de sistemas con experiencia en desarrollo de software, bases de datos y soporte")}>Perfil de sistemas</button></div></div>}
        {!loading && !loadError && smartReady && filteredJobs.length === 0 && <div className="opec-empty"><EmptyIcon /><h3>No encontramos coincidencias</h3><p>Prueba con otra descripción o selecciona todas las convocatorias para ampliar los resultados.</p><button type="button" onClick={() => { setQuery(""); resetFilters(); setModality(""); }}>Limpiar búsqueda</button></div>}
        {!loading && smartReady && filteredJobs.length > 0 && <><div className="opec-grid">{filteredJobs.slice(0, visibleCount).map(({ job, match }) => <JobCard key={job.id} job={job} match={match} onOpen={openDetail} onCopy={copyReference} copied={copiedId === job.id} />)}</div>{visibleCount < filteredJobs.length && <div className="opec-load-more"><button type="button" onClick={() => setVisibleCount((count) => count + PAGE_SIZE)}>Ver más oportunidades</button><span>Mostrando {Math.min(visibleCount, filteredJobs.length)} de {filteredJobs.length.toLocaleString("es-CO")}</span></div>}</>}
      </section>
    </div>

    {selected && <DetailModal job={selected} detail={detail} loading={detailLoading} error={detailError} copied={copiedId === selected.id} onClose={closeDetail} onCopy={copyReference} />}
  </>;
}

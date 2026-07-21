import type { OpecSummary } from "./opec";

const PROFILE_STOP_WORDS = new Set([
  "actualmente", "ademas", "ano", "anos", "busco", "como", "con", "cuento", "cual",
  "de", "del", "desde", "donde", "durante", "el", "ella", "empleo", "en", "entre",
  "esta", "este", "estos", "experiencia", "formacion", "he", "la", "las", "los", "me",
  "mes", "meses", "mi", "mis", "para", "perfil", "por", "profesional", "que", "quiero",
  "sin", "soy", "tengo", "trabajado", "trabaje", "trabajar", "trabajo", "un", "una", "unos",
  "vacante", "vacantes", "y",
]);

const STRUCTURED_TERMS = new Set([
  "abierto", "ascenso", "bachiller", "bachillerato", "discapacidad", "doctorado", "especialista",
  "especializacion", "maestria", "posgrado", "primaria", "profesional", "secundaria", "tecnica",
  "tecnico", "tecnologa", "tecnologia", "tecnologo", "universitaria", "universitario",
  "procuraduria", "ereon", "ese",
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
  ["salud", "hospital", "asistencial"],
  ["saneamiento", "salubridad", "sanitario", "sanitaria", "higiene"],
  ["ambiental", "ambiente", "medioambiente", "ecologia", "ecologico", "ecologica"],
  ["contratacion", "contratos", "contractual"],
  ["planeacion", "planificacion", "proyectos"],
  ["auditoria", "control", "riesgos"],
  ["comunicador", "comunicadora", "comunicacion", "periodismo"],
  ["trabajador", "trabajadora", "social", "sociologia"],
  ["tecnico", "tecnica", "tecnologo", "tecnologa"],
  ["bachiller", "bachillerato", "secundaria"],
  ["conductor", "conductora", "conduccion", "licencia"],
  ["laboratorio", "laboratorista", "muestras"],
  ["alimentos", "alimentaria", "nutricion", "nutricionista"],
];

const NUMBER_WORDS: Record<string, number> = {
  un: 1, uno: 1, una: 1, dos: 2, tres: 3, cuatro: 4, cinco: 5, seis: 6,
  siete: 7, ocho: 8, nueve: 9, diez: 10, once: 11, doce: 12, trece: 13,
  catorce: 14, quince: 15, dieciseis: 16, diecisiete: 17, dieciocho: 18,
  diecinueve: 19, veinte: 20,
};

export interface SmartLocation {
  label: string;
  normalized: string;
  type: "municipio" | "departamento";
}

export interface SmartProfile {
  original: string;
  normalized: string;
  exactReference: string | null;
  locations: SmartLocation[];
  roleTerms: string[];
  educationTerms: string[];
  educationRank: number | null;
  educationLabel: string | null;
  experienceMonths: number | null;
  minimumSalary: number | null;
  convocatoriaIds: string[];
  modality: "Abierto" | "Ascenso" | null;
  disabilityOnly: boolean;
  criteria: string[];
  ready: boolean;
}

export interface SmartMatch {
  score: number;
  compatibility: number;
  reasons: string[];
  matchedTerms: string[];
}

export function normalizeSearch(value: string): string {
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

function aliasesFor(term: string): string[] {
  const group = SYNONYM_GROUPS.find((items) => items.includes(term));
  return group ?? [term];
}

function canonicalTerm(term: string): string {
  return aliasesFor(term)[0];
}

function tokenMatches(text: string, alias: string): boolean {
  const tokens = text.split(" ");
  return tokens.includes(alias) || (alias.length >= 5 && tokens.some((token) => token.startsWith(alias)));
}

function textMatchesTerm(text: string, term: string): boolean {
  return aliasesFor(term).some((alias) => tokenMatches(text, alias));
}

function uniqueLocations(jobs: OpecSummary[]): SmartLocation[] {
  const locations = new Map<string, SmartLocation>();
  for (const job of jobs) {
    for (const [type, value] of [["municipio", job.municipio], ["departamento", job.departamento]] as const) {
      for (const label of splitValues(value)) {
        if (label === "No especificado" || label === "No aplica") continue;
        const normalized = normalizeSearch(label);
        const key = `${type}:${normalized}`;
        if (normalized && !locations.has(key)) locations.set(key, { label, normalized, type });
      }
    }
  }
  return Array.from(locations.values()).sort((a, b) => b.normalized.length - a.normalized.length);
}

function containsExplicitLocation(originalQuery: string, normalizedQuery: string, location: SmartLocation): boolean {
  const aliases = [location.normalized];
  const withoutDistrictSuffix = location.normalized.replace(/ d c$/, "");
  if (withoutDistrictSuffix !== location.normalized) aliases.push(withoutDistrictSuffix);

  return aliases.some((locationAlias) => {
    const escaped = locationAlias.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const direct = new RegExp(`(?:^| )(?:en|ubicacion|ciudad|municipio|departamento|resido|vivo|radicado|radicada|prefiero|cerca)(?: (?:la|el|de|del|ciudad|municipio|departamento|trabajar|empleo)){0,4} ${escaped}(?: |$)`);
    const workIntent = new RegExp(`(?:trabajar|empleo|vacante|cargo|oportunidad|quiero)(?: [a-z0-9]+){0,5} (?:en )?${escaped}(?: |$)`);
    const endsWithLocation = normalizedQuery.endsWith(locationAlias)
      && /\b(?:busco|quiero|empleo|trabajar|trabajo|vacante|ubicacion|resido|vivo)\b/.test(normalizedQuery);
    if (normalizedQuery === locationAlias || direct.test(` ${normalizedQuery} `) || workIntent.test(` ${normalizedQuery} `) || endsWithLocation) return true;

    const originalLocation = location.label.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const listMatch = new RegExp(`[,;]\\s*(?:en\\s+)?${originalLocation}(?:\\s*[,;.]|\\s*$)`, "i");
    return listMatch.test(originalQuery);
  });
}

function parseExperience(normalizedQuery: string): number | null {
  if (/\bsin experiencia\b/.test(normalizedQuery)) return 0;
  const amountPattern = `(\\d+|${Object.keys(NUMBER_WORDS).join("|")})`;
  const matches = Array.from(normalizedQuery.matchAll(new RegExp(`${amountPattern}\\s*(anos?|mes(?:es)?)\\b`, "g")));
  if (!matches.length) return null;
  return Math.max(...matches.map((match) => {
    const amount = /^\d+$/.test(match[1]) ? Number(match[1]) : NUMBER_WORDS[match[1]];
    return amount * (match[2].startsWith("ano") ? 12 : 1);
  }));
}

function parseEducation(normalizedQuery: string): { rank: number | null; label: string | null } {
  if (/doctorado|maestria|especializacion|especialista|posgrado/.test(normalizedQuery)) return { rank: 9, label: "Profesional con posgrado" };
  if (/abogad|administrador|contador|ingenier|medic|enfermer|psicolog|economista|arquitect|universitari|profesion/.test(normalizedQuery)) return { rank: 8, label: "Formación profesional" };
  if (/tecnolog/.test(normalizedQuery)) return { rank: 6, label: "Formación tecnológica" };
  if (/tecnic/.test(normalizedQuery)) return { rank: 6, label: "Formación técnica" };
  if (/bachiller|secundaria/.test(normalizedQuery)) return { rank: 3, label: "Bachiller" };
  if (/primaria/.test(normalizedQuery)) return { rank: 1, label: "Primaria" };
  return { rank: null, label: null };
}

function parseEducationSpecialty(normalizedQuery: string, locations: SmartLocation[]): string[] {
  let profileText = normalizedQuery;
  for (const location of locations) {
    const aliases = [location.normalized, location.normalized.replace(/ d c$/, "")];
    for (const alias of aliases) profileText = profileText.replace(new RegExp(`\\b${alias}\\b`, "g"), " ");
  }
  const match = profileText.match(/\b(?:soy |titulo de |formacion )?(?:tecnico|tecnica|tecnologo|tecnologa|ingeniero|ingeniera|profesional|especialista)\s+(?:en|de)\s+(.+?)(?=\s+(?:con|cuento|tengo|experiencia|busco|quiero|trabaj|empleo|salario|sueldo)\b|$)/);
  if (!match) return [];
  return Array.from(new Set(
    match[1].split(" ")
      .filter((term) => term.length >= 3 && !PROFILE_STOP_WORDS.has(term) && !STRUCTURED_TERMS.has(term))
      .map(canonicalTerm),
  ));
}

function parseMinimumSalary(normalizedQuery: string): number | null {
  const millions = normalizedQuery.match(/(?:salario|sueldo|aspiracion|minimo|desde|superior)(?: [a-z]+){0,3} (\d+(?:[.,]\d+)?)\s*millones?/);
  if (millions) return Math.round(Number(millions[1].replace(",", ".")) * 1_000_000);
  const amount = normalizedQuery.match(/(?:salario|sueldo|aspiracion|minimo|desde|superior)(?: [a-z]+){0,3} (\d{6,8})\b/);
  return amount ? Number(amount[1]) : null;
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

function formatExperience(months: number): string {
  if (months === 0) return "Sin experiencia previa";
  if (months % 12 === 0) return `${months / 12} ${months === 12 ? "año" : "años"} de experiencia`;
  return `${months} meses de experiencia`;
}

function formatSalary(value: number): string {
  return `$${new Intl.NumberFormat("es-CO").format(value)} o más`;
}

export function interpretSmartProfile(query: string, jobs: OpecSummary[]): SmartProfile {
  const normalized = normalizeSearch(query);
  const matchedLocations = uniqueLocations(jobs).filter((location) => containsExplicitLocation(query, normalized, location));
  const locations = Array.from(
    new Map(matchedLocations.map((location) => [location.normalized, location])).values(),
  );
  const locationTokens = new Set(locations.flatMap((location) => location.normalized.split(" ")));
  const education = parseEducation(normalized);
  const educationTerms = parseEducationSpecialty(normalized, locations);
  const experienceMonths = parseExperience(normalized);
  const minimumSalary = parseMinimumSalary(normalized);
  const exactReference = /^[0-9]{2,6}(?:-20\d{2})?$/.test(normalized.replace(/ /g, ""))
    ? normalized.replace(/ /g, "")
    : null;
  const convocatoriaIds = [
    ...(normalized.includes("procuraduria") ? ["procuraduria-2026"] : []),
    ...(normalized.includes("ereon") || normalized.includes("orden nacional") ? ["ereon-2026"] : []),
    ...(normalized.includes("ese 2") || normalized.includes("empresas sociales") ? ["ese-2026"] : []),
  ];
  const modality = /\bascenso\b/.test(normalized)
    ? "Ascenso"
    : /\babiert[oa]s?\b/.test(normalized) ? "Abierto" : null;
  const disabilityOnly = /discapacidad|reserva especial/.test(normalized);

  const roleTerms = Array.from(new Set(
    normalized.split(" ").filter((term) =>
      term.length >= 3
      && !PROFILE_STOP_WORDS.has(term)
      && !STRUCTURED_TERMS.has(term)
      && !locationTokens.has(term)
      && !/^\d+$/.test(term)
      && !Object.prototype.hasOwnProperty.call(NUMBER_WORDS, term),
    ).map(canonicalTerm),
  ));

  const criteria: string[] = [];
  if (locations.length) criteria.push(`Ubicación exacta: ${locations.map((item) => item.label).join(" o ")}`);
  if (roleTerms.length) criteria.push(`Perfil y áreas: ${roleTerms.slice(0, 7).join(", ")}`);
  if (education.label) criteria.push(`Estudios: ${education.label}${educationTerms.length ? ` en ${educationTerms.join(", ")}` : ""}`);
  if (experienceMonths !== null) criteria.push(`Experiencia disponible: ${formatExperience(experienceMonths)}`);
  if (minimumSalary !== null) criteria.push(`Salario: ${formatSalary(minimumSalary)}`);
  if (convocatoriaIds.length) {
    const labels: Record<string, string> = { "ese-2026": "ESE 2", "ereon-2026": "EREON 2026", "procuraduria-2026": "Procuraduría" };
    criteria.push(`Convocatoria: ${convocatoriaIds.map((id) => labels[id]).join(" o ")}`);
  }
  if (modality) criteria.push(`Modalidad: ${modality}`);
  if (disabilityOnly) criteria.push("Reserva para discapacidad");
  if (exactReference) criteria.push(`Referencia exacta: ${exactReference}`);

  return {
    original: query,
    normalized,
    exactReference,
    locations,
    roleTerms,
    educationTerms,
    educationRank: education.rank,
    educationLabel: education.label,
    experienceMonths,
    minimumSalary,
    convocatoriaIds,
    modality,
    disabilityOnly,
    criteria,
    ready: Boolean(exactReference || locations.length || roleTerms.length || education.rank !== null || experienceMonths !== null || minimumSalary !== null || convocatoriaIds.length || modality || disabilityOnly),
  };
}

function matchesRequestedLocation(job: OpecSummary, locations: SmartLocation[]): boolean {
  if (!locations.length) return true;
  const jobLocations = [
    ...splitValues(job.municipio).map(normalizeSearch),
    ...splitValues(job.departamento).map(normalizeSearch),
  ];
  return locations.some((location) => jobLocations.includes(location.normalized));
}

export function scoreSmartProfile(job: OpecSummary, profile: SmartProfile): SmartMatch | null {
  if (!profile.ready) return null;
  if (profile.exactReference) {
    return normalizeSearch(job.referencia) === profile.exactReference
      ? { score: 1000, compatibility: 100, reasons: [`${job.tipoReferencia} exacta`], matchedTerms: [] }
      : null;
  }

  // Los criterios explícitos se respetan como condiciones, no solo como puntos de ranking.
  if (!matchesRequestedLocation(job, profile.locations)) return null;
  if (profile.convocatoriaIds.length && !profile.convocatoriaIds.includes(job.convocatoriaId)) return null;
  if (profile.modality && job.modalidad !== profile.modality) return null;
  if (profile.disabilityOnly && !job.discapacidad) return null;
  if (profile.minimumSalary !== null && job.salario < profile.minimumSalary) return null;
  if (profile.educationRank !== null && educationRankFromJob(job) > profile.educationRank) return null;
  if (profile.educationTerms.length && !profile.educationTerms.every((term) => textMatchesTerm(job.perfilFormacion, term))) return null;
  if (profile.experienceMonths !== null && (job.experienciaMeses === null || job.experienciaMeses > profile.experienceMonths)) return null;

  const denomination = normalizeSearch(job.denominacion);
  const education = job.perfilFormacion;
  const functions = job.perfilFunciones;
  const matchedTerms: string[] = [];
  let denominationMatches = 0;
  let educationMatches = 0;
  let functionMatches = 0;
  let score = 0;

  for (const term of profile.roleTerms) {
    const inDenomination = textMatchesTerm(denomination, term);
    const inEducation = textMatchesTerm(education, term);
    const inFunctions = textMatchesTerm(functions, term);
    const inGeneral = textMatchesTerm(job.busqueda, term);
    const best = inDenomination ? 18 : inEducation ? 15 : inFunctions ? 10 : inGeneral ? 5 : 0;
    if (!best) continue;
    matchedTerms.push(term);
    score += best;
    if (inDenomination) denominationMatches += 1;
    if (inEducation) educationMatches += 1;
    if (inFunctions) functionMatches += 1;
  }

  if (profile.roleTerms.length) {
    const minimumMatches = profile.roleTerms.length <= 2
      ? profile.roleTerms.length
      : Math.max(2, Math.ceil(profile.roleTerms.length * 0.55));
    if (matchedTerms.length < minimumMatches) return null;
    // Evita que menciones casuales en funciones conviertan un cargo de otra área en una coincidencia principal.
    if (!denominationMatches && !educationMatches) return null;
  }

  const coverage = profile.roleTerms.length ? matchedTerms.length / profile.roleTerms.length : 1;
  score += coverage * 35;
  const reasons: string[] = [];
  if (profile.locations.length) {
    score += 35;
    reasons.push(`Ubicación: ${profile.locations.map((item) => item.label).join(" o ")}`);
  }
  if (denominationMatches) reasons.push("Cargo relacionado");
  if (educationMatches) reasons.push("Formación específica relacionada");
  if (functionMatches) reasons.push("Experiencia y funciones afines");
  if (profile.educationRank !== null) {
    score += 12;
    reasons.push("Nivel de estudios compatible");
  }
  if (profile.experienceMonths !== null) {
    score += 14;
    reasons.push("Experiencia suficiente");
  }
  if (profile.minimumSalary !== null) score += 8;
  if (profile.convocatoriaIds.length) score += 8;

  if (score <= 0) return null;
  const compatibility = Math.max(45, Math.min(99, Math.round(45 + coverage * 34 + Math.min(score, 55) * 0.35)));
  return { score, compatibility, reasons: Array.from(new Set(reasons)).slice(0, 4), matchedTerms };
}

export function matchesLexicalSearch(job: OpecSummary, normalizedQuery: string): boolean {
  const terms = normalizedQuery.split(" ").filter(Boolean);
  if (!terms.length) return true;
  return terms.every((term) => {
    if (/^\d+$/.test(term)) return normalizeSearch(job.referencia).startsWith(term);
    if (tokenMatches(job.busqueda, term)) return true;
    return aliasesFor(term).some((alias) => tokenMatches(job.busqueda, alias));
  });
}

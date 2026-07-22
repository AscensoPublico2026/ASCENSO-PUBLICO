export const ANALYTICS_EVENT_NAMES = [
  "page_view",
  "cta_click",
  "whatsapp_clicked",
  "search_mode_changed",
  "search_used",
  "search_zero_results",
  "opec_detail_viewed",
  "opec_reference_copied",
  "opec_official_clicked",
  "simulacro_started",
  "simulacro_progress",
  "simulacro_submitted",
  "simulacro_completed",
  "simulacro_restarted",
  "checkout_form_submitted",
  "checkout_started",
  "purchase_completed",
] as const;

export type AnalyticsEventName = (typeof ANALYTICS_EVENT_NAMES)[number];
export type AnalyticsPrimitive = string | number | boolean | null;
export type AnalyticsProperties = Record<string, AnalyticsPrimitive>;

const PROPERTY_ALLOWLIST = new Set([
  "path",
  "page_title",
  "source",
  "placement",
  "destination",
  "level",
  "mode",
  "criteria_count",
  "has_location",
  "query_length_bucket",
  "result_count",
  "convocatoria_id",
  "employment_level",
  "empleo_id",
  "referencia",
  "answered",
  "total",
  "percentage",
  "milestone",
  "value",
  "currency",
]);

export function isAnalyticsEventName(value: unknown): value is AnalyticsEventName {
  return typeof value === "string" && (ANALYTICS_EVENT_NAMES as readonly string[]).includes(value);
}

export function sanitizeAnalyticsProperties(value: unknown): AnalyticsProperties {
  if (!value || typeof value !== "object" || Array.isArray(value)) return {};

  const clean: AnalyticsProperties = {};
  for (const [key, raw] of Object.entries(value).slice(0, 24)) {
    if (!PROPERTY_ALLOWLIST.has(key)) continue;
    if (typeof raw === "string") clean[key] = raw.slice(0, 120);
    else if (typeof raw === "number" && Number.isFinite(raw)) clean[key] = raw;
    else if (typeof raw === "boolean" || raw === null) clean[key] = raw;
  }
  return clean;
}

function getSessionId(): string | null {
  if (typeof window === "undefined") return null;
  const key = "ascenso_analytics_session";
  try {
    const current = window.sessionStorage.getItem(key);
    if (current) return current;
    const created = window.crypto.randomUUID();
    window.sessionStorage.setItem(key, created);
    return created;
  } catch {
    return null;
  }
}

function safePath(): string {
  if (typeof window === "undefined") return "/";
  return window.location.pathname.slice(0, 200);
}

export function trackEvent(name: AnalyticsEventName, properties: AnalyticsProperties = {}): void {
  if (typeof window === "undefined") return;
  let consent: string | null = null;
  try {
    consent = window.localStorage.getItem("ascenso_analytics_consent_v1");
  } catch {
    return;
  }
  if (consent !== "accepted" && consent !== "anonymous") return;

  const cleanProperties = sanitizeAnalyticsProperties({
    ...properties,
    path: properties.path || safePath(),
  });
  const sessionId = getSessionId();

  if (typeof window.gtag === "function") {
    window.gtag("event", name, cleanProperties);
  }

  void fetch("/api/analytics/events", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      event_name: name,
      anonymous_session_id: sessionId,
      properties: cleanProperties,
    }),
    keepalive: true,
    credentials: "same-origin",
  }).catch(() => undefined);
}

declare global {
  interface Window {
    dataLayer?: unknown[];
    gtag?: (...args: unknown[]) => void;
    clarity?: (...args: unknown[]) => void;
  }
}

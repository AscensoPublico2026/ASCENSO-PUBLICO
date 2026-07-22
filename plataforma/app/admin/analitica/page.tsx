import Link from "next/link";
import { createClient } from "@/lib/supabase/server";

export const dynamic = "force-dynamic";

type EventRow = {
  event_name: string;
  anonymous_session_id: string | null;
  properties: Record<string, unknown> | null;
  occurred_at: string;
};

const EVENT_LABELS: Record<string, string> = {
  page_view: "Visitas de página",
  cta_click: "Clics en llamados a la acción",
  whatsapp_clicked: "Clics en WhatsApp",
  search_used: "Búsquedas realizadas",
  search_zero_results: "Búsquedas sin resultados",
  opec_detail_viewed: "Detalles de vacante consultados",
  simulacro_started: "Simulacros iniciados",
  simulacro_completed: "Simulacros terminados",
  checkout_started: "Checkouts iniciados",
  purchase_completed: "Compras aprobadas",
};

function number(value: number): string {
  return value.toLocaleString("es-CO");
}

function percentage(numerator: number, denominator: number): string {
  if (!denominator) return "0%";
  return `${Math.round((numerator / denominator) * 100)}%`;
}

function property(event: EventRow, key: string): string {
  const value = event.properties?.[key];
  return typeof value === "string" || typeof value === "number" ? String(value) : "";
}

function uniqueSessions(events: EventRow[], eventName?: string): number {
  return new Set(
    events
      .filter((event) => !eventName || event.event_name === eventName)
      .map((event) => event.anonymous_session_id)
      .filter((session): session is string => Boolean(session)),
  ).size;
}

function countBy(events: EventRow[], key: string): { label: string; count: number }[] {
  const counts = new Map<string, number>();
  for (const event of events) {
    const label = property(event, key) || "No especificado";
    counts.set(label, (counts.get(label) || 0) + 1);
  }
  return [...counts.entries()]
    .map(([label, count]) => ({ label, count }))
    .sort((a, b) => b.count - a.count);
}

export default async function AnaliticaPage({ searchParams }: { searchParams?: { days?: string } }) {
  const requestedDays = Number(searchParams?.days || 30);
  const days = [7, 30, 90].includes(requestedDays) ? requestedDays : 30;
  const since = new Date(Date.now() - days * 86_400_000).toISOString();
  const supabase = createClient();

  const leadsResponse = await supabase
    .from("leads_simulacro")
    .select("*", { count: "exact", head: true })
    .gte("created_at", since);

  const events: EventRow[] = [];
  let analyticsUnavailable = false;
  const pageSize = 1_000;
  for (let from = 0; ; from += pageSize) {
    const response = await supabase
      .from("analytics_events")
      .select("event_name,anonymous_session_id,properties,occurred_at")
      .gte("occurred_at", since)
      .order("occurred_at", { ascending: false })
      .range(from, from + pageSize - 1);
    if (response.error) {
      analyticsUnavailable = true;
      break;
    }
    const page = (response.data || []) as EventRow[];
    events.push(...page);
    if (page.length < pageSize) break;
  }

  const pageEvents = events.filter((event) => event.event_name === "page_view");
  const searchEvents = events.filter((event) => event.event_name === "search_used");
  const zeroSearchEvents = events.filter((event) => event.event_name === "search_zero_results");
  const simulacroStarts = events.filter((event) => event.event_name === "simulacro_started");
  const simulacroCompleted = events.filter((event) => event.event_name === "simulacro_completed");
  const checkoutEvents = events.filter((event) => event.event_name === "checkout_started");
  const purchaseEvents = events.filter((event) => event.event_name === "purchase_completed");
  const whatsappEvents = events.filter((event) => event.event_name === "whatsapp_clicked");

  const sessions = uniqueSessions(pageEvents);
  const searchers = uniqueSessions(searchEvents);
  const simulacroUsers = uniqueSessions(simulacroStarts);
  const completedUsers = uniqueSessions(simulacroCompleted);
  const formCheckoutUsers = uniqueSessions(events, "checkout_form_submitted");
  const purchases = purchaseEvents.length;
  const averageScore = simulacroCompleted.length
    ? Math.round(simulacroCompleted.reduce((sum, event) => sum + Number(property(event, "percentage") || 0), 0) / simulacroCompleted.length)
    : 0;

  const topPages = countBy(pageEvents, "path").slice(0, 8);
  const searchesByMode = countBy(searchEvents, "mode");
  const simulacrosByLevel = countBy(simulacroCompleted, "level");
  const recentEvents = Object.entries(
    events.reduce<Record<string, number>>((acc, event) => {
      const day = event.occurred_at.slice(0, 10);
      acc[day] = (acc[day] || 0) + 1;
      return acc;
    }, {}),
  ).sort(([a], [b]) => b.localeCompare(a)).slice(0, 10);

  const card: React.CSSProperties = {
    background: "#fff",
    border: "1px solid var(--gris-borde)",
    borderRadius: 16,
    padding: "20px",
    boxShadow: "0 4px 20px rgba(10,42,94,.05)",
  };
  const table: React.CSSProperties = {
    width: "100%",
    borderCollapse: "collapse",
    fontSize: ".86rem",
  };
  const th: React.CSSProperties = {
    textAlign: "left",
    color: "var(--texto-suave)",
    borderBottom: "1px solid var(--gris-borde)",
    padding: "10px 8px",
  };
  const td: React.CSSProperties = {
    borderBottom: "1px solid var(--gris-borde)",
    padding: "10px 8px",
  };

  return (
    <main style={{ padding: "40px 28px", maxWidth: 1180 }}>
      <div style={{ display: "flex", justifyContent: "space-between", gap: 16, alignItems: "flex-start", flexWrap: "wrap" }}>
        <div>
          <h1 style={{ fontSize: "1.7rem", marginBottom: 6 }}>Analítica e indicadores</h1>
          <p style={{ color: "var(--texto-suave)", margin: 0 }}>Actividad anónima registrada durante los últimos {days} días.</p>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          {[7, 30, 90].map((value) => (
            <Link key={value} href={`/admin/analitica?days=${value}`} style={{
              padding: "8px 12px", borderRadius: 9, fontSize: ".82rem", fontWeight: 700,
              color: value === days ? "#fff" : "var(--azul)",
              background: value === days ? "var(--azul)" : "#fff",
              border: "1px solid var(--gris-borde)",
            }}>{value} días</Link>
          ))}
        </div>
      </div>

      {analyticsUnavailable && (
        <div style={{ ...card, marginTop: 24, borderColor: "#E8A33D", background: "#FFF8E8" }}>
          <strong style={{ color: "#8A5200" }}>La tabla de analítica todavía no está disponible.</strong>
          <p style={{ margin: "6px 0 0", color: "#6A4A16", fontSize: ".88rem" }}>
            Ejecuta una vez <code>plataforma/supabase/migracion-analytics.sql</code> en el SQL Editor de Supabase. Desde ese momento comenzarán a acumularse los indicadores; no son retroactivos.
          </p>
        </div>
      )}

      <section style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(155px, 1fr))", gap: 14, marginTop: 24 }}>
        {[
          ["Sesiones con analítica", sessions, "Visitantes aproximados que autorizaron medición"],
          ["Páginas vistas", pageEvents.length, `${sessions ? (pageEvents.length / sessions).toLocaleString("es-CO", { maximumFractionDigits: 1 }) : "0"} por sesión`],
          ["Usaron el buscador", searchers, `${percentage(searchers, sessions)} de sesiones medidas`],
          ["Terminaron simulacro", completedUsers, `${percentage(completedUsers, simulacroUsers)} de sesiones que iniciaron`],
          ["Checkouts iniciados", checkoutEvents.length, "Intentos creados en el servidor"],
          ["Compras aprobadas", purchases, "Aprobaciones registradas en el período"],
        ].map(([label, value, detail]) => (
          <div key={String(label)} style={card}>
            <div style={{ color: "var(--texto-suave)", fontSize: ".78rem", fontWeight: 700 }}>{label}</div>
            <div style={{ fontSize: "2rem", color: "var(--azul)", fontWeight: 800, margin: "4px 0" }}>{number(Number(value))}</div>
            <div style={{ color: "var(--texto-suave)", fontSize: ".74rem" }}>{detail}</div>
          </div>
        ))}
      </section>

      <section style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(330px, 1fr))", gap: 18, marginTop: 20 }}>
        <div style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 6 }}>Volumen por etapa</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".76rem", margin: "0 0 12px" }}>Orientativo: las primeras etapas son sesiones anónimas; checkout y compra son intentos confirmados por el servidor. No representa una cohorte individual.</p>
          <table style={table}><thead><tr><th style={th}>Etapa</th><th style={{ ...th, textAlign: "right" }}>Sesiones o intentos</th></tr></thead><tbody>
            {[
              ["Visitaron la plataforma", sessions],
              ["Usaron el buscador", searchers],
              ["Iniciaron un simulacro", simulacroUsers],
              ["Terminaron un simulacro", completedUsers],
              ["Enviaron el formulario de compra", formCheckoutUsers],
              ["Llegaron al checkout de Wompi", checkoutEvents.length],
              ["Compra aprobada", purchases],
            ].map(([label, value]) => <tr key={String(label)}><td style={td}>{label}</td><td style={{ ...td, textAlign: "right", fontWeight: 800 }}>{number(Number(value))}</td></tr>)}
          </tbody></table>
        </div>

        <div style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Simulacros</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".86rem", marginBottom: 12 }}>
            {number(simulacroStarts.length)} inicios · {number(simulacroCompleted.length)} finalizaciones · promedio {averageScore}% · {number(leadsResponse.count ?? 0)} resultados enviados por correo.
          </p>
          <table style={table}><thead><tr><th style={th}>Nivel terminado</th><th style={{ ...th, textAlign: "right" }}>Cantidad</th></tr></thead><tbody>
            {simulacrosByLevel.length ? simulacrosByLevel.map((item) => <tr key={item.label}><td style={td}>{item.label}</td><td style={{ ...td, textAlign: "right", fontWeight: 800 }}>{number(item.count)}</td></tr>) : <tr><td style={td} colSpan={2}>Aún no hay finalizaciones registradas.</td></tr>}
          </tbody></table>
        </div>

        <div style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Buscador de empleos</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".86rem", marginBottom: 12 }}>
            {number(searchEvents.length)} búsquedas · {number(zeroSearchEvents.length)} sin resultados ({percentage(zeroSearchEvents.length, searchEvents.length)}).
          </p>
          <table style={table}><thead><tr><th style={th}>Modalidad</th><th style={{ ...th, textAlign: "right" }}>Búsquedas</th></tr></thead><tbody>
            {searchesByMode.length ? searchesByMode.map((item) => <tr key={item.label}><td style={td}>{item.label === "smart" ? "Inteligente" : item.label === "filters" ? "Filtros" : item.label}</td><td style={{ ...td, textAlign: "right", fontWeight: 800 }}>{number(item.count)}</td></tr>) : <tr><td style={td} colSpan={2}>Aún no hay búsquedas registradas.</td></tr>}
          </tbody></table>
        </div>

        <div style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Páginas más vistas</h2>
          <table style={table}><thead><tr><th style={th}>Ruta</th><th style={{ ...th, textAlign: "right" }}>Vistas</th></tr></thead><tbody>
            {topPages.length ? topPages.map((item) => <tr key={item.label}><td style={td}><code>{item.label}</code></td><td style={{ ...td, textAlign: "right", fontWeight: 800 }}>{number(item.count)}</td></tr>) : <tr><td style={td} colSpan={2}>Aún no hay páginas registradas.</td></tr>}
          </tbody></table>
        </div>

        <div style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Actividad reciente</h2>
          <table style={table}><thead><tr><th style={th}>Fecha</th><th style={{ ...th, textAlign: "right" }}>Eventos</th></tr></thead><tbody>
            {recentEvents.length ? recentEvents.map(([date, count]) => <tr key={date}><td style={td}>{date}</td><td style={{ ...td, textAlign: "right", fontWeight: 800 }}>{number(count)}</td></tr>) : <tr><td style={td} colSpan={2}>Aún no hay actividad registrada.</td></tr>}
          </tbody></table>
        </div>

        <div style={card}>
          <h2 style={{ fontSize: "1.05rem", marginBottom: 12 }}>Otros eventos</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".86rem", marginBottom: 12 }}>{number(whatsappEvents.length)} clics en WhatsApp.</p>
          <table style={table}><tbody>
            {Object.entries(EVENT_LABELS).map(([name, label]) => {
              const count = events.filter((event) => event.event_name === name).length;
              return <tr key={name}><td style={td}>{label}</td><td style={{ ...td, textAlign: "right", fontWeight: 800 }}>{number(count)}</td></tr>;
            })}
          </tbody></table>
        </div>
      </section>

      <section style={{ ...card, marginTop: 20 }}>
        <h2 style={{ fontSize: "1.05rem", marginBottom: 10 }}>Integraciones externas opcionales</h2>
        <div style={{ display: "flex", gap: 12, flexWrap: "wrap", fontSize: ".84rem" }}>
          <span style={{ padding: "7px 10px", borderRadius: 8, background: process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID ? "#E8F7EF" : "#F4F4F4", color: process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID ? "#17653B" : "#666" }}>
            Google Analytics: {process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID ? "configurado" : "pendiente de ID"}
          </span>
          <span style={{ padding: "7px 10px", borderRadius: 8, background: process.env.NEXT_PUBLIC_CLARITY_PROJECT_ID ? "#E8F7EF" : "#F4F4F4", color: process.env.NEXT_PUBLIC_CLARITY_PROJECT_ID ? "#17653B" : "#666" }}>
            Microsoft Clarity: {process.env.NEXT_PUBLIC_CLARITY_PROJECT_ID ? "configurado" : "pendiente de ID"}
          </span>
        </div>
        <p style={{ color: "var(--texto-suave)", fontSize: ".8rem", margin: "10px 0 0" }}>
          Este panel propio funciona sin esas cuentas. GA4 y Clarity solo se cargan después de que el visitante acepta la analítica.
        </p>
      </section>
    </main>
  );
}

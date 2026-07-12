import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import NavLanding from "./components/NavLanding";
import NivelTabs from "./components/NivelTabs";
import ConvocatoriasGrid from "./components/ConvocatoriasGrid";
import ContadorCupos from "./components/ContadorCupos";
import ScrollReveal from "./components/ScrollReveal";
import { waUrl, WA_MENSAJES, CORREO_CONTACTO, REDES } from "@/lib/contacto";
import "./landing.css";

export const dynamic = "force-dynamic";

const WA_URL = waUrl(WA_MENSAJES.comprar);
const WA_ASESORIA = waUrl(WA_MENSAJES.asesoria);
const CUPOS_LANZAMIENTO = 200; // Total de cupos del precio de lanzamiento

export default async function LandingPage() {
  let convocatorias: any[] = [];
  let cursosVendidos = 0;
  try {
    const supabase = createClient();
    const { data } = await supabase
      .from("convocatorias")
      .select("id, nombre, entidad, estado, etiqueta, vacantes, fecha_prueba_aprox, imagen_url")
      .eq("activa", true)
      .order("orden");
    convocatorias = data || [];

    // Contar cupos vendidos (pagos aprobados)
    const { count } = await supabase.from("pagos").select("*", { count: "exact", head: true }).eq("estado", "aprobado");
    cursosVendidos = count || 0;
  } catch {
    convocatorias = [];
  }

  return (
    <>
      <NavLanding />
      <ScrollReveal />

      {/* ===== HERO ===== */}
      <section className="hero">
        <div className="wrap hero-grid">
          <div>
            <span className="kick">⭐ Concursos de mérito · CNSC Colombia</span>
            <h1>Estudia para <span className="hl">tu cargo</span>, no para toda la convocatoria.</h1>
            <p className="sub">El único curso de la CNSC que estudia el <strong>manual de funciones de tu cargo específico</strong> —no solo tu nivel— y te prepara exactamente para lo que van a evaluarte en la prueba escrita.</p>
            <p className="vp">Deja de estudiar a ciegas. Sabe <strong>exactamente qué estudiar</strong> para ganar tu ascenso.</p>
            <div className="hero-cta">
              <Link href="/comprar" className="btn btn-oro">Quiero mi curso personalizado</Link>
              <a href={WA_ASESORIA} target="_blank" rel="noopener" className="btn btn-wa">💬 Asesoría por WhatsApp</a>
              <a href="#como" className="btn btn-ghost">Ver cómo funciona</a>
            </div>
            <a href="#convocatorias" className="btn btn-ghost btn-conv-movil">📋 Ver convocatorias disponibles</a>
            <div className="hero-mini">
              <span>🎯 Personalizado por cargo</span>
              <span>📅 Plan de 21 días</span>
              <span>📝 Simulacros tipo CNSC</span>
            </div>
          </div>

          {/* Mockup */}
          <div className="mockup" aria-hidden="true">
            <div className="float-badge fb-1"><span className="fb-ic">✅</span> Por tu cargo</div>
            <div className="mockup-card">
              <div className="mockup-head">
                <span className="mk-dot">AP</span>
                <span><b>Tu ruta de estudio</b><small>Plan personalizado · 21 días</small></span>
              </div>
              <div className="mk-row"><span className="mk-day">D1</span><p>Estado y función pública</p><span className="mk-check">✓</span></div>
              <div className="mk-row"><span className="mk-day">D5</span><p>Competencias de tu nivel</p><span className="mk-check">✓</span></div>
              <div className="mk-row"><span className="mk-day">D9</span><p>Funciones reales de tu empleo</p><span className="mk-check">✓</span></div>
              <div className="mk-row"><span className="mk-day">D14</span><p>Simulacro situacional tipo CNSC</p></div>
              <div className="mk-row"><span className="mk-day">D21</span><p>Simulacro integral final</p></div>
              <div className="mk-bar"><i></i></div>
              <div className="mk-prog"><span>Progreso</span><span>13 de 21 días</span></div>
            </div>
            <div className="float-badge fb-2"><span className="fb-ic">⚡</span> Listo en 12 h</div>
          </div>
        </div>
      </section>

      {/* ===== TRUST BAND ===== */}
      <div className="trust">
        <div className="trust-in">
          <span>🔒 <b>Pago seguro</b> con Wompi</span>
          <span>🏦 PSE · Nequi · Tarjetas</span>
          <span>🛡️ Datos protegidos · <b>Ley 1581</b></span>
          <span>⚡ Tu ruta lista en <b>12 horas</b></span>
        </div>
      </div>

      {/* ===== SIMULACRO GRATIS (lead magnet) ===== */}
      <section className="sim-promo" id="simulacro">
        <div className="wrap">
          <div className="sim-promo-head">
            <span className="sim-promo-tag">🎁 Gratis · sin registro · resultado al instante</span>
            <h2>Empieza con tu <span className="hl">simulacro gratis</span></h2>
            <p className="sim-promo-lead">Mide tu nivel en los temas que la CNSC evalúa en la prueba escrita. Al terminar recibes una <strong>retroalimentación</strong> con lo que ya dominas y lo que debes reforzar. Elige tu nivel:</p>
          </div>
          <div className="sim-promo-grid">
            <a href="/simulacro-gratis/asistencial.html" className="sim-promo-card">
              <span className="sim-promo-emoji">🧰</span>
              <h3>Nivel Asistencial</h3>
              <p>Estado, atención al ciudadano y competencias del nivel.</p>
              <span className="sim-promo-go">Empezar simulacro →</span>
            </a>
            <a href="/simulacro-gratis/tecnico.html" className="sim-promo-card">
              <span className="sim-promo-emoji">🛠️</span>
              <h3>Nivel Técnico</h3>
              <p>Marco institucional, procesos y competencias técnicas.</p>
              <span className="sim-promo-go">Empezar simulacro →</span>
            </a>
            <a href="/simulacro-gratis/profesional.html" className="sim-promo-card">
              <span className="sim-promo-emoji">🎓</span>
              <h3>Nivel Profesional</h3>
              <p>Función pública, gestión y competencias del nivel.</p>
              <span className="sim-promo-go">Empezar simulacro →</span>
            </a>
          </div>
          <div className="sim-promo-foot">
            <Link href="/simulacro" className="btn btn-azul">Ver los simulacros gratis →</Link>
            <span className="sim-promo-mini">20 preguntas · sin costo · sin necesidad de registrarte</span>
          </div>
        </div>
      </section>

      {/* ===== PROBLEMA ===== */}
      <section className="sec" id="problema">
        <div className="wrap">
          <span className="eyebrow">El problema</span>
          <h2>Estudiar sin dirección es perder tiempo</h2>
          <p className="lead">La mayoría de cursos te dan lo mismo a todos: PDFs enormes, videos genéricos y simulacros que no se parecen a tu prueba. El resultado: estudias mucho, pero no lo que tu cargo realmente evalúa.</p>
          <div className="grid grid-3">
            <div className="card pain"><span className="ic">📚</span><h3>Demasiada información</h3><p>Cientos de páginas y normas, sin saber cuáles aplican de verdad a tu empleo.</p></div>
            <div className="card pain"><span className="ic">🎯</span><h3>Cero personalización</h3><p>Te preparan para &quot;la convocatoria&quot; en general, no para el cargo específico al que aspiras.</p></div>
            <div className="card pain"><span className="ic">😵</span><h3>Simulacros que no se parecen</h3><p>Preguntas de memoria, cuando la CNSC evalúa con casos situacionales reales.</p></div>
          </div>
        </div>
      </section>

      {/* ===== SOLUCION ===== */}
      <section className="sec sec-alt" id="solucion">
        <div className="wrap">
          <div className="sol">
            <div>
              <span className="badge">La solución</span>
              <h2>Una ruta hecha a la medida de tu cargo</h2>
              <p style={{ color: "var(--texto-suave)", fontSize: "1.02rem" }}>Ascenso Público parte de <strong>tu OPEC, tu manual de funciones y tu nivel</strong> para construir un plan de estudio que se enfoca solo en lo que tu prueba va a evaluar.</p>
              <ul>
                <li>Analizamos las <strong>funciones reales</strong> de tu empleo.</li>
                <li>Identificamos las <strong>competencias</strong> que la CNSC evalúa en tu nivel.</li>
                <li>Te entregamos guías claras, dinámicas y <strong>simulacros tipo CNSC</strong>.</li>
                <li>Aprendes <strong>estrategia</strong>: cómo piensa la CNSC y cómo responder.</li>
              </ul>
            </div>
            <div className="sol-visual">
              <div className="big">Por tu cargo,<br/>no por la convocatoria.</div>
              <small>Esa es la diferencia.</small>
              <hr/>
              <p style={{ fontSize: ".95rem", color: "rgba(255,255,255,.9)" }}>«No se trata de estudiar más. Se trata de <strong style={{ color: "var(--oro-claro)" }}>estudiar mejor</strong>.»</p>
            </div>
          </div>
        </div>
      </section>

      {/* ===== EJEMPLO INTERACTIVO POR NIVEL ===== */}
      <section className="sec sec-alt center" id="ejemplo">
        <div className="wrap">
          <span className="eyebrow c">Mira la diferencia</span>
          <h2>Así se adapta tu ruta según tu nivel</h2>
          <p className="lead">Elige tu nivel y mira un <strong>ejemplo</strong> de cómo cambia el enfoque. Tu curso real va aún más lejos: se ajusta al <strong>manual de funciones de tu cargo específico</strong>.</p>
          <NivelTabs />
        </div>
      </section>

      {/* ===== STATS ===== */}
      <section className="sec" style={{ paddingTop: 64, paddingBottom: 64 }}>
        <div className="wrap">
          <div className="stats">
            <div className="stat"><div className="n">21<span className="u"> días</span></div><p>de plan estructurado paso a paso</p></div>
            <div className="stat"><div className="n">100<span className="u">%</span></div><p>enfocado en tu cargo y tu nivel</p></div>
            <div className="stat"><div className="n">12<span className="u"> h</span></div><p>y tu ruta queda lista en tu perfil</p></div>
            <div className="stat"><div className="n">CNSC</div><p>simulacros de juicio situacional</p></div>
          </div>
        </div>
      </section>

      {/* ===== COMO FUNCIONA ===== */}
      <section className="sec sec-alt" id="como">
        <div className="wrap">
          <span className="eyebrow">Cómo funciona</span>
          <h2>De la compra a tu ruta de estudio</h2>
          <p className="lead">Un proceso simple. Tú aportas los datos de tu cargo; nosotros armamos tu curso.</p>
          <div className="pasos">
            <div className="paso"><h3>Eliges tu convocatoria y cargas tus datos</h3><p>Seleccionas tu convocatoria y subes tu OPEC, el cargo, el nivel y el manual de funciones (te enseñamos cómo descargarlos).</p></div>
            <div className="paso"><h3>Pagas de forma segura</h3><p>Realizas un único pago con Wompi (PSE, Nequi o tarjeta de crédito/débito).</p></div>
            <div className="paso"><h3>Armamos tu ruta</h3><p>En máximo 12 horas construimos tu plan personalizado de 21 días y lo dejamos en tu perfil.</p></div>
            <div className="paso"><h3>Estudias y practicas</h3><p>Accedes a tus guías por día y cierras con tu simulacro final tipo CNSC.</p></div>
          </div>

          {/* Compromiso de tiempo diario */}
          <div style={{ marginTop: 32, display: "flex", alignItems: "center", gap: 18, background: "linear-gradient(135deg,#0A2A5E,#1A4A8A)", borderRadius: 16, padding: "22px 26px", color: "#fff", flexWrap: "wrap" }}>
            <div style={{ fontSize: "2.4rem", lineHeight: 1, flexShrink: 0 }}>⏱️</div>
            <div style={{ flex: 1, minWidth: 220 }}>
              <h3 style={{ margin: "0 0 4px", color: "#fff", fontSize: "1.12rem" }}>Con 1 a 1½ hora al día, vas a tu ritmo</h3>
              <p style={{ margin: 0, color: "rgba(255,255,255,.85)", fontSize: ".95rem" }}>
                Cada guía está diseñada para estudiarse en <strong style={{ color: "var(--oro-claro)" }}>60 a 90 minutos</strong>. Estudias <strong style={{ color: "var(--oro-claro)" }}>de lunes a viernes</strong> y descansas los fines de semana: son <strong style={{ color: "var(--oro-claro)" }}>20 días de preparación + tu simulacro final</strong>, un plan disciplinado que avanzas sin afán ni desgaste.
              </p>
            </div>
          </div>
        </div>
      </section>
      <section className="sec" id="incluye">
        <div className="wrap">
          <span className="eyebrow">Qué incluye</span>
          <h2>Todo lo que necesitas para tu prueba</h2>
          <p className="lead">Un plan completo, personalizado y enfocado en aprobar.</p>
          <div className="grid grid-2">
            <div className="feat"><div className="fic">🗺️</div><div><h3>Plan personalizado de 21 días</h3><p>Una ruta diseñada para tu cargo: general, por nivel y por las funciones reales de tu empleo.</p></div></div>
            <div className="feat"><div className="fic">📖</div><div><h3>Guías claras y dinámicas</h3><p>Contenido que se entiende, con ejemplos reales y enfocado en lo que la CNSC evalúa.</p></div></div>
            <div className="feat"><div className="fic">📝</div><div><h3>Simulacros tipo CNSC</h3><p>Preguntas situacionales con retroalimentación, igual que en la prueba real.</p></div></div>
            <div className="feat"><div className="fic">🧠</div><div><h3>Estrategia CNSC</h3><p>Aprende a identificar trampas, descartar distractores y administrar el tiempo.</p></div></div>
            <div className="feat"><div className="fic">🎓</div><div><h3>Simulacro integral final</h3><p>Una evaluación completa enfocada en tu OPEC para llegar listo el día del examen.</p></div></div>
            <div className="feat"><div className="fic">💻</div><div><h3>Acceso en tu perfil</h3><p>Estudias desde la plataforma, a tu ritmo, durante toda la vigencia de tu acceso.</p></div></div>
          </div>
        </div>
      </section>

      {/* ===== CONVOCATORIAS ===== */}
      <section className="sec sec-alt" id="convocatorias">
        <div className="wrap">
          <span className="eyebrow">Convocatorias disponibles</span>
          <h2>¿Tu concurso está activo?</h2>
          <p className="lead">Estas son las convocatorias para las que estamos preparando aspirantes ahora mismo. ¿No ves la tuya? <a href={waUrl(WA_MENSAJES.convocatoria)} target="_blank" rel="noopener" className="wa-link" style={{ color: "var(--azul)" }}>Escríbenos</a>.</p>
          <ConvocatoriasGrid convocatorias={convocatorias} />
        </div>
      </section>

      {/* ===== PRECIO ===== */}
      <section className="sec" id="precio">
        <div className="wrap">
          <span className="eyebrow c" style={{ display: "block", textAlign: "center" }}>Precio de lanzamiento</span>
          <h2 className="center">Invierte en tu ascenso</h2>
          <p className="lead center" style={{ margin: "0 auto 38px" }}>Un único pago por tu curso personalizado completo.</p>
          <div className="precio-card">
            <span className="precio-tag">🚀 Precio de lanzamiento</span>
            <div className="precio-num">$300.000 <small>COP</small></div>
            <p style={{ color: "var(--texto-suave)" }}>Pago único · Acceso a tu curso completo</p>
            <ul>
              <li>Plan personalizado de 21 días según tu cargo</li>
              <li>Todas las guías de tu ruta (general, nivel y funcionales)</li>
              <li>Simulacros tipo CNSC + simulacro integral final</li>
              <li>Guía de estrategia CNSC</li>
              <li>Acceso desde tu perfil durante la vigencia del curso</li>
            </ul>
            <Link href="/comprar" className="btn btn-oro" style={{ width: "100%", padding: 15 }}>Comprar mi curso</Link>
            <ContadorCupos vendidos={cursosVendidos} total={CUPOS_LANZAMIENTO} />
            <p style={{ fontSize: ".8rem", color: "var(--texto-suave)", marginTop: 14 }}>Pago seguro con Wompi · PSE, Nequi y tarjetas</p>
            <div className="garantia"><span className="gic">🛡️</span><span>¿Dudas antes de comprar? <a href={WA_ASESORIA} target="_blank" rel="noopener" className="wa-link" style={{ color: "var(--azul)" }}>Escríbenos por WhatsApp</a> y te asesoramos sin compromiso antes de pagar.</span></div>
          </div>
        </div>
      </section>

      {/* ===== FAQ ===== */}
      <section className="sec sec-alt" id="faq">
        <div className="wrap">
          <span className="eyebrow">Preguntas frecuentes</span>
          <h2>Resolvemos tus dudas</h2>
          <div className="faq" style={{ marginTop: 30 }}>
            <details open><summary>¿En qué se diferencia de otros cursos?</summary><div className="ans">No te preparamos para &quot;la convocatoria&quot; en general, sino para <strong>tu cargo específico</strong>. Analizamos tu OPEC y tu manual de funciones para enfocar el estudio en lo que tu prueba realmente evalúa.</div></details>
            <details><summary>¿Cuánto tarda en estar listo mi curso?</summary><div className="ans">En máximo <strong>12 horas</strong> desde tu compra tendrás tu ruta de estudio personalizada disponible en tu perfil.</div></details>
            <details><summary>¿Qué necesito para empezar?</summary><div className="ans">Tu número de OPEC, el nombre y nivel del cargo, y el <strong>manual de funciones en PDF</strong>. Dentro de la plataforma te explicamos cómo descargarlos de la página de la CNSC.</div></details>
            <details><summary>¿Cómo son los simulacros?</summary><div className="ans">Son de <strong>juicio situacional</strong>, igual que la prueba real de la CNSC: un caso y la mejor actuación, con retroalimentación por cada opción.</div></details>
            <details><summary>¿Cuánto tiempo debo dedicarle al día?</summary><div className="ans">Con <strong>1 a 1 hora y media al día</strong> es suficiente. Cada guía está diseñada para estudiarse en <strong>60 a 90 minutos</strong> y el plan está pensado para estudiar <strong>de lunes a viernes</strong>, descansando los fines de semana. Son <strong>20 días de preparación más tu simulacro final</strong>: avanzas con disciplina y sin saturarte.</div></details>
            <details><summary>¿Por cuánto tiempo tengo acceso?</summary><div className="ans">Tendrás acceso a tu curso durante la vigencia definida desde tu fecha de compra, suficiente para prepararte con calma para tu prueba.</div></details>
            <details><summary>¿Cómo pago?</summary><div className="ans">De forma segura con <strong>Wompi</strong>: PSE, Nequi o tarjeta de crédito/débito.</div></details>
          </div>
        </div>
      </section>

      {/* ===== CTA FINAL ===== */}
      <section className="cta-band">
        <div className="wrap">
          <h2>¿List@ para preparar tu ascenso?</h2>
          <p>Asegura tu cupo del precio de lanzamiento y empieza a estudiar con dirección.</p>
          <Link href="/comprar" className="btn btn-azul" style={{ padding: "15px 34px", fontSize: "1rem" }}>Quiero mi curso personalizado</Link>
        </div>
      </section>

      {/* ===== POLITICA DE DATOS ===== */}
      <section className="sec" id="datos" style={{ padding: "50px 0" }}>
        <div className="wrap" style={{ maxWidth: 760 }}>
          <span className="eyebrow">Privacidad</span>
          <h2 style={{ fontSize: "1.5rem" }}>Tratamiento de datos personales</h2>
          <p style={{ color: "var(--texto-suave)", fontSize: ".94rem" }}>En cumplimiento de la <strong>Ley 1581 de 2012</strong> y sus decretos reglamentarios, los datos que nos compartas (nombre, datos de contacto, número de OPEC, cargo y manual de funciones) se usan <strong>únicamente</strong> para crear y entregar tu curso personalizado y para comunicarnos contigo sobre tu preparación. No los compartimos con terceros ajenos a la prestación del servicio ni con la CNSC. Puedes solicitar en cualquier momento la consulta, actualización o eliminación de tus datos escribiéndonos a <a href="mailto:ascensopublico@gmail.com" style={{ color: "var(--azul)", fontWeight: 700, borderBottom: "1px solid var(--oro)" }}>ascensopublico@gmail.com</a>.</p>
        </div>
      </section>

      {/* ===== FOOTER ===== */}
      <footer className="landing-footer">
        <div className="brand" style={{ display: "inline-flex", justifyContent: "center" }}>
          <span className="brand-logo" style={{ width: 38, height: 38 }}>
            <svg viewBox="0 0 100 100" width={22} height={22} aria-hidden="true">
              <circle cx="26" cy="74" r="3.4" fill="#0A2A5E" opacity={0.45}/>
              <circle cx="34" cy="70" r="4.2" fill="#0A2A5E" opacity={0.72}/>
              <path d="M36 66 C48 62 58 54 72 34" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round"/>
              <path d="M61 32 L75 30 L73 45" fill="none" stroke="#0A2A5E" strokeWidth="9" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </span>
          <span className="brand-name" style={{ fontSize: "1.2rem" }}>Ascenso Público</span>
        </div>
        <div className="fslogan">Tu ruta personalizada hacia el empleo público</div>
        <div className="fcont">Escríbenos por <a href={WA_URL} target="_blank" rel="noopener" style={{ color: "#fff", fontWeight: 700, borderBottom: "1px solid var(--oro)" }}>WhatsApp</a> o al correo <a href="mailto:ascensopublico@gmail.com" style={{ color: "#fff", fontWeight: 700, borderBottom: "1px solid var(--oro)" }}>ascensopublico@gmail.com</a></div>
        {/* Redes sociales */}
        <div style={{ display: "flex", gap: 12, justifyContent: "center", margin: "16px 0 4px" }}>
          {REDES.tiktok && (
            <a href={REDES.tiktok} target="_blank" rel="noopener" aria-label="TikTok de Ascenso Público" style={{ width: 40, height: 40, borderRadius: 10, background: "rgba(255,255,255,.1)", border: "1px solid rgba(255,255,255,.2)", display: "inline-flex", alignItems: "center", justifyContent: "center", color: "#fff" }}>
              <svg width={20} height={20} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 0 1-2.59 2.5 2.59 2.59 0 0 1-2.59-2.59 2.59 2.59 0 0 1 3.39-2.46V7.3a5.7 5.7 0 0 0-.8-.06A5.66 5.66 0 0 0 4.2 12.9a5.66 5.66 0 0 0 9.66 4 5.66 5.66 0 0 0 1.65-4V9.01a7.33 7.33 0 0 0 4.29 1.37V7.3a4.28 4.28 0 0 1-3.2-1.48z"/></svg>
            </a>
          )}
          {REDES.instagram && (
            <a href={REDES.instagram} target="_blank" rel="noopener" aria-label="Instagram de Ascenso Público" style={{ width: 40, height: 40, borderRadius: 10, background: "rgba(255,255,255,.1)", border: "1px solid rgba(255,255,255,.2)", display: "inline-flex", alignItems: "center", justifyContent: "center", color: "#fff" }}>
              <svg width={20} height={20} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
            </a>
          )}
          <a href={WA_URL} target="_blank" rel="noopener" aria-label="WhatsApp de Ascenso Público" style={{ width: 40, height: 40, borderRadius: 10, background: "rgba(255,255,255,.1)", border: "1px solid rgba(255,255,255,.2)", display: "inline-flex", alignItems: "center", justifyContent: "center", color: "#fff" }}>
            <svg width={20} height={20} viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm5.52 11.99c-.25.7-1.47 1.36-2.02 1.41-.55.06-1.05.27-3.53-.74-2.97-1.2-4.84-4.24-4.99-4.44-.14-.2-1.18-1.57-1.18-3 0-1.42.75-2.12 1.01-2.41.26-.29.57-.36.76-.36.19 0 .38 0 .55.01.18.01.41-.07.64.49.25.6.83 2.07.9 2.22.07.15.12.32.02.52-.1.2-.15.32-.29.49-.15.17-.31.39-.44.52-.15.15-.3.31-.13.6.17.29.76 1.25 1.63 2.02 1.12.99 2.07 1.3 2.36 1.45.29.15.46.12.63-.07.17-.2.73-.85.92-1.14.19-.29.39-.24.64-.15.26.09 1.66.78 1.94.93.29.15.48.22.55.34.07.12.07.7-.18 1.4z"/></svg>
          </a>
        </div>
        <div className="fmeta">© {new Date().getFullYear()} Ascenso Público · Preparación para concursos de mérito CNSC.<br/>No afiliado a la CNSC. Material de preparación independiente.<br/><Link href="/privacidad" style={{ color: "rgba(255,255,255,.7)", borderBottom: "1px solid var(--oro)" }}>Política de privacidad</Link> · <Link href="/terminos" style={{ color: "rgba(255,255,255,.7)", borderBottom: "1px solid var(--oro)" }}>Términos y condiciones</Link></div>
      </footer>

      {/* ===== WhatsApp flotante ===== */}
      <a className="wa-float" href={WA_URL} target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">
        <svg width={24} height={24} viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15h-.01c-1.52 0-3.01-.41-4.3-1.18l-.31-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.37c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.82c0 4.54-3.69 8.23-8.23 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.16.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.5.11-.11.25-.29.37-.43.12-.14.16-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43-.14-.01-.31-.01-.48-.01a.92.92 0 0 0-.66.31c-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/></svg>
        <span>WhatsApp</span>
      </a>
    </>
  );
}

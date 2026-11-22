import Link from "next/link";
import { createClient } from "@/lib/supabase/server";
import NavLanding from "./components/NavLanding";
import ConvocatoriasGrid from "./components/ConvocatoriasGrid";
import ContadorCupos from "./components/ContadorCupos";
import ScrollReveal from "./components/ScrollReveal";
import { waUrl, WA_MENSAJES, CORREO_CONTACTO, REDES } from "@/lib/contacto";
import { formatOpecDate } from "@/lib/opec";
import opecMeta from "@/data/opec-meta.json";
import "./landing.css";

export const dynamic = "force-dynamic";

const WA_URL = waUrl(WA_MENSAJES.comprar);
const WA_PRECIO = waUrl(WA_MENSAJES.precio);
const WA_SIMULACRO = waUrl(WA_MENSAJES.simulacroPago);
const formatNumber = (value: number) => value.toLocaleString("es-CO");
const opecUpdatedDate = formatOpecDate(opecMeta.fechaActualizacion);

export default async function LandingPage() {
  let convocatorias: any[] = [];
  try {
    const supabase = createClient();
    const { data } = await supabase
      .from("convocatorias")
      .select("id, nombre, entidad, estado, etiqueta, vacantes, fecha_prueba_aprox, imagen_url, tema")
      .eq("activa", true)
      .order("orden");
    convocatorias = data || [];
  } catch {
    convocatorias = [];
  }

  return (
    <>
      <NavLanding />
      <ScrollReveal />

      {/* ===== 1. HERO ===== */}
      <section className="hero">
        <span className="hero-borde-oro" aria-hidden="true" />
        <div className="wrap hero-grid">
          <div>
            <span className="kick">⭐ Concursos de mérito · CNSC Colombia</span>
            <h1>Estudia para <span className="hl">tu cargo</span>, no para toda la convocatoria.</h1>
            <p className="sub">Armamos tu plan de estudio con <strong>el manual de funciones de tu cargo</strong> —no solo de tu nivel— para que estudies exactamente lo que van a evaluarte en la prueba escrita.</p>
            <div className="hero-cta">
              <a href={WA_PRECIO} target="_blank" rel="noopener" className="btn btn-oro" data-analytics-event="whatsapp_clicked" data-analytics-placement="hero_buy">Quiero mi curso · escribir por WhatsApp</a>
              <Link href="/guias-gratis" className="btn btn-ghost" data-analytics-event="cta_click" data-analytics-placement="hero_gratis">Probar gratis primero</Link>
            </div>
            <div className="hero-mini">
              <span>🎯 Personalizado por cargo</span>
              <span>📅 Plan de 21 días</span>
              <span>⚡ Listo en 24 horas</span>
            </div>
          </div>

          {/* Maqueta: captura real del producto */}
          <div className="hero-shot" aria-hidden="true">
            <div className="hero-window">
              <div className="hero-window-bar"><i /><i /><i /><span>ascensopublico.com · tu guía del día</span></div>
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/producto/guia.jpg" alt="" loading="eager" />
            </div>
            <div className="hero-ruta">
              <div className="hero-ruta-top"><span className="mk-dot">AP</span><span><b>Tu ruta de estudio</b><small>Plan de 21 días · por tu cargo</small></span></div>
              <div className="mk-row"><span className="mk-day">D1</span><p>Estado y función pública</p><span className="mk-check">✓</span></div>
              <div className="mk-row"><span className="mk-day">D9</span><p>Funciones reales de tu empleo</p><span className="mk-check">✓</span></div>
              <div className="mk-row"><span className="mk-day">D21</span><p>Simulacro integral final</p></div>
              <div className="mk-bar"><i></i></div>
              <div className="mk-prog"><span>Progreso</span><span>13 de 21 días</span></div>
            </div>
            <div className="float-badge fb-2"><span className="fb-ic">⚡</span> Listo en 24 h</div>
          </div>
        </div>
      </section>

      {/* ===== 2. CONCURSOS (lo primero que la gente viene a buscar) ===== */}
      <section className="sec sec-alt" id="convocatorias">
        <div className="wrap">
          <span className="eyebrow">Concursos · actualizado a noviembre de 2026</span>
          <h2>¿En qué va tu concurso?</h2>
          <p className="lead">Estado y próxima fecha de cada convocatoria que seguimos. Primero las que todavía tienen prueba escrita por delante. <strong>Si tu cargo ya tiene manual de funciones publicado, podemos armarte el curso</strong>, aparezca o no en esta lista: <a href={waUrl(WA_MENSAJES.convocatoria)} target="_blank" rel="noopener" className="wa-link" style={{ color: "var(--azul)" }}>escríbenos</a>.</p>
          <ConvocatoriasGrid convocatorias={convocatorias} />
        </div>
      </section>

      {/* ===== 3. GRATIS: simulacros y guías ===== */}
      <section className="sim-promo" id="simulacro">
        <div className="wrap">
          <div className="sim-promo-head">
            <span className="sim-promo-tag">🎁 Gratis · sin registro · resultado al instante</span>
            <h2>Mide tu nivel <span className="hl">antes de pagar nada</span></h2>
            <p className="sim-promo-lead">Simulacros con casos tipo prueba real y guías de estudio completas. Al terminar ves tu puntaje, la explicación de cada opción y qué debes reforzar.</p>
          </div>

          <div className="sim-promo-grid sim-promo-grid-2">
            <a href="/simulacro-gratis/procuraduria.html" className="sim-promo-card" data-analytics-event="cta_click" data-analytics-placement="landing_simulacro" data-analytics-level="procuraduria">
              <span className="sim-promo-emoji">⚖️</span>
              <h3>Procuraduría 2026</h3>
              <p>Cuatro simulacros: el núcleo común del concurso y uno por cada nivel de la convocatoria.</p>
              <span className="sim-promo-go">Empezar simulacro →</span>
            </a>
            <a href="/simulacro-gratis/docente.html" className="sim-promo-card" data-analytics-event="cta_click" data-analytics-placement="landing_simulacro" data-analytics-level="docente">
              <span className="sim-promo-emoji">👩‍🏫</span>
              <h3>Concurso Docente 2026</h3>
              <p>Lectura crítica, razonamiento, pedagogía y casos de aula.</p>
              <span className="sim-promo-go">Empezar simulacro →</span>
            </a>
          </div>

          <div className="sim-promo-foot">
            <Link href="/simulacro" className="btn btn-azul" data-analytics-event="cta_click" data-analytics-placement="landing_all_simulacros">Ver todos los simulacros</Link>
            <Link href="/guias-gratis" className="btn btn-ghost-conv" style={{ padding: "13px 22px" }} data-analytics-event="cta_click" data-analytics-placement="landing_guias_gratis">📚 Guías de estudio gratis</Link>
          </div>
        </div>
      </section>

      {/* ===== 4. ASÍ SE VE POR DENTRO ===== */}
      <section className="dentro" id="dentro">
        <div className="wrap">
          <span className="eyebrow c">Así se ve por dentro</span>
          <h2 className="center">No son PDFs. Son guías que se usan.</h2>
          <p className="lead center">Cada día de tu ruta es una guía interactiva: explicación, casos reales, trampas frecuentes, tarjetas de repaso y un simulacro al final. Se abren en el navegador, desde el celular o el computador.</p>

          <div className="dentro-grid">
            <article className="dentro-item">
              <div className="dentro-shot">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/producto/guia.jpg" alt="Guía interactiva de Ascenso Público con secciones de objetivo, desarrollo, casos y repaso" loading="lazy" />
              </div>
              <div className="dentro-txt">
                <span className="dentro-num">01</span>
                <h3>Guías interactivas, no archivos muertos</h3>
                <p>Objetivo, desarrollo, comparaciones, casos tipo CNSC, errores frecuentes, repaso y simulacro. Avanzas por secciones y la guía te lleva de la mano.</p>
              </div>
            </article>

            <article className="dentro-item alt">
              <div className="dentro-shot">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/producto/caso.jpg" alt="Caso práctico resuelto dentro de una guía de Ascenso Público" loading="lazy" />
              </div>
              <div className="dentro-txt">
                <span className="dentro-num">02</span>
                <h3>Casos resueltos con el razonamiento completo</h3>
                <p>No basta con saber la respuesta: te mostramos por qué cada opción equivocada es una trampa. Eso es lo que define tu puntaje en juicio situacional.</p>
              </div>
            </article>

            <article className="dentro-item">
              <div className="dentro-shot">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src="/producto/simulacro.jpg" alt="Simulacro de Ascenso Público con un caso y tres opciones de respuesta" loading="lazy" />
              </div>
              <div className="dentro-txt">
                <span className="dentro-num">03</span>
                <h3>Simulacros con el formato real</h3>
                <p>Casos con tres opciones plausibles, el formato oficial de la Prueba de Juicio Situacional. Al terminar ves tu puntaje, la explicación de cada opción y los temas que debes reforzar.</p>
              </div>
            </article>
          </div>
        </div>
      </section>

      {/* ===== 5. CÓMO FUNCIONA ===== */}
      <section className="sec" id="como">
        <div className="wrap">
          <span className="eyebrow">Cómo funciona</span>
          <h2>De tu mensaje a tu ruta de estudio</h2>
          <p className="lead">Tú nos dices tu cargo; nosotros armamos el plan. Todo empieza por WhatsApp.</p>
          <div className="pasos">
            <div className="paso"><h3>Nos escribes por WhatsApp</h3><p>Nos dices tu convocatoria y tu cargo. Te confirmamos el precio de tu nivel y resolvemos tus dudas sin compromiso.</p></div>
            <div className="paso"><h3>Revisamos tu OPEC</h3><p>Verificamos tu empleo y su manual de funciones. Si no sabes dónde están, te enseñamos a descargarlos.</p></div>
            <div className="paso"><h3>Armamos tu ruta en 24 horas</h3><p>Construimos tu plan de 21 días con las guías generales, las de tu nivel y las funcionales de tu empleo.</p></div>
            <div className="paso"><h3>Estudias y practicas</h3><p>Entras con tu usuario, avanzas una guía por día (60 a 90 minutos) y cierras con el simulacro integral.</p></div>
          </div>
          <div className="como-cta">
            <a href={WA_PRECIO} target="_blank" rel="noopener" className="btn btn-wa" data-analytics-event="whatsapp_clicked" data-analytics-placement="como_wa">💬 Escribir por WhatsApp</a>
          </div>
        </div>
      </section>

      {/* ===== 6. PRECIO ===== */}
      <section className="sec sec-alt" id="precio">
        <div className="wrap">
          <span className="eyebrow c" style={{ display: "block", textAlign: "center" }}>Precio por nivel</span>
          <h2 className="center">El precio depende del cargo al que aspiras</h2>
          <p className="lead center" style={{ margin: "0 auto 34px" }}>Como los derechos de participación del concurso, el valor cambia según el nivel del empleo. Pago único, sin mensualidades.</p>

          <div className="precio-grid">
            <div className="precio-nivel">
              <span className="precio-nivel-tag">Operativo y administrativo</span>
              <div className="precio-nivel-num">$150.000</div>
              <p>Auxiliares, citadores y oficinistas.</p>
            </div>
            <div className="precio-nivel">
              <span className="precio-nivel-tag">Técnico</span>
              <div className="precio-nivel-num">$200.000</div>
              <p>Sustanciadores, técnicos y tecnólogos.</p>
            </div>
            <div className="precio-nivel destacado">
              <span className="precio-nivel-tag">Profesional</span>
              <div className="precio-nivel-num">$250.000</div>
              <p>Profesional universitario y equivalentes.</p>
            </div>
            <div className="precio-nivel">
              <span className="precio-nivel-tag">Asesor y ejecutivo</span>
              <div className="precio-nivel-num">$350.000</div>
              <p>Asesores y cargos de dirección.</p>
            </div>
          </div>

          <div className="precio-incluye">
            <h3>Lo que incluye, en cualquier nivel</h3>
            <ul>
              <li>Plan personalizado de 21 días construido con tu OPEC y tu manual de funciones</li>
              <li>Guías generales, de tu nivel y funcionales de tu empleo</li>
              <li>Simulacros tipo CNSC y simulacro integral final</li>
              <li>Guía de estrategia: cómo piensa la CNSC y cómo descartar distractores</li>
              <li>Acceso desde tu perfil durante toda la vigencia del curso</li>
            </ul>
            <a href={WA_PRECIO} target="_blank" rel="noopener" className="btn btn-oro" style={{ width: "100%", padding: 15 }} data-analytics-event="whatsapp_clicked" data-analytics-placement="pricing_wa">💬 Pedir mi curso por WhatsApp</a>
            <ContadorCupos />
            <p className="precio-nota">Te confirmamos el precio exacto de tu cargo antes de que pagues. Sin compromiso.</p>
          </div>
        </div>
      </section>

      {/* ===== 7. SIMULACRO COMPLETO DE PAGO ===== */}
      <section className="sim39" id="simulacro-completo">
        <div className="wrap sim39-grid">
          <div>
            <span className="eyebrow c">¿Todavía no quieres el curso completo?</span>
            <h2>Simulacro completo de tu cargo</h2>
            <p>100 preguntas con el formato de la prueba real, cronómetro y explicación de cada opción. Al terminar recibes un informe con tu puntaje por competencia y qué estudiar primero.</p>
            <ul className="sim39-lista">
              <li>100 preguntas construidas con los ejes temáticos de tu empleo</li>
              <li>Cronómetro y una sola sesión, como en el examen</li>
              <li>Explicación de por qué cada opción es correcta o es trampa</li>
              <li>Informe por competencia y plan de refuerzo</li>
            </ul>
            <div className="sim39-precio">
              <div><span className="sim39-num">$39.000</span><small>pago único</small></div>
              <p>Y si después compras el curso, <strong>te lo descontamos completo</strong> durante los 30 días siguientes.</p>
            </div>
            <div className="sim39-ctas">
              <Link href="/simulacro-completo" className="btn btn-oro" data-analytics-event="cta_click" data-analytics-placement="sim39_page">Ver el simulacro completo</Link>
              <a href={WA_SIMULACRO} target="_blank" rel="noopener" className="sim39-wa" data-analytics-event="whatsapp_clicked" data-analytics-placement="sim39_wa">o pídelo por WhatsApp</a>
            </div>
          </div>
          <div className="sim39-shot" aria-hidden="true">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/producto/simulacro.jpg" alt="" loading="lazy" />
          </div>
        </div>
      </section>

      {/* ===== 8. BUSCADOR OPEC ===== */}
      <section className="opec-home-promo" id="buscador-opec">
        <div className="wrap opec-home-grid">
          <div className="opec-home-copy">
            <span className="opec-home-tag"><i /> Herramienta gratuita</span>
            <h2>Encuentra la vacante que <span>sí encaja contigo</span></h2>
            <p>Explora las OPEC de la convocatoria Empresas Sociales del Estado 2026. Filtra por profesión, ciudad, salario y experiencia sin revisar cientos de páginas en SIMO.</p>
            <div className="opec-home-points">
              <span><b>{formatNumber(opecMeta.totalOpec)}</b> OPEC consolidadas</span>
              <span><b>{formatNumber(opecMeta.totalVacantes)}</b> vacantes</span>
              <span><b>{formatNumber(opecMeta.sinExperiencia)}</b> sin experiencia</span>
            </div>
            <Link href="/buscador-opec" className="btn btn-oro opec-home-cta" data-analytics-event="cta_click" data-analytics-placement="landing_search">Buscar mi OPEC gratis <span aria-hidden="true">→</span></Link>
            <small>Sin registro · información actualizada al {opecUpdatedDate}</small>
          </div>
          <div className="opec-home-demo" aria-hidden="true">
            <div className="opec-home-window">
              <div className="opec-home-window-top"><i /><i /><i /><span>Buscador OPEC ESE 2026</span></div>
              <div className="opec-home-search"><span>⌕</span> Auxiliar sin experiencia</div>
              <div className="opec-home-filter-row"><span>Todos los departamentos</span><span>Asistencial</span><span>Sin experiencia ✓</span></div>
              <div className="opec-home-result">
                <div><span>Asistencial</span><b>OPEC 193509</b></div>
                <h3>Auxiliar área salud</h3>
                <p>E.S.E. Hospital Universitario de La Samaritana · Bogotá D.C.</p>
                <div><strong>$1.643.220</strong><em>✓ Sin experiencia</em></div>
              </div>
              <div className="opec-home-result second">
                <div><span>Asistencial</span><b>OPEC 206227</b></div>
                <h3>Auxiliar administrativo</h3>
                <p>E.S.E. Hospital San Rafael · Facatativá</p>
              </div>
            </div>
            <div className="opec-home-float"><span>✓</span><b>Tu OPEC ideal</b><small>Lista para buscar en SIMO</small></div>
          </div>
        </div>
      </section>

      {/* ===== 9. FAQ ===== */}
      <section className="sec" id="faq">
        <div className="wrap">
          <span className="eyebrow">Preguntas frecuentes</span>
          <h2>Resolvemos tus dudas</h2>
          <div className="faq" style={{ marginTop: 30 }}>
            <details open><summary>¿En qué se diferencia de otros cursos?</summary><div className="ans">No te preparamos para &quot;la convocatoria&quot; en general, sino para <strong>tu cargo específico</strong>. Analizamos tu OPEC y tu manual de funciones para enfocar el estudio en lo que tu prueba realmente evalúa.</div></details>
            <details><summary>¿Tienen curso para mi convocatoria?</summary><div className="ans">Sí, para <strong>cualquier concurso cuyo cargo ya tenga manual de funciones publicado</strong>, incluido el <strong>concurso docente</strong>. El curso no se arma a partir de un temario nuestro sino de tu empleo, así que lo que necesitamos es tu OPEC y tu manual de funciones. Si el concurso todavía no los publica, te avisamos apenas salgan.</div></details>
            <details><summary>¿Cuánto cuesta para mi cargo?</summary><div className="ans">Depende del nivel del empleo: <strong>$150.000</strong> operativo y administrativo, <strong>$200.000</strong> técnico, <strong>$250.000</strong> profesional y <strong>$350.000</strong> asesor y ejecutivo. Escríbenos con tu convocatoria y tu cargo y te confirmamos el valor exacto.</div></details>
            <details><summary>¿Cuánto tarda en estar listo mi curso?</summary><div className="ans">En máximo <strong>24 horas</strong> desde el pago tendrás tu ruta personalizada en tu perfil.</div></details>
            <details><summary>¿Qué necesito para empezar?</summary><div className="ans">Tu número de OPEC, el nombre y nivel del cargo, y el <strong>manual de funciones en PDF</strong>. Si no sabes dónde están, te guiamos por WhatsApp para descargarlos.</div></details>
            <details><summary>¿Cuánto tiempo debo dedicarle al día?</summary><div className="ans">Entre <strong>60 y 90 minutos</strong>. El plan está pensado para estudiar <strong>de lunes a viernes</strong>: son 20 días de preparación más el simulacro final.</div></details>
            <details><summary>¿Cómo son los simulacros?</summary><div className="ans">De <strong>juicio situacional</strong>, como la prueba real: un caso y tres opciones plausibles, con la explicación de cada una. Puedes probar los gratuitos antes de comprar.</div></details>
            <details><summary>¿Cómo pago?</summary><div className="ans">Coordinamos el pago por WhatsApp: PSE, Nequi o tarjeta a través de <strong>Wompi</strong>. Te enviamos el enlace de pago seguro.</div></details>
          </div>
        </div>
      </section>

      {/* ===== 10. CTA FINAL ===== */}
      <section className="cta-band">
        <div className="wrap">
          <h2>¿List@ para preparar tu ascenso?</h2>
          <p>Cuéntanos tu convocatoria y tu cargo. Te decimos qué estudiar y cuánto cuesta, sin compromiso.</p>
          <a href={WA_PRECIO} target="_blank" rel="noopener" className="btn btn-azul" data-analytics-event="whatsapp_clicked" data-analytics-placement="final_wa" style={{ padding: "15px 34px", fontSize: "1rem" }}>💬 Escribir por WhatsApp</a>
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
      <a className="wa-float" href={WA_URL} target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp" data-analytics-event="whatsapp_clicked" data-analytics-placement="floating_button">
        <svg width={24} height={24} viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21h.01c5.46 0 9.91-4.45 9.91-9.91C21.96 6.45 17.5 2 12.04 2zm0 18.15h-.01c-1.52 0-3.01-.41-4.3-1.18l-.31-.18-3.12.82.83-3.04-.2-.31a8.2 8.2 0 0 1-1.26-4.37c0-4.54 3.7-8.23 8.24-8.23 2.2 0 4.27.86 5.82 2.42a8.18 8.18 0 0 1 2.41 5.82c0 4.54-3.69 8.23-8.23 8.23zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.12-.16.25-.64.81-.79.97-.14.17-.29.19-.54.06-.25-.12-1.05-.39-1.99-1.23-.74-.66-1.23-1.47-1.38-1.72-.14-.25-.01-.38.11-.5.11-.11.25-.29.37-.43.12-.14.16-.25.25-.41.08-.17.04-.31-.02-.43-.06-.12-.56-1.34-.76-1.84-.2-.48-.41-.42-.56-.43-.14-.01-.31-.01-.48-.01a.92.92 0 0 0-.66.31c-.23.25-.87.85-.87 2.07 0 1.22.89 2.4 1.01 2.56.12.17 1.75 2.67 4.24 3.74.59.26 1.05.41 1.41.52.59.19 1.13.16 1.56.1.48-.07 1.47-.6 1.68-1.18.21-.58.21-1.07.14-1.18-.06-.1-.22-.16-.47-.28z"/></svg>
        <span>WhatsApp</span>
      </a>
    </>
  );
}

# 📊 PLAN DE PROYECTO — Ascenso Público

> **Para qué sirve este documento.** Es la **vista de gestión** del proyecto: en qué fase vamos, qué está hecho, qué falta, en qué orden hacerlo, cuánto esfuerzo toma y cómo medir el avance.
>
> Complementa a `PROYECTO-MAESTRO.md` (el *qué* y el *porqué*). Aquí está el *cuándo*, *en qué orden* y *cuánto*.
>
> **Última actualización:** 14 de junio de 2026 · **Responsable:** César (fundador) · **Modelo de trabajo:** fundador + asistente IA.

---

## 1. Ficha del proyecto

| Campo | Detalle |
|---|---|
| **Proyecto** | Ascenso Público — plataforma de preparación personalizada para concursos CNSC. |
| **Objetivo** | Llevar el producto de "contenido base listo" a "plataforma vendible con primer cliente real". |
| **Alcance (incluye)** | Contenido reutilizable, diseño de lo personalizable, producción a demanda, plataforma web, marketing y (visión) automatización IA. |
| **Fuera de alcance (hoy)** | Desarrollo de la IA que genera guías sola (es visión futura, Fase 6). |
| **Estado global** | Contenido reutilizable casi completo; producto y comercialización por arrancar. |

---

## 2. Fases del proyecto (EDT / estructura de trabajo)

El proyecto se divide en **6 fases**. Cada fase agrupa paquetes de trabajo (entregables concretos).

### Fase 0 · Fundación  ✅
- 0.1 Identidad de marca y logo (V2) — congelado.
- 0.2 Estándar técnico de guías (CSS/HTML/JS) — congelado.
- 0.3 Repositorio, biblioteca versionable y documentación maestra.

### Fase 1 · Contenido reutilizable  ✅ (95%)
- 1.1 Biblioteca General — INTRO-00, GEN-01/02/03 (Días 1–4). ✅
- 1.2 Biblioteca por Nivel — Asistencial, Técnico y Profesional (12 guías, Días 5–8). ✅
- 1.3 Bonus — BON-01 Estrategia CNSC. 🟦 *construido; PR pendiente de merge.*

### Fase 2 · Diseño de lo personalizable  ⏳ (se define con la PRIMERA COMPRA)
> **Decisión (14 jun):** el molde de las guías funcionales y del simulacro final se diseñará **en tiempo real con el primer cliente** (OPEC real). Al verlo funcionando se fija el estándar para las próximas compras. Se evita diseñar en abstracto.
- 2.1 **Diseño de las guías funcionales** — se define con la 1ª compra.
- 2.2 **Diseño del simulacro integral final (SIM-001)** — se define con la 1ª compra.
- 2.3 Decisión sobre **guías adicionales** — tras ver el caso real.

### Fase 3 · Producción a demanda (por cliente/OPEC)  ⬜
- 3.1 Guías funcionales según funciones del cargo.
- 3.2 INTRO-01 "Conoce tu Entidad" (por entidad, `ENT-xxx`).
- 3.3 SIM-001 personalizado por OPEC.
- 3.4 Generador/flujo para armar un plan completo desde OPEC + manual.

### Fase 4 · Plataforma / Producto  ⬜
- 4.1 **Landing page** (presentación + captación + venta).
- 4.2 Registro/compra + carga de datos (OPEC, manual de funciones).
- 4.3 Panel del estudiante (estado "en preparación/listo" + barra de progreso + acceso a guías).
- 4.4 Panel administrador (gestionar clientes, planes, publicación de guías).

### Fase 5 · Marketing y adquisición  ⬜
- 5.1 **TikTok / redes** — gestionado por el fundador con apoyo de IA externa (Claude).
- 5.2 Otros canales (a definir).
- 5.3 Embudo: contenido en redes → **landing** → captación/compra.

### Fase 6 · Automatización IA (visión futura)  ⬜
- 6.1 Analizar OPEC + manual → generar plan → generar guías → publicar.

---

## 3. Tablero de avance (dashboard)

| Fase | Estado | Avance | Entregable que falta para cerrarla |
|---|:--:|:--:|---|
| 0 · Fundación | ✅ Completa | 100% | — |
| 1 · Contenido reutilizable | 🟦 Casi | 95% | Mergear BON-01 |
| 2 · Diseño de lo personalizable | ⏳ Diferida | — | Se define con la primera compra (caso real) |
| 3 · Producción a demanda | ⬜ Por iniciar | 0% | Depende de Fase 2 y del primer cliente |
| 4 · Plataforma | ⬜ Por iniciar | 0% | Landing → compra → panel estudiante |
| 5 · Marketing | ⬜ Por iniciar | 0% | TikTok y embudo |
| 6 · Automatización IA | ⬜ Visión | 0% | — |

**Lectura rápida:** el **producto-contenido** está prácticamente listo (Fases 0–1). El proyecto entra ahora en **diseño de lo personalizable (Fase 2)** y, en paralelo, en **plataforma (Fase 4)** y **marketing (Fase 5)**, que son los frentes que convierten el contenido en un negocio.

---

## 4. Cronograma sugerido (orden + esfuerzo estimado)

> Las estimaciones son en **sesiones de trabajo** (no días calendario), para que tú les pongas fechas reales según tu disponibilidad. Las dependencias indican qué debe ir antes.

| # | Paquete de trabajo | Esfuerzo aprox. | Depende de | Se puede en paralelo |
|:--:|---|:--:|:--:|:--:|
| 1 | Mergear BON-01 | 5 min | — | — |
| 2 | Spec diseño guías funcionales (2.1) | 1 sesión | — | con 3, 5, 6 |
| 3 | Spec diseño simulacro SIM-001 (2.2) | 1 sesión | — | con 2, 5, 6 |
| 4 | Decidir guías adicionales (2.3) | 0.5 sesión | 2 | — |
| 5 | Landing page v1 (4.1) | 2–3 sesiones | — | con 2, 3 |
| 6 | Línea de contenido TikTok (5.1) | 1–2 sesiones | — | con 2, 3, 5 |
| 7 | Plataforma: compra + panel estudiante (4.2–4.3) | varias | 5 | — |
| 8 | Producción guías funcionales del 1er cliente (3.1) | según cargo | 2 | — |
| 9 | SIM-001 del 1er cliente (3.3) | 1 sesión | 3, 8 | — |

**Ruta crítica hacia "primer cliente":** 2 → 8 → 9 (contenido) y 5 → 7 (plataforma de venta). Marketing (6) alimenta el embudo en paralelo.

---

## 5. Hitos (milestones)

- **M1 — Contenido reutilizable completo** 🟦 *(a un merge de cumplirse: BON-01).*
- **M2 — Moldes definidos:** specs de guías funcionales y de SIM-001 aprobadas. *(siguiente meta).*
- **M3 — Presencia y captación:** landing publicada + primeros TikToks al aire.
- **M4 — MVP vendible:** compra + panel del estudiante funcionando con un curso de ejemplo.
- **M5 — Primer cliente real:** plan personalizado producido y entregado de punta a punta.
- **M6 — Escala/automatización:** generación asistida por IA.

---

## 6. Próximo paso recomendado (actualizado 14 jun)

**Decisión del fundador:** la Fase 2 (diseño de guías funcionales y simulacro) se trabaja **con la primera compra**, sobre un caso real. El foco inmediato pasa a **producto y captación**.

Orden de trabajo:
1. **Mergear BON-01** (cierra la Fase 1).
2. **Landing page** ← prioridad inmediata (se construye con el asistente).
3. **TikTok / redes** ← lo gestiona el fundador con apoyo de IA externa (Claude); el landing es el destino del embudo.
4. **Fase 2 (funcionales + simulacro)** ← se diseña en tiempo real al llegar la primera compra.

> Razón: ya hay contenido de calidad para mostrar; lo que urge es **tener presencia y captar demanda** mientras se diseña lo personalizable con un caso real.

---

## 7. Backlog priorizado (lista viva)

| Prioridad | Ítem | Fase |
|:--:|---|:--:|
| 🔴 Alta | Spec diseño guías funcionales | 2.1 |
| 🔴 Alta | Spec diseño SIM-001 | 2.2 |
| 🔴 Alta | Landing page v1 | 4.1 |
| 🟠 Media | Línea de contenido TikTok | 5.1 |
| 🟠 Media | Decidir guías adicionales | 2.3 |
| 🟠 Media | Plataforma: compra + panel estudiante | 4.2–4.3 |
| 🟢 Baja | Panel admin | 4.4 |
| 🟢 Baja | Automatización IA | 6 |

---

## 8. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Producir guías funcionales sin un molde claro | Inconsistencia y retrabajo | Cerrar la spec (2.1) antes de producir. |
| Alcance muy grande para un fundador solo | Estancamiento | Trabajar por hitos cortos; priorizar MVP vendible. |
| Tener contenido pero sin canal de venta | Cero ingresos | Avanzar plataforma + marketing en paralelo. |
| Personalización lenta por cliente | Mala experiencia | Diseñar la producción a demanda como proceso repetible. |

---

## 9. Cómo se mide el avance

- **Por fase:** % de paquetes de trabajo entregados (tablero §3).
- **Por hito:** M1…M6 cumplidos.
- **Indicador de negocio (cuando aplique):** landing publicada → visitas → registros → primer pago.

> Este documento es **vivo**: al cerrar un paquete o hito, se actualiza el tablero (§3) y los hitos (§5). El detalle de guías sigue en `biblioteca/biblioteca.json`.

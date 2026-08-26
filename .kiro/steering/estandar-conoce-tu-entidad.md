---
inclusion: auto
---

# Estándar de guías "Conoce tu Entidad" (ENT-*) — Ascenso Público

> **Regla permanente aprobada por el cliente (Julio César, ago-2026).**
> Toda guía "Conoce tu Entidad" debe seguir este modelo. Benchmark aprobado: `guias/ENT-DIAN-01-conoce-entidad-dian.html`.

## Principios

1. **GENERAL y REUTILIZABLE por entidad.** La guía ENT sirve para **cualquier cargo/nivel de esa entidad**, así que **NO menciona cargo, código ni OPEC en el cuerpo**. Una sola ENT-<SIGLA>-01 se reutiliza en todos los cursos futuros de la misma entidad. (El enfoque del cargo vive en las comportamentales y funcionales, no aquí.)
2. **PREMIUM, al nivel de una guía de Desarrollo.** ~4.000–4.500 palabras, ~15 secciones navegables con `nav` sticky. Nunca un "abrebocas" corto.
3. **Específica de la entidad:** NO reutilizable entre entidades distintas (cada entidad tiene su propia ENT).

## Estructura del modelo (15 secciones)

1. **Bienvenida** — hero + recuadro dorado "qué vas a dominar".
2. **Identidad** — tarjetas `.id-item` (nombre, naturaleza jurídica, adscripción, máxima autoridad, cobertura, régimen de carrera) + recuadro que explica su naturaleza jurídica.
3. **Misión, Visión y Valores** — `.mvv` + `.valores` (código de integridad de la entidad) + recuadro "ojo en la prueba".
4. **Historia** — línea de tiempo `.timeline` con hitos normativos.
5. **Qué hace** — ámbitos + día a día en tarjetas `.linea`.
6. **Lo que administra / su objeto** — tabla + distinciones clave.
7. **Conceptos clave** — 10–12 definiciones `.def` (término + explicación) del vocabulario que verá el estudiante.
8. **Herramientas** — acordeones `.acc` (sistemas/plataformas de la entidad).
9. **Organización** — tarjetas + diagrama `.flujo` de dónde encaja el cargo (en genérico).
10. **La entidad en cifras** — `.stat` con datos reales verificados.
11. **Servicios y canales de atención** — `.canal` con enlaces oficiales.
12. **Transparencia y participación ciudadana** — Ley 1712/2014, rendición de cuentas.
13. **Marco legal** — `.leyes` con enlaces a la norma.
14. **Para tu prueba** — ideas clave + ventaja situacional.
15. **Fuentes oficiales para consultar** — bloque `.fuentes` con 15–30 enlaces oficiales agrupados por tema.

## Reglas de contenido y forma

- **Muchos enlaces a fuentes oficiales verificadas** (`target="_blank"`); nunca inventados/rotos. Verificar HTTP 200 cuando el dominio lo permita (algunos como cnsc.gov.co bloquean curl pero abren en navegador).
- **Frases clave con `<mark>`** (subrayado dorado, no fondo).
- **Datos y cifras reales verificados** en fuentes oficiales (nunca inventar vacantes ni montos).
- Identidad de marca navy `#0A2A5E` / oro `#E8A33D` / crema `#FBF9F4`; barra de progreso de lectura; JS que resalta la sección activa del `nav`.
- Si el concurso lo organiza la **CNSC**, mencionarla como organizadora. Si es **régimen especial** (PGN, etc.), NO decir CNSC.

## Validación obligatoria antes de entregar

- HTML balanceado (div/section/details/ul/table), `node --check` del JS sin errores.
- 0 fugas de otro cargo, nivel, entidad o aspirante.
- Día coherente (kicker/footer).
- Sincronizar `guias/<archivo>.html` y `plataforma/public/seed-guias/<archivo>.html` con `scripts/sync-biblioteca.sh` y registrar en `biblioteca/biblioteca.json`.
- Tras desplegar, re-subir el bucket (`/api/admin/seed-guias`) para que el estudiante vea la versión nueva.

## Codificación

- `ENT-[SIGLA]-01` (ej. `ENT-DIAN-01`, `ENT-PGN-01`, `ENT-IDV-01`). El "Día" mostrado es siempre "Día 1 · Conoce tu Entidad".

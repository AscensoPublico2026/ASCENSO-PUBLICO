# 🚚 MIGRACIÓN DEL PROYECTO — Ascenso Público (a Claude u otra IA)

> Documento para retomar TODO el proyecto en otra herramienta de IA (Claude Code, Cursor, Copilot)
> sin perder nada. **Todo el trabajo vive en este repositorio de GitHub**, no en ninguna IA.
> El cliente/fundador es **Julio César**. Última migración documentada: 22 sep 2026.

---

## 0. Lo primero (tranquilidad): nada se pierde
Todo el código, las 200+ guías HTML, los simulacros, la plataforma (Next.js) y toda la
documentación del método están en **GitHub: `AscensoPublico2026/ASCENSO-PUBLICO`**.
Migrar de IA = solo conectar ese repo en la herramienta nueva y pegarle el prompt de la §3.
El "cerebro" del proyecto (proceso, estándares, moldes, specs) está escrito en el repo.

---

## 1. Qué herramienta usar
| Opción | Qué es | Por qué |
|---|---|---|
| **Claude Code** (recomendado) | IA en la terminal que clona el repo, edita archivos, corre git/node/python | Lo más parecido a como se venía trabajando (agente sobre el repo). |
| **Cursor** | Editor de código con IA (puede usar Claude por dentro) | Cómodo para ver los cambios y darles merge visualmente. |
| **GitHub Copilot (agente/workspace)** | Agente de IA integrado con GitHub | Bien si ya vives en GitHub. |

Cualquiera sirve: el conocimiento no está en la IA, está en el repo.

**Para instalar Claude Code:** buscar "Claude Code" en el sitio oficial de Anthropic, instalarlo,
autenticarse con la cuenta, y en una carpeta local ejecutar el clon del repo (ver §2).

---

## 2. Poner el repo en la máquina nueva (HTTPS)
```bash
git clone https://github.com/AscensoPublico2026/ASCENSO-PUBLICO.git
cd ASCENSO-PUBLICO
```
La IA nueva necesitará acceso a GitHub (con tu cuenta o un token). Nada más para el CONTENIDO
(guías/simulacros): eso solo requiere el repo, git, python3 y node.

---

## 3. PROMPT DE ARRANQUE (pegar tal cual en la IA nueva)

```
Eres mi ingeniero de software y creador de contenido para "Ascenso Público"
(negocio de Julio César, el fundador — ese soy yo, con quien hablas directamente;
los aspirantes son los estudiantes destinatarios de cada curso, NO me confundas con ellos).

Trabajamos sobre el repo de GitHub: AscensoPublico2026/ASCENSO-PUBLICO (ya clonado).
Todo el conocimiento del proyecto ya está escrito ahí.

ANTES DE HACER NADA, lee y absorbe estos archivos para retomar el método y el estándar
EXACTOS (no improvises, síguelos al pie de la letra):
- MIGRACION-A-CLAUDE.md                   (este documento: contexto general)
- referencias/PROCESO-CURSOS-GUIAS.md     (proceso maestro para armar un curso de 21 días)
- referencias/PROMPT-INICIO-CURSO.md      (flujo de arranque de un curso nuevo)
- referencias/PROCESO-ASESORIA-VACANTES.md (si el trabajo es asesoría de vacantes)
- prompts/generador-guias.md              (estándar v3.0 de cada guía)
- prompts/generador-plan-estudio.md       (cómo armar el plan de 21 días)
- CONTINUIDAD.md                          (estado actual — fuente de verdad)
- ESTANDAR-TECNICO.md y PLANTILLA-GUIA.md (detalles técnicos del HTML)
- El spec del último curso aprobado: referencias/_SPEC-CURSO-3PU17V-VALENTINA.md
Confirma que existe el validador scripts/validar-guia.py y que node y python3 están disponibles.

REGLAS QUE NO SE ROMPEN (detalladas en esos archivos; resumen):
1. PUSH POR GUÍA: rama feat/curso-<entidad>-<código>-<aspirante>, pushear de una,
   commit+push tras CADA tanda validada. Nunca acumular sin commitear.
2. Desarrollo (sección data-sec="2") >= 10.000 palabras en funcionales y generales,
   módulos profundos con VARIAS tablas y VARIOS ejemplos .practica en el ROL REAL del cargo,
   acordeones, 3-4 checkpoints, .flujo, .ojo, cierre "Idea clave/Tips/Frase para recordar"
   + .fuentes con enlaces reales target="_blank". Frases clave en <mark> (subrayado dorado).
3. Simulacros IDÉNTICOS a la prueba real: contexto 6-10 renglones (450-1000 caracteres),
   4 opciones largas (120-280 car) y confusas. Simulacro final (Día 21) = 50 funcionales
   + 20 comportamentales Likert = 70.
4. Reenfocar el molde, NO find-replace ciego. 0 FUGAS de otro aspirante/cargo/código/
   convocatoria/entidad (verificar con grep + límite de palabra en cada guía). La PGN es
   régimen ESPECIAL: NO mencionar la CNSC como organizadora.
5. Registrar cada guía en biblioteca/biblioteca.json Y plataforma/lib/biblioteca.json
   (sincronizar con scripts/sync-biblioteca.sh), copiar a plataforma/public/seed-guias/,
   y plan plantilla en plataforma/lib/autocargarGuias.ts.
6. Validar cada guía: node --check del JS + python3 scripts/validar-guia.py <archivo> "Día N"
   + grep de fugas = 0 + día coherente en kicker/badge/finalizar.

Al terminar un curso, dame el enlace directo para crear/mergear el PR
(https://github.com/AscensoPublico2026/ASCENSO-PUBLICO/pull/new/<rama>) y los pasos de carga
(merge -> deploy Vercel -> panel admin "Rehacer" con el plan -> /api/admin/seed-guias -> Ctrl+Shift+R).

Empieza confirmando que leíste el proceso y espera a que te dé los datos del próximo aspirante
(nombre, correo, cargo, código, convocatoria). Sé eficiente y directo.
```

---

## 4. Estado al día del trabajo (qué está hecho y qué falta mergear)

### Último curso terminado (pendiente de merge por Julio):
- **Valentina Martínez Valenzuela** — PGN Profesional Universitario **3PU-17** (Funciones Mixtas), Conv. **144-2026**.
  - Rama: `feat/curso-pgn-3pu17-valentina-martinez` — **22 guías completas, validadas y pusheadas**.
  - Spec: `referencias/_SPEC-CURSO-3PU17V-VALENTINA.md`. Plan plantilla: `pgn-profesional-3pu17-valentina`.
  - **Enlace para mergear:** https://github.com/AscensoPublico2026/ASCENSO-PUBLICO/pull/new/feat/curso-pgn-3pu17-valentina-martinez

### Otros cursos ya construidos (ver CONTINUIDAD.md para el detalle de cuáles están en main):
- Silvia Cortés — PGN Asesor 1AS-19 (Conv. 33-2026) — rama `feat/curso-pgn-1as19-silvia-cortes`.
- Nathaly Rodríguez — PGN Asesor 1AS-19 (Conv. 02-2026) — rama `feat/curso-pgn-1as19-nathaly-rodriguez`.
- Leyner Urrego — PGN Prof. Univ. 3PU-15 (Conv. 112-2026) — rama `feat/curso-pgn-3pu15-leyner`.
- María Alejandra — PGN Prof. Univ. 3PU-17 (Conv. 147-2026) — rama `feat/curso-pgn-3pu17-maria-alejandra`.
- DIAN Gestor I (Andrés Díaz) — varias ramas `feat/fun-dian-*` y `feat/sim-dian-001-*`.
- Otros: Gina (Procurador Judicial II), Viviana, URT, terapias, salud.

> ⚠️ Para saber con exactitud qué ramas están mergeadas a `main` y cuáles pendientes,
> en la IA nueva pídele: "compara cada rama feat/ con main y dime cuáles tienen commits sin mergear".
> Comando: `git log origin/main..origin/<rama> --oneline` (si sale vacío, ya está en main).

---

## 5. La plataforma web (Next.js + Supabase) — para el problema de PAGOS
- Carpeta: `plataforma/` (Next.js, deploy en **Vercel**, base de datos **Supabase**, pagos **Wompi**).
- Docs internas: `plataforma/SETUP.md`, `plataforma/DESPLIEGUE.md`, `ARQUITECTURA-PLATAFORMA.md`.
- **Pagos (Wompi):** el flujo usa llaves `pub_prod_`/`prv_prod_` y `PRECIO_COP=300000` (variables de
  entorno en Vercel). El webhook de eventos de Wompi debe apuntar a
  `https://ascensopublico.com/api/webhooks/wompi`. El endpoint `/activar` es robusto (activa aunque
  getTransaction falle, si el webhook ya procesó el pago).
- **Si la pasarela no funciona, revisar en este orden:**
  1. Que las llaves de Wompi en Vercel sean de PRODUCCIÓN y del comercio correcto (no de sandbox/otro entorno).
  2. Que el WEBHOOK en el panel de Wompi apunte a `https://ascensopublico.com/api/webhooks/wompi`.
  3. Logs de Vercel (Functions) al momento de pagar/activar.
  4. Que las variables de entorno de Supabase (URL, anon key, service role) estén bien en Vercel.
- Diagnóstico con la IA nueva: "lee plataforma/app/api/webhooks/wompi, /activar y lib/wompi.ts y
  dime por qué podría estar fallando la pasarela; propón el arreglo mínimo".

### Cosas que Julio debe tener a la mano (NO están en el repo por seguridad):
- Acceso a **Vercel** (proyecto de la plataforma) para ver logs y variables de entorno.
- Acceso a **Supabase** (proyecto) para la base de datos y el bucket 'guias'.
- Acceso al panel de **Wompi** (llaves y configuración del webhook).
- La cuenta de **GitHub** de AscensoPublico2026.

---

## 6. Pasos para publicar un curso (después de mergear su PR)
1. Merge del PR a `main` → esperar el deploy de Vercel (2-3 min).
2. En el panel admin del curso del estudiante → **🔄 Rehacer** con el plan plantilla correcto.
3. Visitar `https://ascensopublico.com/api/admin/seed-guias` (sube los HTML al bucket de Supabase).
4. Recargar sin caché (Ctrl+Shift+R).

---

## 7. Notas técnicas del entorno (para la IA nueva)
- Validar JS de una guía: extraer los `<script>` y `node --check`.
- Validar estructura: `python3 scripts/validar-guia.py <archivo> "Día N"` (marca `POSIBLES FUGAS: <código correcto>`
  como falso positivo del cargo del curso; lo importante es que NO aparezca el código de OTRO curso).
- Sincronizar catálogo + HTML a la plataforma: `bash scripts/sync-biblioteca.sh` (requiere `chmod +x`).
- Regla de anti-fugas: `grep -icE` con los tokens de otros cursos = 0 en cada guía.

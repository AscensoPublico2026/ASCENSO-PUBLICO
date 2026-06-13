---
inclusion: always
---

# Proyecto Ascenso Público — Reglas de trabajo (steering)

> Este archivo se carga automáticamente en cada sesión de Kiro para este repositorio.
> Mantiene el contexto del proyecto y las decisiones ya congeladas.
> **Documentos completos de referencia:** `ESTADO-PROYECTO.md`, `ESTANDAR-TECNICO.md`, `PLANTILLA-GUIA.md` (todos en la raíz).

---

## 1. Qué es este proyecto en una frase

**Ascenso Público** es una plataforma de cursos personalizados para aspirantes a concursos CNSC (Comisión Nacional del Servicio Civil) en Colombia. El cliente compra un curso adaptado a su vacante (OPEC + manual de funciones) y recibe un plan de 21 días con guías HTML interactivas + simulacro final.

**Slogan:** *Tu ruta personalizada al ascenso público.*

---

## 2. Identidad visual — CONGELADA (no cambiar sin permiso)

### Logo
- Concepto oficial: **V2 (flecha con impulso + estela)**.
- 4 variantes en `/brand/`: principal, navy, TikTok, favicon.
- **NO volver a explorar opciones de logo.** Está cerrado.

### Paleta — regla 60-30-10
- 60 % Crema cálido `#FBF9F4` (fondo)
- 30 % Azul institucional `#0A2A5E` (headers, títulos, nav)
- 10 % Dorado cálido `#E8A33D` (acentos, CTAs)
- Semánticos: verde `#1A7A4A`, rojo `#C0392B`, ámbar `#B8600A`, info azul `#2D6CC0`.

### Tipografías
- Títulos: `'Source Serif 4'` (serif)
- Texto: `'Plus Jakarta Sans'` (sans)
- Importadas vía Google Fonts en cada guía.

### Estilo
- Cálido + profesional. No "arcoíris", no "corporativo aburrido".
- Emojis distintivos por concepto (no decorativos: ayudan a memorizar).
- Bordes redondeados 12-16 px, sombras sutiles.
- Hover suave (`translateY(-2px)`).

---

## 3. Estándar de guías — CONGELADO

### Tiempo objetivo
**75–110 minutos** de estudio por guía.

### Las 11 secciones obligatorias
1. 🎯 Objetivo
2. ⭐ Importancia
3. 📖 Desarrollo (corazón — 6-8 conceptos en 4 capas)
4. ⚖️ Comparaciones (2-4 tablas)
5. 📂 Casos (5)
6. ⚠️ Errores (6)
7. 💡 Tips (6)
8. 🎭 Trampas (4)
9. 🧠 Repaso (10 flashcards)
10. 📝 Resumen + Glosario (6 + 6)
11. 🎓 Simulacro (12 preguntas)

### Las 4 capas por concepto (Desarrollo)
Cada concepto importante se presenta en este orden:
1. 🟦 **Definición** — qué es exactamente (con norma + artículo)
2. 🟩 **Aplicación** — para qué sirve, cómo opera en la práctica
3. 🟨 **Ejemplo real** — caso verificable con entidad/OPEC concreta
4. 🟥 **Cómo lo evalúa la CNSC** — cómo aparece en la prueba real

**Longitud por capa:** 2 a 4 párrafos cortos. Ni más, ni menos.

### Patrón "concepto madre + sub-bloques"
Para conceptos con 3+ sub-componentes evaluables (ramas del poder, órganos autónomos, PQRSD, acciones constitucionales): usar `<details class="sb sb-{color}">` con summary, body, trampa CNSC y mini-pregunta tipo CNSC desplegable.

### Simulacro — formato CNSC real (JUICIO SITUACIONAL)
- **Tipo: juicio situacional.** Cada pregunta plantea un **caso/contexto** real del día a día del servidor y un enunciado tipo *"¿qué es lo más apropiado que debe hacer?"*. **NO se pregunta la norma de memoria** (nada de "¿qué dice la ley X?"); se evalúa **aplicar el criterio** a la situación, tal como en la prueba real de competencias de la CNSC.
- Las 4 opciones son **cursos de acción plausibles**; solo uno refleja la actuación correcta.
- **12 preguntas** total. Distribución: **4 básicas + 5 intermedias + 3 avanzadas**.
- **4 opciones (A, B, C, D)** — formato real CNSC. **NUNCA usar 3 opciones.**
- **Todas las preguntas llevan `ctx`** (el caso situacional).
- **Retroalimentación por opción** (`expl[i]`): explica por qué cada acción es correcta o incorrecta; **aquí sí se cita la norma** (artículo/ley) para reforzar el aprendizaje.
- **Cada pregunta tiene `tema`** para alimentar la lista de "Temas a reforzar" al final.
- **Respuestas correctas distribuidas sin patrón visible.**

### Botón "Avanzar"
Cada sección termina con una barra dorada con botón "Avanzar a {siguiente sección} →". La última sección dice "✅ Finalizar Día N" en verde.

---

## 4. Estructura del curso — CONGELADA

| Día | Código | Categoría |
|---|---|---|
| 1 | INTRO-00 | Bienvenida (genérica, ya creada) |
| 1 | INTRO-01 | Bienvenida personalizada (creada **bajo demanda** al comprar) |
| 2 | GEN-01 | Biblioteca General — Estado y Función Pública ✅ |
| 3 | GEN-02 | Biblioteca General — Relación Estado-Ciudadano ✅ |
| 4 | GEN-03 | Biblioteca General — Marco Institucional ✅ |
| 5–8 | varía | Biblioteca por Nivel (Asistencial / Técnico / Profesional) |
| 9–20 | varía | Biblioteca Funcional (según funciones del cargo) |
| 21 | SIM-001 | Simulacro Integral Final |

**Atención al numerar GEN:** GEN-01 = Día 2 (no Día 1). La introducción CNSC quedó **absorbida** dentro de INTRO-00.

> **Ubicación de las guías:** todas las guías HTML definitivas viven en la carpeta **`guias/`**. Referencian el favicon como `../brand/favicon.svg`. Las guías heredadas antiguas fueron retiradas del repo (su historial queda en los PRs).

### 4 bibliotecas
- **A) General** — fija para todos los clientes (3 GEN + INTRO-00)
- **B) Por Nivel** — depende del nivel jerárquico de la OPEC (competencias Dec. 815/2018)
- **C) Funcional** — depende de funciones específicas; reutilizable
- **D) Por Entidad** — creada bajo demanda y reutilizada (`ENT-001` Indervalle, etc.)

> **Registro maestro de guías:** la carpeta **`biblioteca/`** reemplaza al antiguo `BIBLIOTECA.xlsx`. La fuente de verdad es `biblioteca/biblioteca.json`; el índice legible `biblioteca/BIBLIOTECA.md` se regenera con `python3 biblioteca/generar_indice.py`. **Al crear o publicar una guía, registrarla en el JSON (estado + archivo + temas) y regenerar el índice.**

---

## 5. Reglas de trabajo

### Antes de tocar archivos
- **Siempre leer un archivo antes de modificarlo** — nunca proponer cambios a código sin verlo.
- Si el usuario menciona algo que ya hicimos en una conversación previa, validar con el repo (no asumir).
- Si falta información para una guía nueva, **preguntar** los 8 datos requeridos (ver §1 de `PLANTILLA-GUIA.md`). No inventar.

### Al crear/modificar guías
- Tomar `guias/GEN-01-estado-funcion-publica.html` como **base de referencia**: es la versión más completa y aprobada. (La vía rápida: copiarla, reemplazar metadata + contenido por sección + arrays JS; ver `PLANTILLA-GUIA.md` §4 Opción A.)
- Si una guía nueva supera ~80 KB, **crear el archivo vacío y agregar contenido por bloques** (`fs_write` inicial + `fs_append` sucesivos). Más confiable que un único `fs_write` gigante.
- Para ediciones puntuales en archivos existentes, usar **`str_replace`** (más estable que reescribir todo).
- **Validar después de cada cambio mayor:** etiquetas balanceadas, conteo de elementos, abrir mentalmente el flujo del usuario.

### Decisiones congeladas — NO MODIFICAR sin permiso explícito
1. Logo V2.
2. Paleta 60-30-10 (azul + dorado + crema).
3. Tipografías Source Serif 4 + Plus Jakarta Sans.
4. Simulacro **de juicio situacional**: 12 preguntas / 4 opciones / retroalimentación por opción / temas a reforzar. (Casos, no memoria de la norma.)
5. 11 secciones obligatorias.
6. Patrón 4 capas + sub-bloques.
7. Botón "Avanzar" al final de cada sección.
8. Numeración: INTRO-00 e INTRO-01 = Día 1; GEN-01 = Día 2; GEN-02 = Día 3; GEN-03 = Día 4.
9. Guías HTML autocontenidas (un solo archivo, abre en navegador, sin dependencia de internet salvo Google Fonts).

### Workflow Git
- **Nunca** push directo a `main`.
- Una rama por guía: `feat/gen-XX-nombre-corto`.
- Un PR por rama. Mensaje de commit en formato: `feat(GEN-XX): {descripción}`.
- Antes de un PR nuevo, ejecutar `github_list_pull_requests` para verificar que no haya uno abierto reutilizable.

### Comunicación con el usuario
- **Idioma del proyecto:** español (con tildes y ñ).
- Tono: directo, didáctico, sin tecnicismos innecesarios.
- Estructurar respuestas con encabezados, tablas y listas — el usuario procesa mejor en bloques.
- Cuando el usuario apruebe (`me gustó`, `seguimos`, `dale`), avanzar al siguiente paso sin reabrir lo aprobado.
- Cuando el usuario diga "no me gusta" o "no entiendo", reformular con ejemplo concreto antes de proponer cambio.

---

## 6. Anti-patrones a evitar

❌ Usar 3 opciones en el simulacro (es 4).
❌ Simulacro con preguntas de memoria de la norma ("¿qué dice la ley X?") — debe ser **juicio situacional** (un caso + "¿qué es lo más apropiado?").
❌ Capas de 1 línea (sensación "perdí mi dinero").
❌ Capas de 7+ párrafos (fatiga lectora).
❌ Cambiar la paleta `:root`.
❌ Quitar el slogan del header o footer.
❌ Conceptos sin norma/artículo explícitos.
❌ Casos abstractos sin nombres reales (siempre Indervalle, DIAN, SENA, etc.).
❌ Hacer un único `fs_write` gigantesco para guías extensas (falla por tamaño).
❌ Modificar archivos sin leerlos primero.
❌ Asumir contexto de chats anteriores sin validar el estado real del repo.

---

## 7. Cuando una sesión arranca

Al inicio de cualquier sesión sobre este repo:

1. **Leer estos 4 documentos** en este orden:
   - `.kiro/steering/proyecto-ascenso-publico.md` (este archivo, automático)
   - `ESTADO-PROYECTO.md` (visión completa)
   - `PLANTILLA-GUIA.md` (cómo crear guías)
   - `ESTANDAR-TECNICO.md` (código real)

2. **Verificar el estado real del repo:**
   - Listar ramas: `git branch -a`
   - Ver PRs abiertos: `github_list_pull_requests`
   - Ver últimos commits: `git log --oneline -10`

3. **Confirmar el estado entendido al usuario** antes de hacer cambios:
   - "Aquí estamos: GEN-01 y GEN-02 aprobadas, próxima es GEN-03..."

4. **Solo después** proponer próximos pasos.

---

## 8. Pendientes actuales (al 13 de junio de 2026)

### Estado de la Biblioteca General — ✅ COMPLETA
INTRO-00 + GEN-01 + GEN-02 + GEN-03 listas (Días 1–4). El módulo general está terminado.

### Próximo paso inmediato
- 🔜 **Biblioteca por Nivel (Día 5+)** — empezar por el nivel que se necesite (Asistencial / Técnico / Profesional).

### En cola (orden de prioridad)
1. 4 guías Nivel Técnico (TEC-COM-01/02, TEC-ESP-01/02).
2. 4 guías Nivel Asistencial (ASI-COM-01/02, ASI-ESP-01/02).
3. 4 guías Nivel Profesional (PRO-COM-01/02, PRO-ESP-01/02).
4. Generador de Guías (prompt) — desbloquea creación masiva de guías funcionales.
5. SIM-001 — Simulacro Integral Final.
6. Plataforma web (landing, registro, panel estudiante, panel admin).

### Decisiones operativas pendientes
- ¿12 h o más para entregar el curso después de la compra?
- ¿60 días o más de acceso al material?
- Distribución del simulacro final SIM-001 según nivel de la vacante.

---

*Steering activo. Si una nueva sesión necesita más contexto, leer los 4 documentos de referencia.*

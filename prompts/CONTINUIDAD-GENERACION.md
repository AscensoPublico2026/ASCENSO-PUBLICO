# 🏗️ Continuidad — GENERACIÓN DE CURSOS (plan + guías)

> **Cuándo usar este documento:** cuando entra una venta (o vas a preparar un cargo nuevo)
> y necesitas **generar el plan de estudio y las guías** de ese cargo, montarlas y dejar
> el curso listo en el perfil del estudiante.

---

## 🟢 PROMPT PARA PEGAR EN UNA SESIÓN NUEVA DE KIRO

Copia y pega esto tal cual al iniciar sesión (con el repo `ascensopublico2026/ASCENSO-PUBLICO` conectado):

```
Hola Kiro. Vamos a GENERAR EL CURSO de un cargo nuevo para Ascenso Público.
Primero lee, en este orden:
1. CONTINUIDAD.md (estado del proyecto)
2. prompts/CONTINUIDAD-GENERACION.md (este flujo)
3. prompts/generador-plan-estudio.md y prompts/generador-guias.md (los generadores)
4. ESTANDAR-TECNICO.md y PLANTILLA-GUIA.md (estándar de las guías)

Datos del cargo que vamos a preparar:
- OPEC:
- Entidad:
- Cargo y nivel:
- Manual de funciones: (lo pego o lo adjunto)

Quiero que: (1) generes el PLAN DE 21 DÍAS marcando qué guías REUSAR y cuáles CREAR,
(2) generes las guías nuevas con el motor (JSON de contenido), (3) me indiques cómo
montarlas a la biblioteca y cargarlas en el perfil del estudiante según el plan.
No empieces a escribir guías hasta que aprobemos el plan.
```

---

## 🔁 EL FLUJO PASO A PASO (la "sección de generación")

Esta es la **sección de generación** del proyecto. Cada vez que entra un cargo nuevo, se repite:

### 1) Generar el PLAN de estudio
- Insumos: **OPEC + manual de funciones + nivel**.
- Con `prompts/generador-plan-estudio.md` (v3) → produce la **tabla del plan de 21 días** con columna **Estado** (✅ Reusar / 🆕 Crear) y las **fichas de contenido** de cada guía a crear.
- **Regla del plan:** 20 días de estudio (lunes a viernes) + 1 simulacro final = 21. Estructura: Día 1 (Intro + "Conoce tu Entidad") → Generales → Competencias por nivel → 12 funcionales del cargo → Simulacro.
- ⛔ No avanzar a crear guías hasta aprobar el plan.

### 2) Reusar lo que ya existe
- Revisar la biblioteca (`biblioteca/biblioteca.json`) y los cursos previos del **mismo OPEC**.
- Genéricas (INTRO, GEN, nivel, BON) casi siempre se **reusan**. Las **funcionales** y "Conoce tu Entidad" suelen ser propias del cargo/entidad.

### 3) Crear SOLO las guías que faltan
- Con `prompts/generador-guias.md` (v2.1) + el **motor** (`motor/base-guia.html` + `motor/construir_guia.py`).
- La IA llena un **JSON de contenido** en `motor/contenido/<CODIGO>.json` (NO escribe el HTML enorme); el script arma el HTML con el diseño congelado. Así el diseño nunca se rompe.
- Generar simulacro con `simulacro/motor/` + `simulacro/bancos/` (receta en `simulacro/contenido/<CODIGO>.json`): se reusan los bancos (generales, nivel, ofimática, funcionales-comunes) y se escriben solo las funcionales del cargo.

### 4) Registrar en la biblioteca
- Guardar el HTML en `guias/` (y simulacro en `simulacro/SIM-NNN.html`).
- Registrar la guía en `biblioteca/biblioteca.json` (estado `publicada`, `archivo`).
- Correr `scripts/sync-biblioteca.sh` (copia catálogo + HTML a `plataforma/public/seed-guias/` y a `plataforma/lib/biblioteca.json`).
- La auto-sanación del visor sube el HTML al bucket la primera vez que se abre (ya NO hay que correr `/api/admin/seed-guias` a mano).

### 5) Cargar el curso en el perfil del estudiante
- En `/admin/cursos/[id]`: las genéricas y de nivel se auto-cargan; **asignar por código** desde los desplegables: "Conoce tu Entidad" (ENT-), funcionales (x/12) y el simulacro (SIM-).
- **Atajo por OPEC:** si ya existe otro curso del mismo OPEC con el plan armado, aparece el banner **"✅ Este OPEC ya fue preparado antes → Generar curso automáticamente"** (copia funcionales + entidad + simulacro sin duplicar).
- Revisar con **"👁️ Previsualizar"** y luego **"Curso listo (12h)"** o **"Habilitar ahora"** (el cliente recibe correo al habilitarse).

### 6) Otro cliente → repetir
- Cargo nuevo → desde el paso 1. Mismo OPEC ya preparado → paso 5 (atajo por OPEC).

---

## 📌 Notas importantes
- **El "generador" hoy es la IA (Kiro/Claude) trabajando en sesión contigo**, apoyada en el motor + prompts. NO hay aún una API de IA conectada que genere sola al recibir la compra (eso es la Fase de automatización futura; ver §9.5 de CONTINUIDAD.md).
- Ventana de tiempo: el cliente tiene el curso "en preparación" hasta 12h (o hasta que des "Habilitar ahora"), y el **simulacro queda bloqueado** hasta que termine las guías del plan → margen para construir.
- **Idea/biblioteca propia:** ir creando guías de temas comunes en tiempos libres amplía la biblioteca y acelera futuros cargos que compartan temas.
- **Marca y estándar:** navy `#0A2A5E`, crema `#FBF9F4`, oro `#E8A33D`. No inventar datos/cifras. Diseño de guías congelado en el motor.

> Al terminar de generar un curso, **actualiza CONTINUIDAD.md** con el cargo/OPEC preparado.

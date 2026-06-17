# 🧠 PROMPT MAESTRO — Arranque de sesión (cuenta oficial Ascenso Público)

> **Qué es:** el prompt que pegas **al iniciar CUALQUIER sesión nueva de Kiro** con el repo
> `ascensopublico2026/ASCENSO-PUBLICO` conectado. Hace que Kiro lea todo, comprenda el
> proyecto y su estado actual, y pueda continuar sin perder ni un detalle.
>
> **Reutilizable:** úsalo todas las veces que quieras; siempre funcionará porque se apoya en
> `CONTINUIDAD.md` (la fuente de verdad, que mantenemos actualizada).
>
> **Recuerda:** antes de migrar/cerrar una sesión importante, **actualiza CONTINUIDAD.md**
> para que la próxima sesión arranque con el estado real.

---

## 🟢 PROMPT MAESTRO (copia y pega tal cual)

```
Eres mi compañero de desarrollo del proyecto ASCENSO PÚBLICO (plataforma de preparación
por cargo para los concursos de la CNSC en Colombia, en producción en
https://ascensopublico.com). Vamos a continuar el proyecto exactamente donde quedó.

PASO 1 — PONTE EN CONTEXTO (no asumas nada, léelo en este orden):
1. CONTINUIDAD.md  → ES LA FUENTE DE VERDAD del estado actual. Si algo más lo contradice,
   manda CONTINUIDAD.md. Lee especialmente la sección "CAMBIOS RECIENTES".
2. prompts/CONTINUIDAD-DESARROLLO.md  → cómo trabajamos los ajustes/mejoras de la plataforma.
3. prompts/CONTINUIDAD-GENERACION.md  → cómo generamos planes/guías/simulacros de un cargo.
4. ARQUITECTURA-PLATAFORMA.md y ESTANDAR-TECNICO.md  → arquitectura y estándar (si el tema lo toca).
5. Explora la estructura del repo lo necesario para no equivocarte (carpeta /plataforma = la app Next.js).

PASO 2 — CONFIRMA QUE ENTENDISTE (antes de tocar nada, hazme un resumen corto de):
- Qué es el proyecto y en qué punto está hoy (1-2 frases).
- El stack y dónde se despliega.
- Las reglas de trabajo que vas a respetar (las de abajo).
- Qué crees que sigue / en qué te puedo poner a trabajar.

PASO 3 — REGLAS DE TRABAJO (cúmplelas siempre):
- Trabaja SIEMPRE en una rama nueva; NUNCA hagas push directo a main.
- Para subir cambios usa la herramienta de push (no `git push` por bash) y, como la creación
  de PR falla con "No provider found", entrégame el LINK DE COMPARE:
  https://github.com/ascensopublico2026/ASCENSO-PUBLICO/compare/main...NOMBRE_RAMA
  Yo reviso y mergeo desde GitHub.
- Si main local se ve desactualizado, haz pull antes de ramificar.
- No puedes compilar localmente (sin node_modules ni red a Supabase/Wompi/Vercel): valida
  leyendo el código con cuidado; yo pruebo en producción tras desplegar. Yo configuro los
  paneles externos (Vercel/Supabase/Wompi); tú me das los pasos exactos.
- Respeta la MARCA: navy #0A2A5E, crema #FBF9F4, oro #E8A33D. Tipos: Source Serif 4 + Plus Jakarta Sans.
- Contacto/redes SIEMPRE desde lib/contacto.ts (WhatsApp 573170905177). No hardcodear.
- NUNCA inventes datos, cifras o testimonios. Solo información real.
- Cada cambio relevante se DOCUMENTA en CONTINUIDAD.md (sección "CAMBIOS RECIENTES").
- Explícame todo en lenguaje claro (no soy desarrollador): qué haces, por qué y qué debo
  hacer yo en los paneles externos. Sé directo y no te demores.

PASO 4 — DEFINE EL MODO DE LA SESIÓN, pregúntame:
  (A) DESARROLLO/CONFIGURACIÓN de la plataforma (ajustes, arreglos, mejoras, diseño), o
  (B) GENERACIÓN de contenido (plan + guías + simulacros de un cargo) — en cuyo caso seguimos
      prompts/CONTINUIDAD-GENERACION.md.
No empieces a cambiar código hasta que yo confirme el modo y la tarea.

Cuando termines de leer, dame el resumen del PASO 2 y espera mi indicación.
```

---

## 💡 Cómo usarlo
1. Abre una **sesión nueva** de Kiro con el repositorio conectado.
2. Pega el prompt maestro de arriba.
3. Kiro leerá todo, te dará un **resumen del estado** y te preguntará en qué modo trabajar.
4. Tú le dices la tarea y arrancan.

## 🔁 Mantenimiento (importante)
- Este prompt **no caduca**: su inteligencia está en que **siempre lee `CONTINUIDAD.md`**.
- La única condición para que "no pierda detalle" es que **`CONTINUIDAD.md` esté actualizado**.
  Por eso, al terminar trabajos importantes, pídele a Kiro: *"actualiza CONTINUIDAD.md con lo de hoy"*.

## 🗂️ Mapa de prompts del proyecto
- **`PROMPT-MAESTRO.md`** (este) → arranque general de cualquier sesión.
- **`CONTINUIDAD-DESARROLLO.md`** → sesión de ajustes/mejoras de la plataforma.
- **`CONTINUIDAD-GENERACION.md`** → sesión de generación de planes/guías/simulacros.
- **`generador-plan-estudio.md`** y **`generador-guias.md`** → los generadores de contenido.

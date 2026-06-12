# Ascenso Público — Estado del Proyecto

> **Documento maestro de respaldo.** Permite retomar el proyecto desde cero si todo lo demás se pierde.
>
> **Última actualización:** 12 de junio de 2026
> **Mantenedor:** César Deávila
> **Repositorio:** [CesarDeavila1126/ASCENSO-PUBLICO](https://github.com/CesarDeavila1126/ASCENSO-PUBLICO)

---

## 1. Visión y propósito

**Ascenso Público** es una plataforma de cursos personalizados para aspirantes a concursos públicos de la **CNSC (Comisión Nacional del Servicio Civil)** en Colombia.

**Promesa de valor:** El cliente compra un curso totalmente adaptado a la vacante (OPEC) en la que está concursando — no un curso genérico. En menos de 12 horas recibe un plan de estudio de 21 días con guías HTML interactivas y un simulacro final, listo para estudiar.

**Slogan:** *Tu ruta personalizada al ascenso público.*

---

## 2. Alcance del producto

### Lo que SÍ hace
- Vende cursos preparatorios CNSC personalizados por vacante.
- Genera plan de estudio automatizado de 21 días basado en el manual de funciones de la vacante.
- Combina 4 bibliotecas de guías reutilizables para escalar sin reproducir trabajo.
- Entrega contenido interactivo (HTML autocontenido) que abre en cualquier navegador.
- Incluye simulacros idénticos al formato real CNSC.

### Lo que NO hace (fuera de alcance v1)
- No reemplaza la prueba oficial.
- No emite certificados oficiales.
- No tiene mentoría 1:1 (al menos no en MVP).
- No cubre pruebas psicotécnicas en profundidad (sólo conocimientos).

---

## 3. Flujo de negocio (cliente)

```
1. Cliente entra a la landing page de Ascenso Público
2. Lee la introducción al concepto y al método
3. Selecciona el proceso de selección de su interés
4. Encuentra info del proceso + plan de estudio resumido
5. Decide comprar
6. Se registra: nombre completo, correo, celular
7. Ingresa datos de la oferta:
   - Número de OPEC
   - Nombre de OPEC
   - Nivel jerárquico
   - Adjunta manual de funciones (PDF)
8. Realiza la compra
9. Recibe correo de confirmación
10. Entra a su perfil → ve su curso ("Técnico Almacenista – Indervalle")
    + barra de progreso (cuenta regresiva de las ~12 h)
11. Ascenso Público (admin) recibe notificación con todos los datos
12. ADMIN genera el curso (ver §4)
13. Antes de las 12 h, el cliente recibe el curso completo
14. Estudia 1 guía por día durante 20 días + simulacro día 21
15. Tiene acceso al material por 60 días (a confirmar duración final)
```

---

## 4. Flujo de generación del curso (admin / Ascenso Público)

```
1. Recibo la compra → tengo OPEC + manual de funciones
2. Ejecuto el "Generador de Plan de Estudio" (prompt ya diseñado v1.1):
   • Input: manual de funciones + datos de la vacante
   • Output: plan de 21 días con temario detallado
3. El generador SIEMPRE incluye:
   a) Biblioteca General (aplica a todos los cargos) — guías ya creadas
   b) Biblioteca por Nivel (Asistencial / Técnico / Profesional)
   c) Biblioteca Funcional (depende de las funciones del cargo)
   d) Biblioteca por Entidad (creada bajo demanda y reutilizada)
4. El generador lee un Excel con todas las guías ya existentes
   y, si una guía funcional ya fue creada antes, devuelve su CÓDIGO
   en vez de pedir que la generemos otra vez (reutilización).
5. Para los temas funcionales que NO existen aún:
   - Tomo el tema → lo paso al "Generador de Guías" (PENDIENTE crearlo)
   - Recibo la guía HTML lista
6. Ordeno todas las guías por día y se las cargo al perfil del cliente
7. A las 12 h después de la compra → cliente tiene acceso completo
```

---

## 5. Identidad visual (CONGELADA)

### Logo oficial
**Concepto:** Flecha de impulso con estela (V2) — elegida tras descartar opciones más institucionales y otras más infantiles. Comunica ascenso/despegue, funciona en TikTok, en favicon, y en headers formales.

**Variantes (todas en `/brand/`):**
- `logo-ascenso-publico.svg` → para guías y header (cuadrado dorado + flecha azul)
- `logo-ascenso-publico-navy.svg` → fondos claros (cuadrado azul + flecha dorada)
- `logo-ascenso-publico-tiktok.svg` → redes sociales (azul + flecha amarillo vibrante + estela menta)
- `favicon.svg` → pestaña del navegador

### Paleta — Regla 60-30-10 (basada en estudios de UX educativo)

| % | Color | Hex | Uso |
|---|---|---|---|
| 60 | Crema cálido | `#FBF9F4` | Fondo (menos fatiga visual que blanco puro) |
| 30 | Azul institucional | `#0A2A5E` | Headers, títulos, navegación |
| 10 | Dorado cálido | `#E8A33D` | Acentos, CTAs, resaltados |

**Colores semánticos** (consistentes en toda guía):
- Verde `#1F9D6E` → correcto / tip
- Rojo `#D43A3A` → error
- Ámbar `#F5B940` → advertencia
- Azul `#3B82F6` → info

### Tipografía
- **Títulos:** `'Poppins', sans-serif` — 600/700, legible y moderna
- **Texto:** `'Inter', sans-serif` — 400/500, óptima para lectura larga
- Importadas de Google Fonts dentro de cada guía (sin necesidad de internet tras cargar)

### Estilo
- **Cálido + profesional**, no "arcoíris" ni "corporativo aburrido".
- Emojis distintivos por concepto (no decorativos: ayudan a memorizar).
- Componentes con bordes redondeados (12-16 px), sombras sutiles.
- Sin animaciones excesivas: solo hover suave (translateY 2px) en cards.

---

## 6. Estándar de calidad (CONGELADO)

Documento base oficial: `ESTÁNDAR DE CALIDAD OFICIAL.docx` (versión AP-QA-001 v1.1, en el repo).

### 6.1 Tiempo objetivo por guía
**75–110 minutos** de estudio efectivo.
- 75–90 min para guías estándar.
- 90–110 min para guías con sub-bloques profundos (concepto madre + sub-componentes evaluables).

### 6.2 Estructura obligatoria — 11 secciones

| # | Sección | Propósito | Tiempo aprox. |
|---|---|---|---|
| 1 | 🎯 Objetivo | Qué va a aprender el estudiante | ~2 min |
| 2 | ⭐ Importancia | Por qué este día vale invertir tiempo | ~3 min |
| 3 | 📖 Desarrollo | Conceptos clave en **4 capas** + sub-bloques | 25–40 min |
| 4 | ⚖️ Comparaciones | Tablas que diferencian conceptos similares | 10–15 min |
| 5 | 📂 Casos | 5 casos aplicados tipo CNSC | 10–15 min |
| 6 | ⚠️ Errores | 6 errores frecuentes a evitar | ~5 min |
| 7 | 💡 Tips | 6 atajos de estudio / mnemotecnia | ~5 min |
| 8 | 🎭 Trampas | 4 trampas típicas de la prueba CNSC | ~5 min |
| 9 | 🧠 Repaso | 10 flashcards interactivas | ~5 min |
| 10 | 📝 Resumen + Glosario | 6 cards clave + 6 términos | ~3 min |
| 11 | 🎓 Simulacro | 12 preguntas formato CNSC real | 15–20 min |

### 6.3 Las "4 capas" por concepto (fórmula de contenido)

Cada concepto importante del Desarrollo se presenta así:

```
🟦 DEFINICIÓN — qué es exactamente (con norma/artículo si aplica)
🟩 APLICACIÓN — para qué sirve, cómo opera en la práctica
🟨 EJEMPLO — caso real verificable (entidad, OPEC, etc.)
🟥 CÓMO LO EVALÚA LA CNSC — cómo aparece en la prueba real
```

**Regla de longitud:** 2 a 4 párrafos cortos por capa, con datos verificables (norma, artículo, caso real). Ni muy corto (sensación "perdí mi dinero") ni muy largo (fatiga lectora).

### 6.4 Patrón "Concepto madre + sub-bloques desplegables"

Cuando un concepto tiene sub-componentes evaluables (ej. las 3 ramas, los 4 grupos de órganos autónomos, los 7 principios del art. 209), se usa:

```
🏛️ CONCEPTO MADRE (intro corta + 4 capas generales)
   ├── 📜 Sub-bloque 1
   │      • Quién/qué lo conforma (con nombres concretos)
   │      • Funciones específicas (verbos clave que la CNSC usa)
   │      • Diferencias nacional vs territorial (si aplica)
   │      • ⚠️ Trampa CNSC típica de ESTE sub-bloque
   │      • 🎯 Mini-pregunta tipo CNSC desplegable
   ├── Sub-bloque 2 (igual estructura)
   └── Sub-bloque 3 (igual estructura)
```

### 6.5 Simulacro — formato CNSC real

| Parámetro | Valor | Notas |
|---|---|---|
| Tipo | Selección múltiple única respuesta | Formato oficial CNSC |
| Opciones | 4 (A, B, C, D) | **Confirmado tras investigación**, anula la versión inicial de 3 opciones del estándar v1.1 |
| Cantidad | 12 preguntas | 4 básicas + 5 intermedias + 3 avanzadas |
| Distribución de respuestas | Sin patrón visible | Ej. B,C,A,D,B,D,C,B,D,C,A,B |
| Retroalimentación inmediata | Sí, por cada opción | Por qué la suya está mal + por qué la correcta es correcta |
| Resultado final | Puntaje + Lista de **temas a reforzar** | Según preguntas falladas |

### 6.6 Botón "Avanzar" al final de cada sección

Cada una de las 11 secciones termina con una barra dorada:

> *¿Listo para continuar?* **[Avanzar a {siguiente sección} →]**

Última sección (Simulacro) cambia a verde:

> *Has completado todo el contenido* **[🎓 Finalizar Día X]**

---

## 7. Estructura del curso (21 días)

### Resumen del cronograma

| Día | Código | Guía | Categoría |
|---|---|---|---|
| 1 | INTRO-00 | Introducción a Ascenso Público y CNSC | Bienvenida (genérica) |
| 1 | INTRO-01 | Introducción a la Entidad | Bienvenida (personalizada por vacante) |
| 2 | GEN-01 | Estado y Función Pública | Biblioteca General |
| 3 | GEN-02 | Relación Estado-Ciudadano | Biblioteca General |
| 4 | GEN-03 | Marco Institucional | Biblioteca General |
| 5–8 | (varía) | Guías por Nivel (Asistencial/Técnico/Profesional) | Biblioteca por Nivel |
| 9–20 | (varía) | Guías Funcionales (según funciones del cargo) | Biblioteca Funcional |
| 21 | SIM-001 | Simulacro Integral Final | Evaluación final |

> **Nota crítica:** INTRO-00 e INTRO-01 son del Día 1 y NO consumen códigos GEN. Por eso GEN-01/02/03 (que antes era 02/03/04) están corridos un día. La Introducción CNSC quedó **absorbida** dentro de INTRO-00.

### Las 4 bibliotecas

#### A) Biblioteca General — fija para todos los clientes
3 guías GEN (Estado, Relación con Ciudadano, Marco Institucional) + INTRO-00 (presentación). Misma para cualquier cargo.

#### B) Biblioteca por Nivel — depende del nivel jerárquico de la OPEC
- **Asistencial:** ASI-COM-01, ASI-COM-02, ASI-ESP-01, ASI-ESP-02
- **Técnico:** TEC-COM-01, TEC-COM-02, TEC-ESP-01, TEC-ESP-02
- **Profesional:** PRO-COM-01, PRO-COM-02, PRO-ESP-01, PRO-ESP-02

#### C) Biblioteca Funcional — depende de las funciones específicas del cargo
- Códigos `FUN-001`, `FUN-002`, etc.
- Se consulta el Excel `BIBLIOTECA.xlsx`: si la guía existe, se reutiliza; si no, se crea con el "Generador de Guías" y se almacena para próximos clientes.
- Esta es la categoría que más crece con el tiempo.

#### D) Biblioteca por Entidad — creada bajo demanda
- Códigos `ENT-001` (Indervalle), `ENT-002` (DIAN), etc.
- Cubre: misión, sector, estructura orgánica básica, contexto para la prueba.
- **NO duplica** las guías funcionales (esas siguen siendo del cargo).
- También se reutiliza: si llega otro cliente de la misma entidad, ya existe.

---

## 8. Inventario actual del repositorio

### Archivos fundacionales (no se modifican)
| Archivo | Contenido |
|---|---|
| `Fundacional de Ascenso Público V1..docx` | Visión, flujo, filosofía |
| `ESTÁNDAR DE CALIDAD OFICIAL.docx` | Estándar AP-QA-001 v1.1 |
| `PRONT GENERADOR DE PLANES 1.1.docx` | Prompt del generador de planes |
| `BIBLIOTECA.xlsx` | Excel maestro con 3 hojas (códigos por categoría) |

### Plantilla maestra y guías nuevas (rama `feat/guia-gen-01`, [PR #1](https://github.com/CesarDeavila1126/ASCENSO-PUBLICO/pull/1))
| Archivo | Descripción | Estado |
|---|---|---|
| `INTRO-00-presentacion-curso.html` | Plantilla maestra congelada (logo + diseño) | ✅ Lista |
| `GEN-01-estado-funcion-publica.html` | Día 2 — Estado y Función Pública (versión robusta) | ✅ Lista (base) |
| `brand/logo-ascenso-publico.svg` | Logo principal (guías) | ✅ |
| `brand/logo-ascenso-publico-navy.svg` | Logo para fondos claros | ✅ |
| `brand/logo-ascenso-publico-tiktok.svg` | Logo para redes/TikTok | ✅ |
| `brand/favicon.svg` | Favicon | ✅ |

### GEN-01 con profundización "Tres Ramas" (rama `feat/gen-01-profundizacion`, [PR #2](https://github.com/CesarDeavila1126/ASCENSO-PUBLICO/pull/2))
| Archivo | Descripción |
|---|---|
| `GEN-01-estado-funcion-publica.html` | Versión final aprobada con sub-bloques desplegables, mini-preguntas tipo CNSC, +20% profundidad |

> ✅ **Versión vigente de GEN-01.** Incluye sub-bloques de las 3 ramas, los 4 grupos de órganos autónomos y mini-preguntas en los 3 tipos de servidor público.

### GEN-02 (rama `feat/gen-02-relacion-ciudadano`, [PR #3](https://github.com/CesarDeavila1126/ASCENSO-PUBLICO/pull/3))
| Archivo | Descripción | Estado |
|---|---|---|
| `GEN-02-relacion-estado-ciudadano.html` | Día 3 — Derecho de petición, PQRSD, acciones constitucionales, habeas data | ✅ Aprobada |

### Guías heredadas (anteriores al estándar nuevo)
17 archivos `.html` con la nomenclatura antigua. **No siguen** la plantilla maestra ni la paleta congelada. Quedan como referencia/contenido a migrar:

- `guia-constitucion-cnsc.html`
- `guia-funcion-publica-cnsc.html`
- `guia-atencion-ciudadano-pqrsd-cnsc.html`
- `guia-gestion-documental-cnsc.html`
- `guia-gtc185-competencias-cnsc.html`
- `guia_indervalle_cnsc_opec243477.html`
- `guia_almacen_indervalle_modulo2.html`
- `guia_recepcion_bienes_modulo3.html`
- `guia_codificacion_unspsc_modulo4.html`
- `guia_kardex_valoracion_modulo5.html`
- `guia_inventario_fisico_conciliacion_kardex_indervalle.html`
- `guia_cnsc_software_inventarios.html`
- `guia_supervision_contratos_apoyo_tecnico_indervalle.html`
- `guia_gestion_documental_modulo7.html`
- `guia_cnsc_decreto815_semana1.html`
- `guia_decreto815_OR_AC_modulo_avanzado.html`
- `guia_decreto815_comportamental_modulo6.html`

---

## 9. Decisiones congeladas (no negociables sin revisión explícita)

1. **Logo oficial:** V2 (flecha con impulso). No volver a explorar opciones.
2. **Paleta:** Crema 60 + Azul institucional 30 + Dorado 10. Solo los 4 semánticos adicionales.
3. **Simulacro CNSC:** 12 preguntas, 4 opciones (A–D), retroalimentación por opción + temas a reforzar.
4. **Tiempo por guía:** 75–110 min.
5. **Estructura del Día 1:** INTRO-00 + INTRO-01 (esta última bajo demanda al comprar).
6. **Numeración GEN:** GEN-01 = Día 2, GEN-02 = Día 3, GEN-03 = Día 4 (corrida tras absorber Introducción CNSC en INTRO-00).
7. **Patrón profundo:** Concepto madre + sub-bloques desplegables con mini-pregunta CNSC.
8. **Botón "Avanzar"** al final de cada sección.
9. **Guías HTML autocontenidas:** Un solo archivo, abre en cualquier navegador, sin dependencia de internet (salvo Google Fonts en primera carga).

---

## 10. Pendientes (en orden de prioridad)

### Fase 1 — Completar el motor de contenido
- [ ] **GEN-03** · Marco Institucional (Día 4) — Próxima en cola
- [ ] **Generador de Guías** (prompt) — desbloquea creación masiva de guías funcionales

### Fase 2 — Biblioteca por Nivel
- [ ] 4 guías Nivel Técnico (TEC-COM-01/02, TEC-ESP-01/02)
- [ ] 4 guías Nivel Asistencial (ASI-COM-01/02, ASI-ESP-01/02)
- [ ] 4 guías Nivel Profesional (PRO-COM-01/02, PRO-ESP-01/02)

### Fase 3 — Simulacro y bonus
- [ ] SIM-001 · Simulacro Integral Final (150 preguntas)
- [ ] BON-01 · Estrategia CNSC (bonus)

### Fase 4 — Plataforma web
- [ ] Landing page
- [ ] Sistema de registro y compra
- [ ] Panel del estudiante (perfil, barra de progreso, guías por día)
- [ ] Panel admin (recibir compras, generar/cargar curso, notificaciones)

### Decisiones operativas pendientes
- [ ] Confirmar tiempo de entrega: ¿12 h o más?
- [ ] Confirmar duración del acceso: ¿60 días o más?
- [ ] Definir distribución de preguntas en el simulacro final SIM-001 según nivel.

---

## 11. Cómo retomar el proyecto si todo falla

Si por cualquier motivo se pierde el chat, el agente, o partes del repo, sigue estos pasos:

### Paso 1 — Recuperar el repo
```bash
git clone https://github.com/CesarDeavila1126/ASCENSO-PUBLICO.git
cd ASCENSO-PUBLICO
```

### Paso 2 — Identificar las ramas de trabajo
- `main` — base original (guías heredadas, sin plantilla nueva)
- `feat/guia-gen-01` — plantilla maestra + INTRO-00 + GEN-01 base + `/brand/`
- `feat/gen-01-profundizacion` — **GEN-01 final aprobada** (con sub-bloques)
- `feat/gen-02-relacion-ciudadano` — **GEN-02 final aprobada**

### Paso 3 — Leer estos 4 documentos en orden
1. `ESTADO-PROYECTO.md` (este archivo) — visión completa
2. `ESTANDAR-TECNICO.md` — código CSS/HTML/JS de los componentes
3. `PLANTILLA-GUIA.md` — checklist para crear cualquier guía nueva
4. `.kiro/steering/proyecto-ascenso-publico.md` — reglas para el agente AI

### Paso 4 — Si necesitas reconstruir una guía desde cero
- Toma `INTRO-00-presentacion-curso.html` o `GEN-01-estado-funcion-publica.html` (PR #2) como base.
- Sigue `PLANTILLA-GUIA.md`.
- Respeta las decisiones congeladas (§9 de este documento).

### Paso 5 — Si necesitas continuar el desarrollo
- Empezar por la próxima guía de `§10 — Pendientes` (hoy: GEN-03).
- Iniciar nueva sesión de Kiro con este documento como referencia.
- El steering en `.kiro/steering/` se carga automáticamente.

---

## 12. Aprendizajes y observaciones

### Lo que funcionó muy bien
- **Plantilla maestra una sola vez:** Pulir INTRO-00 al máximo y replicar evita rediseñar cada guía.
- **Iterar en colaboración:** Cada decisión grande (logo, colores, profundidad) se validó con el cliente antes de avanzar.
- **Investigación CNSC real:** Confirmar el formato de 4 opciones (A-D) hizo los simulacros creíbles.
- **Contenido en 4 capas:** Da profundidad sin saturar.

### Lecciones aprendidas
- Las guías iniciales eran muy cortas. La regla de **2-4 párrafos por capa** con norma + ejemplo + cómo evalúa CNSC resolvió la sensación "perdí mi dinero".
- Los **sub-bloques desplegables** son indispensables para temas con sub-componentes (ramas, órganos, tipos de servidor).
- **Crear archivos extensos por bloques** (write inicial + appends sucesivos) es más confiable que un solo write gigante.

### Anti-patrones a evitar
- ❌ Logos demasiado infantiles para TikTok que no funcionan en guías formales.
- ❌ "Arcoíris" de colores: máximo 3 colores principales + semánticos.
- ❌ Conceptos en 1-2 líneas (sensación de "info de Wikipedia").
- ❌ Simulacros con 3 opciones (no es el formato CNSC real).
- ❌ Modificar archivos extensos con un único `fs_write`: usar `str_replace` o append por bloques.

---

*Fin del documento maestro. Para detalles técnicos consultar `ESTANDAR-TECNICO.md` y `PLANTILLA-GUIA.md`.*

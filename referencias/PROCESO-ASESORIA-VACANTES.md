# 🧭 PROCESO TÉCNICO — Asesoría e identificación de vacantes PGN 2026 (Ascenso Público)

> Método afinado y aprobado por Julio César (fundador). Operado también por Laurita (su esposa).
> Complementa a `PROMPT-ASESORIA-VACANTES.md` (prompt maestro original). Caso de referencia
> aprobado: **juan-sebastian-insuasty** (ver su `expediente.md`).
> Repo: `AscensoPublico2026/ASCENSO-PUBLICO`. Rama de trabajo: `main`.

---

## 🎯 Objetivo
Para cada aspirante: leer su documentación al 100%, construir su perfil, y encontrar las vacantes de
la PGN que **realmente cumple**, entregando al final material listo para WhatsApp (tabla + guiones de
nota de voz + textos por manual).

## 👥 Roles / nombres (no confundir)
- **Julio César** — fundador/cliente. **Laurita** — su esposa, opera esta sección.
- **Juan Gómez** — nombre con el que el asesor se presenta ante el aspirante en WhatsApp.
- **Aspirante/estudiante** — el destinatario del servicio (cambia en cada caso).

## 📁 Estructura por aspirante
```
referencias/expedientes/<nombre-con-guiones>/
├── documentos/          (PDF del aspirante)
├── manuales-vacantes/   (manuales de funciones de las convocatorias elegidas)
└── expediente.md        (perfil + análisis + tabla de opciones + cruce de manuales)
```
Nombre de carpeta: minúsculas y guiones (ej. "María Fernanda Ruiz" → `maria-fernanda-ruiz`).

---

## 🔄 LOS 7 PASOS

### PASO 1 — Recepción del aspirante
El operador da nombre + lo que respondió el aspirante (profesión, estudios, ciudad, salario mínimo de
aspiración, disposición a mudarse y ciudades, concursos previos, nivel de interés).

### PASO 2 — Crear expediente y dar enlace de carga
- Crear carpeta con las dos subcarpetas (`documentos/`, `manuales-vacantes/`), cada una con un `LEEME.md`.
- Crear `expediente.md` con los datos preliminares.
- Commit + push a `main`.
- Entregar enlace de subida directo:
  `https://github.com/AscensoPublico2026/ASCENSO-PUBLICO/upload/main/referencias/expedientes/<nombre>/documentos`
- **Importante (mejora del cliente):** el operador NO hace merge ni pasos extra; sube al enlace y avisa.

### PASO 3 — Operador carga documentos y avisa
Al recibir "ya cargué la documentación": `git pull origin main`.

### PASO 4 — Lectura exhaustiva + perfil
- Extraer texto con **pdfplumber**; toda página escaneada/ilegible → **renderizar a imagen (PyMuPDF, <5 MB)
  y leerla como imagen**. Nunca declarar "falta X" sin ver la imagen.
- Detectar y descartar duplicados (comparar md5).
- **Experiencia:** contar solo desde la fecha del título; unir intervalos traslapados (sin doble conteo).
  Distinguir escenario conservador (solo lo certificado en mano) vs. real (incluye vínculos vigentes que
  el aspirante confirme y vaya a certificar). Documentar ambos si aplica.
- Entregar: perfil + **tabla de análisis de documentación** (✅ está / ⚠️ falta / 🔧 corregir).
- Guardar todo en `expediente.md`. Commit + push.

### PASO 5 — Análisis de vacantes (matriz)
- Leer `Convocatorias_Procuraduria.xlsx` con **openpyxl** (18 columnas; ver prompt maestro).
- Filtrar por: requisito de estudio que acepte su profesión, posgrado si aplica, experiencia real,
  y ciudades/departamentos de interés. Salario ≥ aspiración del aspirante.
- Entregar **tabla ordenada de menor a mayor salario** desde su aspiración, escalando hasta el tope que cumple.
  Columnas: Código · Cargo (Grado) · Nivel · Salario · Plazas · Proceso · Ciudades de su interés.
- Lectura estratégica honesta (más plazas = más probabilidad, pero con matiz; posgrado como diferenciador).
- Indicar de qué convocatorias pedir el manual. Commit + push.

### PASO 6 — Manuales (PRIMERO revisar la biblioteca central)
- **ANTES de pedir manuales**, revisar la biblioteca central `referencias/manuales-funciones/INDICE.md`.
  - Si el manual de la convocatoria **YA existe** → reutilizarlo directamente (copiar/leer desde ahí). NO pedirlo.
  - Si **NO existe** → solo entonces dar el enlace de carga al operador:
    `https://github.com/AscensoPublico2026/ASCENSO-PUBLICO/upload/main/referencias/expedientes/<nombre>/manuales-vacantes`
- Al recibir aviso de carga: `git pull`.
- Después de leer los manuales nuevos, **agregarlos a la biblioteca**:
  `python3 referencias/consolidar_manuales.py && python3 referencias/indice_manuales.py`
  y commitear la biblioteca actualizada (así la próxima vez ya no se piden).

### PASO 7 — Cruce manuales↔perfil + PAQUETE PARA WHATSAPP
Leer los manuales (pdfplumber). Extraer **plazas por ciudad** (solo están en el manual, no en la matriz).
Entregar, en este orden:
1. **Tabla final** para reenviar al aspirante (Convocatoria · Cargo · Nivel · Salario · Plazas totales · plazas en sus ciudades).
2. **Guion de audio de saludo** (nota de voz, primera persona, sin emojis): disculpa por demora (orden de lista),
   mini-resumen del perfil, anuncio de opciones.
3. **Texto corto por cada PDF de manual** (sobrio, sin emojis): N° convocatoria · Cargo · Nivel · Salario ·
   Requisitos · Plazas (con ciudades) · Proceso.
4. **Guion de audio final** explicando todas las opciones de menor a mayor: por qué cumple cada una,
   estrategia (cargo bajo = más aspirantes; profesional/asesor aprovechan posgrado), decisión a criterio del
   aspirante, y recordatorio clave: **prueba escrita ELIMINATORIA, peso 80% conocimientos / 20% antecedentes**;
   ofrecer el **curso 100% personalizado de Ascenso Público** enfocado al manual. Cierre amable.
   Inscripciones hasta el **18 de septiembre de 2026**.

---

## ✅ Checklist de calidad antes de entregar
- [ ] Se leyó el 100% de los documentos (escaneadas vistas como imagen).
- [ ] Experiencia calculada desde el título, sin doble conteo.
- [ ] Todos los datos (salario/plazas/requisitos) provienen de matriz/manual (0 inventados).
- [ ] Tabla ordenada de menor a mayor salario desde la aspiración.
- [ ] Guiones en formato nota de voz, textos de PDF sin emojis.
- [ ] Un expediente = un aspirante (sin mezclar datos de otros).
- [ ] Todo commiteado y pusheado a `main` (nada se pierde si la sesión falla).

## 🧹 Higiene del repo
Borrar scripts temporales (`_*.py`) e imágenes de trabajo (`_img/`) antes del commit final;
conservar solo `documentos/`, `manuales-vacantes/` y `expediente.md`.

## 🔧 Notas técnicas útiles
- Python: usar `python3`. Instalar si hace falta: `pip install pdfplumber pymupdf openpyxl`.
- Datos base del concurso: matriz con 296 vacantes / 2.824 plazas. Tope por concurso: $18.073.001 (Jefe de División).
- Los cargos son de planta globalizada: pueden reubicarse según necesidad del servicio.

# 📚 Biblioteca de Guías — cómo funciona

Esta carpeta **reemplaza al antiguo `BIBLIOTECA.xlsx`**. Es el registro maestro de todas las guías del curso, en un formato versionable, legible en GitHub y **abierto** (cada guía nueva se registra aquí con su código y temas).

## Archivos

| Archivo | Qué es |
|---|---|
| **`biblioteca.json`** | 🧱 **Fuente de verdad.** Lista estructurada de todas las guías (código, día, categoría, nivel, estado, archivo y temas). Es lo que editas. |
| **`BIBLIOTECA.md`** | 📖 Índice legible (tablas + temas). **Se genera** desde el JSON; no se edita a mano. |
| **`generar_indice.py`** | 🔧 Script que regenera `BIBLIOTECA.md` a partir de `biblioteca.json`. |

## ➕ Cómo registrar o publicar una guía

1. Abre **`biblioteca.json`** y busca (o agrega) la guía en el arreglo `guias`.
2. Completa o actualiza sus campos:
   - `estado`: `"pendiente"` → `"publicada"` cuando la guía ya exista.
   - `archivo`: la ruta del HTML, por ejemplo `"guias/TEC-ESP-01-...html"`.
   - `temas`: la lista de contenidos de la guía.
3. Regenera el índice:
   ```bash
   python3 biblioteca/generar_indice.py
   ```
4. Listo: `BIBLIOTECA.md` queda actualizado y consistente.

> 💡 En el flujo de trabajo con Kiro, basta con pedir *"registra esta guía nueva en la biblioteca"* y se actualizan el JSON y el índice.

## Campos de cada guía (esquema)

```json
{
  "codigo": "TEC-ESP-01",
  "dia": 7,
  "titulo": "Competencias del Nivel Técnico",
  "biblioteca": "Por Nivel",
  "nivel": "Técnico",
  "tipo": "comportamental",
  "estado": "pendiente",
  "archivo": null,
  "reutilizable": true,
  "simulacro": true,
  "temas": ["..."]
}
```

- **biblioteca:** `Introducción` · `General` · `Por Nivel` · `Funcional` · `Por Entidad` · `Bonus` · `Simulacro Final`
- **tipo:** `bienvenida` · `conocimiento` · `comportamental` · `funcional` · `bonus` · `evaluacion`
- **estado:** `publicada` · `pendiente` · `bajo-demanda`

## Numeración del plan (21 días)

- **Día 1:** INTRO-00 (+ INTRO-01 *Conoce tu Entidad*, que se crea con la compra)
- **Días 2-4:** GEN-01, GEN-02, GEN-03 (Biblioteca General) ✅
- **Días 5-8:** Guías por Nivel (Asistencial / Técnico / Profesional) — según el nivel del aspirante
- **Días 9-20:** Guías Funcionales (según el cargo)
- **Día 21:** SIM-001 (Simulacro Integral Final)
- **Bonus:** BON-01 (Estrategia CNSC) — aplica a todos los niveles

# 📚 Biblioteca central de Manuales de Funciones

Esta carpeta guarda **todos los manuales de funciones** de la PGN 2026 que ya hemos descargado,
**una sola vez cada uno**, con el nombre `NNN-2026.pdf` (ej. `147-2026.pdf`).

## ¿Para qué sirve?
Las convocatorias se repiten entre aspirantes. En vez de volver a pedir y subir el mismo manual
cada vez, aquí quedan centralizados y **se reutilizan**. Ahorra tiempo y evita duplicados.

## Cómo se usa (para Kiro y para Laurita)
1. **Antes de pedirle manuales a un aspirante**, Kiro revisa `INDICE.md`:
   - Si el manual de esa convocatoria **YA está** → lo reutiliza (no hay que subir nada).
   - Si **NO está** → solo entonces se le pide ese manual al aspirante por el enlace de carga.
2. Cuando llegan manuales nuevos, se agregan a esta biblioteca corriendo:
   `python3 referencias/consolidar_manuales.py` y luego `python3 referencias/indice_manuales.py`
   (el primero copia sin duplicar; el segundo regenera el índice).

## Archivos
- `INDICE.md` → tabla con cada manual: cargo, nivel, grado, salario, plazas, estudio y experiencia
  (datos reales de la matriz). Incluye lista de convocatorias que aún NO tenemos.
- `NNN-2026.pdf` → los manuales.

> 💡 Nota: los manuales tienen las **plazas por ciudad** (dato que la matriz no trae), por eso vale
> la pena conservarlos.

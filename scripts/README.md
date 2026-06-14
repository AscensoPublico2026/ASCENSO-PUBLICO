# Scripts de Ascenso Público

Utilidades para mantener la landing. **Requieren internet y dependencias** (no corren en entornos aislados).

## Requisitos

```bash
cd scripts
python3 -m venv .venv && source .venv/bin/activate   # opcional pero recomendado
pip install -r requirements.txt
```

---

## 1) `scrape_simo.py` — convocatorias desde SIMO (CNSC)

SIMO es una app dinámica (se arma con JavaScript), por eso se usa un navegador
headless (Playwright) en vez de `requests`.

```bash
playwright install chromium      # solo la primera vez
python3 scrape_simo.py --ver     # navegador VISIBLE: úsalo la 1ª vez para ajustar selectores
python3 scrape_simo.py           # modo headless
python3 scrape_simo.py --solo-prueba   # solo las pendientes de prueba escrita
```

- Genera `convocatorias.json` **y** imprime el bloque `const CONVOCATORIAS = [...]`
  listo para pegar en `landing/index.html`.
- ⚠️ Los selectores marcados con `# AJUSTAR` deben verificarse contra el HTML real
  de SIMO (abre el inspector del navegador con `--ver`). SIMO cambia su maquetado.
- Úsalo de forma responsable: una sola consulta, respetando los términos de la CNSC.

---

## 2) `optimizar_imagenes.py` — fotos listas para web

Reduce el peso y genera tamaños responsive + WebP. Ideal para tu foto de
fundador, fotos de alumnos (con permiso) o las capturas del competidor.

```bash
python3 optimizar_imagenes.py --in ./originales --out ../brand/fotos
# personalizado:
python3 optimizar_imagenes.py --in ./originales --out ../brand/fotos --anchos 1600 1080 640 --calidad 80
```

Por cada `foto.jpg` genera `foto-1600.webp/.jpg`, `foto-1080.…`, `foto-640.…`.
Luego úsalas en el HTML con `<picture>` y `srcset` para que el celular cargue la
versión liviana.

### Ejemplo en el HTML (foto del fundador)

```html
<picture>
  <source type="image/webp"
          srcset="../brand/fotos/fundador-640.webp 640w, ../brand/fotos/fundador-1080.webp 1080w">
  <img src="../brand/fotos/fundador-1080.jpg" alt="Nombre del fundador, Ascenso Público" loading="lazy">
</picture>
```

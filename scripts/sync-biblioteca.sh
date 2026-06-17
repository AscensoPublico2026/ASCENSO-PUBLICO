#!/usr/bin/env bash
# Sincroniza el catálogo de guías hacia la plataforma.
#
# La fuente de verdad es /biblioteca/biblioteca.json. Como Vercel usa
# Root Directory = "plataforma", los archivos fuera de esa carpeta NO van
# en el deploy; por eso la plataforma necesita su propia copia en
# plataforma/lib/biblioteca.json.
#
# Además, las guías publicadas deben existir en plataforma/public/seed-guias/
# para poder subirse al bucket de Storage (vía /api/admin/seed-guias).
#
# Uso (desde la raíz del repo):  bash scripts/sync-biblioteca.sh
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# 1) Copiar el catálogo a la plataforma
cp "$ROOT/biblioteca/biblioteca.json" "$ROOT/plataforma/lib/biblioteca.json"
echo "✓ biblioteca.json copiado a plataforma/lib/"

# 2) Copiar las guías publicadas (HTML) a public/seed-guias
copiadas=0
for f in "$ROOT"/guias/*.html; do
  base="$(basename "$f")"
  cp "$f" "$ROOT/plataforma/public/seed-guias/$base"
  copiadas=$((copiadas+1))
done
echo "✓ $copiadas guías HTML copiadas a plataforma/public/seed-guias/"

# 3) Copiar los simulacros FINALES (simulacro/SIM-NNN.html, sin las versiones
#    de iteración -vN / -demo) a public/seed-guias para poder subirlos al bucket.
sim=0
for f in "$ROOT"/simulacro/SIM-[0-9][0-9][0-9].html; do
  [ -e "$f" ] || continue
  base="$(basename "$f")"
  cp "$f" "$ROOT/plataforma/public/seed-guias/$base"
  sim=$((sim+1))
done
echo "✓ $sim simulacro(s) copiado(s) a plataforma/public/seed-guias/"

echo "Listo. Recuerda: tras desplegar, visita /api/admin/seed-guias (como admin) para subirlas al bucket."

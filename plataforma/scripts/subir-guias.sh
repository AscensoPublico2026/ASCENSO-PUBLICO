#!/bin/bash
# ============================================================
# Script para subir las 17 guías HTML al bucket 'guias' de Supabase Storage
# 
# USO:
#   1. Abre la terminal en la raíz del repo (ASCENSO-PUBLICO/)
#   2. Edita las 2 variables de abajo con tus datos de Supabase
#   3. Ejecuta: bash plataforma/scripts/subir-guias.sh
#
# Dónde encontrar tus datos:
#   - Supabase → Settings → API → Project URL (sin /rest/v1 al final)
#   - Supabase → Settings → API → service_role key (la secreta)
# ============================================================

# ⚠️ EDITA ESTAS 2 LÍNEAS CON TUS DATOS:
SUPABASE_URL="https://TU-PROYECTO.supabase.co"
SERVICE_ROLE_KEY="tu_service_role_key_aqui"

# ============================================================
# NO EDITES NADA DE AQUÍ EN ADELANTE
# ============================================================

BUCKET="guias"
GUIAS_DIR="guias"
OK=0
FAIL=0

echo ""
echo "📚 Subiendo guías al bucket '$BUCKET' de Supabase Storage..."
echo "   URL: $SUPABASE_URL"
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -d "$GUIAS_DIR" ]; then
  echo "❌ Error: no encuentro la carpeta 'guias/'. Ejecuta este script desde la raíz del repo ASCENSO-PUBLICO/"
  exit 1
fi

# Verificar que las variables están configuradas
if [[ "$SUPABASE_URL" == *"TU-PROYECTO"* ]] || [[ "$SERVICE_ROLE_KEY" == *"tu_service"* ]]; then
  echo "❌ Error: edita SUPABASE_URL y SERVICE_ROLE_KEY en este script con tus datos reales."
  echo "   Encuéntralos en: Supabase → Settings → API"
  exit 1
fi

for FILE in "$GUIAS_DIR"/*.html; do
  FILENAME=$(basename "$FILE")
  STORAGE_PATH="guias/$FILENAME"
  
  # Subir usando la API REST de Supabase Storage
  RESPONSE=$(curl -s -w "%{http_code}" -o /tmp/supabase_upload_response.txt \
    -X POST \
    -H "Authorization: Bearer $SERVICE_ROLE_KEY" \
    -H "Content-Type: text/html; charset=utf-8" \
    -H "x-upsert: true" \
    --data-binary "@$FILE" \
    "$SUPABASE_URL/storage/v1/object/$BUCKET/$STORAGE_PATH")
  
  if [ "$RESPONSE" = "200" ] || [ "$RESPONSE" = "201" ]; then
    echo "  ✅ $STORAGE_PATH"
    OK=$((OK + 1))
  else
    BODY=$(cat /tmp/supabase_upload_response.txt 2>/dev/null)
    echo "  ❌ $STORAGE_PATH (HTTP $RESPONSE) $BODY"
    FAIL=$((FAIL + 1))
  fi
done

echo ""
echo "📊 Resultado: $OK subidas exitosamente, $FAIL errores."
if [ $FAIL -eq 0 ]; then
  echo "🎉 ¡Todas las guías están en el bucket! El visor de guías funcionará correctamente."
fi
echo ""

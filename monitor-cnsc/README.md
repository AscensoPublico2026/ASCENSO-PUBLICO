# 🔔 Monitor CNSC - Ascenso Público

Bot que monitorea automáticamente la página de la CNSC (Comisión Nacional del Servicio Civil) y te envía alertas por email cuando detecta novedades.

## ¿Qué hace?

- ✅ Revisa la web de la CNSC cada hora
- ✅ Detecta noticias nuevas, resoluciones y comunicados
- ✅ Detecta PDFs nuevos (guías, cronogramas, ejes temáticos)
- ✅ Descarga y lee el contenido de los PDFs
- ✅ Busca palabras clave relevantes (fechas de pruebas, ejes temáticos, citaciones)
- ✅ Envía un email con el resumen de las novedades

## Páginas que monitorea

- Noticias CNSC 2026
- Convocatorias en desarrollo
- Entidades del Orden Nacional y Corpomojana
- Entidades del Orden Nacional 2026
- Territorial 12
- DIAN 2022
- Empresas Sociales del Estado 2

## Configuración rápida (5 minutos)

### 1. Crear una App Password de Gmail

Como el email de destino es Gmail, necesitas crear una "Contraseña de aplicación":

1. Ve a https://myaccount.google.com/apppasswords
2. Selecciona "Correo" y "Otro (nombre personalizado)"
3. Escribe "Monitor CNSC"
4. Google te dará una contraseña de 16 caracteres (algo como `abcd efgh ijkl mnop`)
5. Copia esa contraseña (sin espacios)

### 2. Configurar el archivo .env

Edita el archivo `.env` en la raíz del proyecto:

```
ALERT_EMAIL=ascensopublico@gmail.com
SMTP_EMAIL=ascensopublico@gmail.com
SMTP_PASSWORD=tu-app-password-de-16-caracteres
CHECK_INTERVAL_MINUTES=60
```

**Nota:** `SMTP_EMAIL` es el email DESDE el cual se envían las alertas. Puede ser el mismo `ascensopublico@gmail.com`.

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Probar que funcione

```bash
# Enviar email de prueba
python main.py --test-email

# Ejecutar una revisión manual
python main.py

# Ejecutar en bucle continuo (cada hora)
python main.py --loop
```

## Despliegue en servidor (para que corra 24/7)

### Opción A: Railway (gratis/barato)

1. Crea una cuenta en https://railway.app
2. Conecta tu repositorio de GitHub
3. Railway detectará el `Procfile` y lo desplegará automáticamente
4. Configura las variables de entorno en el dashboard de Railway

### Opción B: Render (gratis)

1. Crea una cuenta en https://render.com
2. Crea un nuevo "Background Worker"
3. Conecta tu repositorio
4. Configura las variables de entorno

### Opción C: VPS (Digital Ocean, $4-6 USD/mes)

```bash
# Clonar el repositorio
git clone <tu-repo> monitor-cnsc
cd monitor-cnsc

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar con screen o tmux para que no se detenga
screen -S monitor
python main.py --loop
# Presiona Ctrl+A luego D para dejarlo corriendo en segundo plano
```

## Estructura del proyecto

```
monitor-cnsc/
├── main.py              ← Script principal (ejecutar este)
├── requirements.txt     ← Dependencias Python
├── .env                 ← Configuración (email, credenciales)
├── .env.example         ← Ejemplo de configuración
├── Procfile             ← Para despliegue en Railway/Render
├── README.md            ← Este archivo
├── src/
│   ├── config.py        ← Configuración y constantes
│   ├── scraper.py       ← Scraper de la web de la CNSC
│   ├── pdf_reader.py    ← Descarga y análisis de PDFs
│   └── emailer.py       ← Envío de alertas por email
├── data/
│   ├── state.json       ← Estado (qué ya se detectó)
│   └── pdfs/            ← PDFs descargados
└── logs/
    └── monitor_*.log    ← Logs diarios
```

## Personalización

### Agregar más convocatorias para monitorear

Edita `src/config.py` y agrega URLs al diccionario `URLS_TO_MONITOR`:

```python
URLS_TO_MONITOR = {
    ...
    "mi_nueva_convocatoria": "https://www.cnsc.gov.co/convocatorias/nombre-convocatoria",
}
```

### Agregar más palabras clave

Edita el archivo `.env`:

```
KEYWORDS=fecha de aplicación,pruebas escritas,cronograma,ejes temáticos,citación,...,nueva-palabra
```

### Cambiar intervalo de revisión

En `.env`:

```
CHECK_INTERVAL_MINUTES=30   # Revisar cada 30 minutos
```

## Notas importantes

- La primera vez que ejecutes el monitor, detectará TODOS los enlaces existentes como "nuevos" (es normal). A partir de la segunda ejecución solo reportará cambios reales.
- Si no quieres recibir el email de la primera ejecución, ejecuta `python main.py` una vez sin credenciales de email configuradas. Eso guardará el estado inicial sin enviar nada.
- El monitor usa `verify=False` para las conexiones HTTPS porque la CNSC tiene problemas con su certificado SSL.

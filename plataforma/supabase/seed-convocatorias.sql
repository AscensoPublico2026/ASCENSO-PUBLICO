-- ============================================================
-- Ascenso Público — Seed de convocatorias
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
-- Esto inserta las 6 convocatorias activas (si ya existe alguna no la duplica).
-- ============================================================

-- Primero verificamos cuáles ya existen para no duplicar
INSERT INTO public.convocatorias (nombre, entidad, estado, etiqueta, vacantes, fecha_prueba_aprox, imagen_url, tema, activa, orden)
SELECT * FROM (VALUES
  (
    'Entidades del Orden Nacional 2026',
    'Varias entidades nacionales (INVIMA, UNP, Contaduría, FONPRECON…) · Modalidad Ascenso',
    'abiertas'::estado_conv,
    'Inscripciones abiertas',
    '1.665',
    'Inscripciones en curso · prueba escrita pendiente',
    '/fotos/nacional.jpg',
    'nacional',
    true,
    1
  ),
  (
    'Territorial 12',
    'Entidades territoriales · Modalidad Abierto',
    'proxima'::estado_conv,
    'Prueba escrita pendiente',
    '1.573',
    'Inscripciones cerradas (12 jun 2026) · prueba pendiente',
    '/fotos/territorial12.jpg',
    'territorial',
    true,
    2
  ),
  (
    'Entidades del Orden Territorial y UApA',
    'Varios departamentos (incluye Valle del Cauca)',
    'proxima'::estado_conv,
    'Prueba escrita pendiente',
    '1.453',
    'Proceso en ejecución · prueba pendiente',
    '/fotos/territorial-uapa.jpg',
    'territorial',
    true,
    3
  ),
  (
    'DIAN 2676',
    'Dirección de Impuestos y Aduanas Nacionales',
    'proxima'::estado_conv,
    'Prueba escrita pendiente',
    '1.990',
    'En verificación de requisitos (VRM) · prueba pendiente',
    '/fotos/dian.jpg',
    'impuestos',
    true,
    4
  ),
  (
    'Procuraduría General de la Nación',
    'Procuraduría General de la Nación',
    'proxima'::estado_conv,
    'Inscripciones próximas',
    NULL,
    'Inscripciones: 7–18 sep 2026 (Res. 133 de 2026)',
    '/fotos/procuraduria.jpg',
    'justicia',
    true,
    5
  ),
  (
    'Empresas Sociales del Estado 2 (ESE 2)',
    'Sector salud · ESE',
    'proxima'::estado_conv,
    'En planeación',
    '~3.000',
    'En divulgación · prueba escrita lejana',
    '/fotos/ese.jpg',
    'salud',
    true,
    6
  )
) AS nuevas(nombre, entidad, estado, etiqueta, vacantes, fecha_prueba_aprox, imagen_url, tema, activa, orden)
WHERE NOT EXISTS (
  SELECT 1 FROM public.convocatorias c WHERE c.nombre = nuevas.nombre
);

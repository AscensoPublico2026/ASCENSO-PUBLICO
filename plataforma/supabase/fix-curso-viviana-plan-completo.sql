-- ============================================================
-- CURSO DE VIVIANA — dejar el plan COMPLETO y LIMPIO (PGN · Auxiliar Administrativo 5AM-10)
-- ============================================================
-- Qué resuelve:
--   El curso quedó con guías GENÉRICAS/CNSC mezcladas y DUPLICADAS (la
--   auto-carga vieja insertó INTRO-00 "y la CNSC", GEN-01/02/03 genéricas,
--   ASI-COM/ASI-ESP, etc.) junto con las correctas -PGN-AUX. Este script deja
--   EXACTAMENTE las 22 guías del plan de Viviana (Días 1 a 21) y borra el resto.
--
-- Cómo usarlo (Supabase → SQL Editor):
--   1) En el bloque "curso" de ABAJO, reemplaza el correo de Viviana
--      (o descomenta la variante por OPEC si prefieres identificarlo así).
--   2) Ejecuta el PASO 1 (previsualizar) y confirma que solo se borran
--      genéricas/duplicadas.
--   3) Ejecuta el PASO 2 (borra sobrantes) y el PASO 3 (inserta las que falten).
--   4) Ejecuta el PASO 4 (verificar): deben quedar 22 filas (Día 1 tiene 2).
--
-- Es idempotente: si lo corres de nuevo, no duplica (el PASO 3 solo inserta
-- las que falten).
-- ============================================================

-- ============================================================
-- PASO 1 — PREVISUALIZAR qué se ELIMINARÁ (no borra nada todavía)
-- ============================================================
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'CORREO_DE_VIVIANA@ejemplo.com'   -- ← REEMPLAZA por el correo real
  -- --- variante por OPEC (comenta la línea de arriba y descomenta estas dos):
  -- WHERE c.opec = 'OPEC_DE_VIVIANA'
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan AS (
  SELECT unnest(ARRAY[
    'guias/INTRO-00-PGN-AUX-presentacion-curso.html',
    'guias/ENT-PGN-AUX-01-conoce-entidad-pgn.html',
    'guias/GEN-01-PGN-AUX-estado-funcion-publica.html',
    'guias/GEN-02-PGN-AUX-relacion-estado-ciudadano.html',
    'guias/GEN-03-PGN-AUX-marco-institucional.html',
    'guias/ASI-PGN-AUX-01-responsabilidad-cumplimiento.html',
    'guias/ASI-PGN-AUX-02-organizacion-recursos.html',
    'guias/ASI-PGN-AUX-03-orientacion-usuario-equipo.html',
    'guias/ASI-PGN-AUX-04-manejo-informacion-integracion.html',
    'guias/FUN-GDOC-AUX-01-gestion-documental-archivo.html',
    'guias/FUN-GDOC-AUX-02-trd-expedientes-transferencias.html',
    'guias/FUN-OFI-AUX-01-documentos-oficina.html',
    'guias/FUN-OFI-AUX-02-ofimatica-aplicada.html',
    'guias/FUN-ATC-AUX-01-servicio-ciudadano.html',
    'guias/FUN-ALM-AUX-01-inventarios-bienes.html',
    'guias/FUN-ALM-AUX-02-inventarios-bienes-ii.html',
    'guias/FUN-PGN-AUX-01-estructura-funciones-pgn.html',
    'guias/FUN-GP-AUX-01-gestion-publica-estado.html',
    'guias/FUN-MIPG-AUX-01-sistemas-gestion-mipg.html',
    'guias/FUN-TRANS-AUX-01-transparencia-datos.html',
    'guias/FUN-CONST-AUX-01-constitucion-politica.html',
    'simulacro/SIM-PGN-5AM10-001.html'
  ]) AS archivo_path
)
SELECT gc.dia, gc.orden, gc.titulo, gc.archivo_path, '⟵ SE ELIMINARÁ' AS accion
FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
  AND (gc.archivo_path IS NULL OR gc.archivo_path NOT IN (SELECT archivo_path FROM plan))
ORDER BY gc.orden;


-- ============================================================
-- PASO 2 — BORRAR las filas que NO son del plan de Viviana
--   (ejecuta solo si el PASO 1 mostró únicamente genéricas/duplicadas)
-- ============================================================
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'CORREO_DE_VIVIANA@ejemplo.com'   -- ← REEMPLAZA por el correo real
  -- WHERE c.opec = 'OPEC_DE_VIVIANA'
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan AS (
  SELECT unnest(ARRAY[
    'guias/INTRO-00-PGN-AUX-presentacion-curso.html',
    'guias/ENT-PGN-AUX-01-conoce-entidad-pgn.html',
    'guias/GEN-01-PGN-AUX-estado-funcion-publica.html',
    'guias/GEN-02-PGN-AUX-relacion-estado-ciudadano.html',
    'guias/GEN-03-PGN-AUX-marco-institucional.html',
    'guias/ASI-PGN-AUX-01-responsabilidad-cumplimiento.html',
    'guias/ASI-PGN-AUX-02-organizacion-recursos.html',
    'guias/ASI-PGN-AUX-03-orientacion-usuario-equipo.html',
    'guias/ASI-PGN-AUX-04-manejo-informacion-integracion.html',
    'guias/FUN-GDOC-AUX-01-gestion-documental-archivo.html',
    'guias/FUN-GDOC-AUX-02-trd-expedientes-transferencias.html',
    'guias/FUN-OFI-AUX-01-documentos-oficina.html',
    'guias/FUN-OFI-AUX-02-ofimatica-aplicada.html',
    'guias/FUN-ATC-AUX-01-servicio-ciudadano.html',
    'guias/FUN-ALM-AUX-01-inventarios-bienes.html',
    'guias/FUN-ALM-AUX-02-inventarios-bienes-ii.html',
    'guias/FUN-PGN-AUX-01-estructura-funciones-pgn.html',
    'guias/FUN-GP-AUX-01-gestion-publica-estado.html',
    'guias/FUN-MIPG-AUX-01-sistemas-gestion-mipg.html',
    'guias/FUN-TRANS-AUX-01-transparencia-datos.html',
    'guias/FUN-CONST-AUX-01-constitucion-politica.html',
    'simulacro/SIM-PGN-5AM10-001.html'
  ]) AS archivo_path
)
DELETE FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
  AND (gc.archivo_path IS NULL OR gc.archivo_path NOT IN (SELECT archivo_path FROM plan));


-- ============================================================
-- PASO 3 — INSERTAR las guías del plan que FALTEN (con su día/orden/tipo)
--   Idempotente: solo inserta las que aún no estén en el curso.
-- ============================================================
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'CORREO_DE_VIVIANA@ejemplo.com'   -- ← REEMPLAZA por el correo real
  -- WHERE c.opec = 'OPEC_DE_VIVIANA'
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan(dia, orden, tipo, titulo, archivo_path) AS (
  VALUES
    (1, 0, 'general'::tipo_guia,   'Presentación del Curso (Auxiliar Administrativo 5AM-10 · PGN Convocatoria 242-2026)', 'guias/INTRO-00-PGN-AUX-presentacion-curso.html'),
    (1, 1, 'general'::tipo_guia,   'Conoce tu Entidad: Procuraduría General de la Nación (nivel Administrativo)',           'guias/ENT-PGN-AUX-01-conoce-entidad-pgn.html'),
    (2, 2, 'general'::tipo_guia,   'Estado y Función Pública (nivel Administrativo)',                                       'guias/GEN-01-PGN-AUX-estado-funcion-publica.html'),
    (3, 3, 'general'::tipo_guia,   'Relación Estado-Ciudadano (nivel Administrativo)',                                      'guias/GEN-02-PGN-AUX-relacion-estado-ciudadano.html'),
    (4, 4, 'general'::tipo_guia,   'Marco Institucional del Estado (nivel Administrativo)',                                 'guias/GEN-03-PGN-AUX-marco-institucional.html'),
    (5, 5, 'nivel'::tipo_guia,     'Responsabilidad y Cumplimiento de Parámetros (nivel Asistencial)',                      'guias/ASI-PGN-AUX-01-responsabilidad-cumplimiento.html'),
    (6, 6, 'nivel'::tipo_guia,     'Organización del Trabajo y Gestión de Recursos (nivel Asistencial)',                    'guias/ASI-PGN-AUX-02-organizacion-recursos.html'),
    (7, 7, 'nivel'::tipo_guia,     'Orientación al Usuario y Trabajo en Equipo (nivel Asistencial)',                        'guias/ASI-PGN-AUX-03-orientacion-usuario-equipo.html'),
    (8, 8, 'nivel'::tipo_guia,     'Manejo de la Información e Integración de Competencias (nivel Asistencial)',            'guias/ASI-PGN-AUX-04-manejo-informacion-integracion.html'),
    (9, 9, 'funcional'::tipo_guia, 'Gestión Documental y Archivo (nivel Administrativo)',                                   'guias/FUN-GDOC-AUX-01-gestion-documental-archivo.html'),
    (10,10,'funcional'::tipo_guia, 'TRD, Expedientes y Transferencias (nivel Administrativo)',                              'guias/FUN-GDOC-AUX-02-trd-expedientes-transferencias.html'),
    (11,11,'funcional'::tipo_guia, 'Elaboración de Documentos de Oficina (nivel Administrativo)',                           'guias/FUN-OFI-AUX-01-documentos-oficina.html'),
    (12,12,'funcional'::tipo_guia, 'Ofimática Aplicada al Trabajo Administrativo',                                          'guias/FUN-OFI-AUX-02-ofimatica-aplicada.html'),
    (13,13,'funcional'::tipo_guia, 'Atención al Usuario y Servicio al Ciudadano (nivel Administrativo)',                    'guias/FUN-ATC-AUX-01-servicio-ciudadano.html'),
    (14,14,'funcional'::tipo_guia, 'Manejo de Inventarios y Control de Bienes I (nivel Administrativo)',                    'guias/FUN-ALM-AUX-01-inventarios-bienes.html'),
    (15,15,'funcional'::tipo_guia, 'Manejo de Inventarios y Control de Bienes II (nivel Administrativo)',                   'guias/FUN-ALM-AUX-02-inventarios-bienes-ii.html'),
    (16,16,'funcional'::tipo_guia, 'Estructura, Organización y Funciones de la PGN (nivel Administrativo)',                 'guias/FUN-PGN-AUX-01-estructura-funciones-pgn.html'),
    (17,17,'funcional'::tipo_guia, 'Gestión Pública y Funcionamiento del Estado (nivel Administrativo)',                    'guias/FUN-GP-AUX-01-gestion-publica-estado.html'),
    (18,18,'funcional'::tipo_guia, 'Sistemas de Gestión y MIPG (nivel Administrativo)',                                     'guias/FUN-MIPG-AUX-01-sistemas-gestion-mipg.html'),
    (19,19,'funcional'::tipo_guia, 'Transparencia, Acceso a la Información y Protección de Datos (nivel Administrativo)',   'guias/FUN-TRANS-AUX-01-transparencia-datos.html'),
    (20,20,'funcional'::tipo_guia, 'Nociones de Constitución Política (nivel Administrativo)',                              'guias/FUN-CONST-AUX-01-constitucion-politica.html'),
    (21,21,'simulacro'::tipo_guia, 'Simulacro Integral Final (Auxiliar Administrativo 5AM-10)',                             'simulacro/SIM-PGN-5AM10-001.html')
)
INSERT INTO public.guias_curso (curso_id, dia, orden, tipo, titulo, archivo_path)
SELECT (SELECT id FROM curso), p.dia, p.orden, p.tipo, p.titulo, p.archivo_path
FROM plan p
WHERE NOT EXISTS (
  SELECT 1 FROM public.guias_curso gc
  WHERE gc.curso_id = (SELECT id FROM curso)
    AND gc.archivo_path = p.archivo_path
);


-- ============================================================
-- PASO 4 — VERIFICAR: deben quedar EXACTAMENTE 22 filas (Día 1 tiene 2)
-- ============================================================
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'CORREO_DE_VIVIANA@ejemplo.com'   -- ← REEMPLAZA por el correo real
  -- WHERE c.opec = 'OPEC_DE_VIVIANA'
  ORDER BY c.created_at DESC
  LIMIT 1
)
SELECT gc.dia, gc.orden, gc.tipo, gc.titulo, gc.archivo_path
FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
ORDER BY gc.orden;

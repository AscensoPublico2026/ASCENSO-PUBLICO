-- ============================================================
-- LIMPIEZA DE DUPLICADOS — curso de Gina (Procurador Judicial II — PGN)
-- ============================================================
-- Causa del problema: al crear el curso, la auto-carga insertó un set de
-- guías GENÉRICAS (CNSC: INTRO-00-PGN, GEN-01/02/03 sin -PGN, PRO-COM/PRO-ESP,
-- BON-01/02) y LUEGO la migración insertó el set CORRECTO del plan de Gina
-- (INTRO-00-PGN-PRO, GEN-0x-PGN, PGN-PRO-COM-0x, etc.). Como los archivos
-- eran distintos, quedaron DUPLICADAS (se ven 6 generales en vez de 3).
--
-- Solución: dejar SOLO las 22 guías del plan real de Gina y borrar el resto.
-- Ejecutar por pasos en el SQL Editor de Supabase.
-- ============================================================

-- Lista blanca: las 22 guías CORRECTAS del plan de Gina.
-- (Usada por los pasos 1 y 2 mediante un CTE.)

-- ------------------------------------------------------------
-- PASO 1 (PREVISUALIZAR): muestra qué filas se ELIMINARÍAN.
--   Revisa que solo aparezcan las genéricas/duplicadas antes de borrar.
-- ------------------------------------------------------------
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan AS (
  SELECT unnest(ARRAY[
    'guias/INTRO-00-PGN-PRO-presentacion-curso.html',
    'guias/ENT-PGN-PRO-01-conoce-entidad-pgn.html',
    'guias/GEN-01-PGN-estado-funcion-publica.html',
    'guias/GEN-02-PGN-relacion-estado-ciudadano.html',
    'guias/GEN-03-PGN-marco-institucional.html',
    'guias/PGN-PRO-COM-01-responsabilidad-organizacion-trabajo.html',
    'guias/PGN-PRO-COM-02-orientacion-resultados-impacto-influencia.html',
    'guias/PGN-PRO-COM-03-investigacion-pensamiento-conceptual-analitico.html',
    'guias/PGN-PRO-COM-04-alcance-cargo-profesional-evaluacion-niveles.html',
    'guias/FUN-MP-01-PRO-ministerio-publico-estructura-pgn.html',
    'guias/FUN-MP-02-PRO-funcion-intervencion-ministerio-publico.html',
    'guias/FUN-INT-01-intervencion-judicial-tecnica-conceptos-argumentacion.html',
    'guias/FUN-INT-02-intervencion-constitucional-tutela-acciones.html',
    'guias/FUN-INT-03-intervencion-penal-procesal-penal.html',
    'guias/FUN-INT-04-intervencion-civil-laboral-familia-contencioso.html',
    'guias/FUN-CONC-01-conciliacion-masc-comites.html',
    'guias/FUN-PREV-01-funcion-preventiva-control-gestion.html',
    'guias/FUN-DDHH-01-derechos-humanos-dih-justicia-transicional.html',
    'guias/FUN-PROB-01-derecho-probatorio-valoracion-prueba.html',
    'guias/FUN-JUR-PRO-01-gestion-publica-normatividad-administrativa.html',
    'guias/FUN-OFI-PRO-01-documentos-oficina-informes-sistemas.html',
    'simulacro/SIM-PGN-002.html'
  ]) AS archivo_path
)
SELECT gc.dia, gc.orden, gc.titulo, gc.archivo_path, '⟵ SE ELIMINARÁ' AS accion
FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
  AND (gc.archivo_path IS NULL OR gc.archivo_path NOT IN (SELECT archivo_path FROM plan))
ORDER BY gc.orden;

-- ------------------------------------------------------------
-- PASO 2 (BORRAR): elimina las filas que NO pertenecen al plan de Gina.
--   Ejecútalo solo si el PASO 1 mostró únicamente duplicados/genéricas.
-- ------------------------------------------------------------
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan AS (
  SELECT unnest(ARRAY[
    'guias/INTRO-00-PGN-PRO-presentacion-curso.html',
    'guias/ENT-PGN-PRO-01-conoce-entidad-pgn.html',
    'guias/GEN-01-PGN-estado-funcion-publica.html',
    'guias/GEN-02-PGN-relacion-estado-ciudadano.html',
    'guias/GEN-03-PGN-marco-institucional.html',
    'guias/PGN-PRO-COM-01-responsabilidad-organizacion-trabajo.html',
    'guias/PGN-PRO-COM-02-orientacion-resultados-impacto-influencia.html',
    'guias/PGN-PRO-COM-03-investigacion-pensamiento-conceptual-analitico.html',
    'guias/PGN-PRO-COM-04-alcance-cargo-profesional-evaluacion-niveles.html',
    'guias/FUN-MP-01-PRO-ministerio-publico-estructura-pgn.html',
    'guias/FUN-MP-02-PRO-funcion-intervencion-ministerio-publico.html',
    'guias/FUN-INT-01-intervencion-judicial-tecnica-conceptos-argumentacion.html',
    'guias/FUN-INT-02-intervencion-constitucional-tutela-acciones.html',
    'guias/FUN-INT-03-intervencion-penal-procesal-penal.html',
    'guias/FUN-INT-04-intervencion-civil-laboral-familia-contencioso.html',
    'guias/FUN-CONC-01-conciliacion-masc-comites.html',
    'guias/FUN-PREV-01-funcion-preventiva-control-gestion.html',
    'guias/FUN-DDHH-01-derechos-humanos-dih-justicia-transicional.html',
    'guias/FUN-PROB-01-derecho-probatorio-valoracion-prueba.html',
    'guias/FUN-JUR-PRO-01-gestion-publica-normatividad-administrativa.html',
    'guias/FUN-OFI-PRO-01-documentos-oficina-informes-sistemas.html',
    'simulacro/SIM-PGN-002.html'
  ]) AS archivo_path
)
DELETE FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
  AND (gc.archivo_path IS NULL OR gc.archivo_path NOT IN (SELECT archivo_path FROM plan));

-- ------------------------------------------------------------
-- PASO 3 (VERIFICAR): debe quedar exactamente el plan de Gina (22 filas),
--   una por día 1-21 (el Día 1 tiene 2: presentación + entidad).
-- ------------------------------------------------------------
SELECT gc.dia, gc.orden, gc.titulo, gc.archivo_path
FROM public.guias_curso gc
JOIN public.cursos c ON c.id = gc.curso_id
JOIN public.profiles p ON p.id = c.usuario_id
WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
ORDER BY gc.orden;

-- ============================================================
-- CARGA DEL CURSO — María Alejandra (Profesional Universitario 3PU-17 — PGN)
-- ============================================================
-- Convocatoria 147-2026 — Procuraduría General de la Nación (régimen ESPECIAL, NO CNSC)
-- Cargo: Profesional Universitario · Código 3PU-17 · Nivel Profesional
--
-- Este script es IDEMPOTENTE y ANTI-DUPLICADOS:
--   * PASO A  → localiza el curso por correo (revisa el resultado).
--   * PASO B  → PREVISUALIZA qué guías ajenas se limpiarían (genéricas de auto-carga).
--   * PASO C  → BORRA las guías que NO pertenecen al plan real (solo si B mostró basura).
--   * PASO D  → INSERTA las 22 guías del plan; NO duplica (WHERE NOT EXISTS por archivo_path).
--   * PASO E  → VERIFICA: deben quedar exactamente 22 filas, sin archivo_path repetido.
--
-- >>> REEMPLAZA el correo de abajo por el de María Alejandra ANTES de ejecutar. <<<
-- ============================================================

-- ############################################################
-- PASO A — Localizar el curso (ejecuta y revisa que aparezca 1 curso)
-- ############################################################
SELECT c.id AS curso_id, c.opec, c.cargo_nombre, c.nivel, c.estado, c.created_at,
       (SELECT COUNT(*) FROM public.guias_curso gc WHERE gc.curso_id = c.id) AS guias_actuales
FROM public.cursos c
JOIN public.profiles p ON p.id = c.usuario_id
WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com'   -- <<< EDITAR
ORDER BY c.created_at DESC;


-- ############################################################
-- PASO B — PREVISUALIZAR limpieza de guías ajenas (genéricas de auto-carga)
--   Muestra las filas que se ELIMINARÍAN por no pertenecer al plan 3PU-17.
--   Si el curso es nuevo/limpio, no devolverá filas: puedes saltar al PASO D.
-- ############################################################
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com'   -- <<< EDITAR
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan AS (
  SELECT unnest(ARRAY[
    'guias/INTRO-00-PGN-PU-presentacion-curso.html',
    'guias/ENT-PGN-PU-01-conoce-entidad-pgn.html',
    'guias/GEN-01-PGN-estado-funcion-publica.html',
    'guias/GEN-02-PGN-relacion-estado-ciudadano.html',
    'guias/GEN-03-PGN-marco-institucional.html',
    'guias/PU-PRO-COM-01-responsabilidad-organizacion-trabajo.html',
    'guias/PU-PRO-COM-02-orientacion-resultados-cumplimiento-parametros.html',
    'guias/PU-PRO-COM-03-investigacion-pensamiento-conceptual.html',
    'guias/PU-PRO-COM-04-alcance-cargo-profesional-evaluacion.html',
    'guias/FUN-MP-01-PU-ministerio-publico-estructura-pgn.html',
    'guias/FUN-CONST-01-derecho-constitucional-control-disciplinario.html',
    'guias/FUN-DIS-01-PU-derecho-disciplinario-fundamentos.html',
    'guias/FUN-DIS-02-PU-procedimiento-instruccion-juzgamiento.html',
    'guias/FUN-PROB-01-PU-derecho-probatorio-valoracion.html',
    'guias/FUN-DIS-03-PU-recursos-segunda-instancia-siri.html',
    'guias/FUN-PREV-01-PU-funcion-preventiva-control-gestion.html',
    'guias/FUN-PEN-01-PU-derecho-penal-administracion-publica.html',
    'guias/FUN-PEN-02-PU-derecho-penal-procesal-penal.html',
    'guias/FUN-JUR-01-PU-derecho-administrativo-cpaca.html',
    'guias/FUN-CONT-01-PU-contratacion-estatal-anticorrupcion.html',
    'guias/FUN-GDOC-01-PU-gestion-documental-atencion-sistemas.html',
    'simulacro/SIM-PGN-3PU17-001.html'
  ]) AS archivo_path
)
SELECT gc.dia, gc.orden, gc.titulo, gc.archivo_path, '⟵ SE ELIMINARÍA' AS accion
FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
  AND (gc.archivo_path IS NULL OR gc.archivo_path NOT IN (SELECT archivo_path FROM plan))
ORDER BY gc.orden;


-- ############################################################
-- PASO C — BORRAR las guías ajenas (ejecuta SOLO si el PASO B mostró basura)
-- ############################################################
WITH curso AS (
  SELECT c.id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com'   -- <<< EDITAR
  ORDER BY c.created_at DESC
  LIMIT 1
),
plan AS (
  SELECT unnest(ARRAY[
    'guias/INTRO-00-PGN-PU-presentacion-curso.html',
    'guias/ENT-PGN-PU-01-conoce-entidad-pgn.html',
    'guias/GEN-01-PGN-estado-funcion-publica.html',
    'guias/GEN-02-PGN-relacion-estado-ciudadano.html',
    'guias/GEN-03-PGN-marco-institucional.html',
    'guias/PU-PRO-COM-01-responsabilidad-organizacion-trabajo.html',
    'guias/PU-PRO-COM-02-orientacion-resultados-cumplimiento-parametros.html',
    'guias/PU-PRO-COM-03-investigacion-pensamiento-conceptual.html',
    'guias/PU-PRO-COM-04-alcance-cargo-profesional-evaluacion.html',
    'guias/FUN-MP-01-PU-ministerio-publico-estructura-pgn.html',
    'guias/FUN-CONST-01-derecho-constitucional-control-disciplinario.html',
    'guias/FUN-DIS-01-PU-derecho-disciplinario-fundamentos.html',
    'guias/FUN-DIS-02-PU-procedimiento-instruccion-juzgamiento.html',
    'guias/FUN-PROB-01-PU-derecho-probatorio-valoracion.html',
    'guias/FUN-DIS-03-PU-recursos-segunda-instancia-siri.html',
    'guias/FUN-PREV-01-PU-funcion-preventiva-control-gestion.html',
    'guias/FUN-PEN-01-PU-derecho-penal-administracion-publica.html',
    'guias/FUN-PEN-02-PU-derecho-penal-procesal-penal.html',
    'guias/FUN-JUR-01-PU-derecho-administrativo-cpaca.html',
    'guias/FUN-CONT-01-PU-contratacion-estatal-anticorrupcion.html',
    'guias/FUN-GDOC-01-PU-gestion-documental-atencion-sistemas.html',
    'simulacro/SIM-PGN-3PU17-001.html'
  ]) AS archivo_path
)
DELETE FROM public.guias_curso gc
WHERE gc.curso_id = (SELECT id FROM curso)
  AND (gc.archivo_path IS NULL OR gc.archivo_path NOT IN (SELECT archivo_path FROM plan));


-- ############################################################
-- PASO D — INSERTAR las 22 guías del plan 3PU-17 (idempotente, no duplica)
-- ############################################################
DO $$
DECLARE
  v_curso_id uuid;
  v_count int;
BEGIN
  SELECT c.id INTO v_curso_id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com'   -- <<< EDITAR
  ORDER BY c.created_at DESC
  LIMIT 1;

  IF v_curso_id IS NULL THEN
    RAISE EXCEPTION 'No se encontró el curso de María Alejandra. Verifica el correo y que el curso exista en public.cursos.';
  END IF;

  RAISE NOTICE 'Curso encontrado: %', v_curso_id;

  INSERT INTO public.guias_curso (curso_id, dia, titulo, tipo, orden, archivo_path)
  SELECT v_curso_id, dia, titulo, tipo::tipo_guia, orden, archivo_path
  FROM (VALUES
    -- Día 1: Presentación + Conoce tu Entidad (PGN)
    (1,  'Presentación del Curso y el Concurso de la Procuraduría (Profesional Universitario 3PU-17)', 'general',   1,  'guias/INTRO-00-PGN-PU-presentacion-curso.html'),
    (1,  'Conoce tu Entidad: Procuraduría General de la Nación',                                       'general',   2,  'guias/ENT-PGN-PU-01-conoce-entidad-pgn.html'),
    -- Días 2-4: Generales (versión PGN)
    (2,  'Estado y Función Pública (versión PGN)',                                                     'general',   3,  'guias/GEN-01-PGN-estado-funcion-publica.html'),
    (3,  'Relación Estado-Ciudadano (versión PGN)',                                                    'general',   4,  'guias/GEN-02-PGN-relacion-estado-ciudadano.html'),
    (4,  'Marco Institucional (versión PGN)',                                                          'general',   5,  'guias/GEN-03-PGN-marco-institucional.html'),
    -- Días 5-8: Competencias comportamentales (Nivel Profesional)
    (5,  'Responsabilidad con la Organización y Organización del Trabajo (Profesional Universitario 3PU-17)', 'nivel', 6,  'guias/PU-PRO-COM-01-responsabilidad-organizacion-trabajo.html'),
    (6,  'Orientación a Resultados y Cumplimiento de Parámetros de Trabajo (Profesional Universitario 3PU-17)', 'nivel', 7, 'guias/PU-PRO-COM-02-orientacion-resultados-cumplimiento-parametros.html'),
    (7,  'Investigación y Pensamiento Conceptual (Profesional Universitario 3PU-17)',                  'nivel',     8,  'guias/PU-PRO-COM-03-investigacion-pensamiento-conceptual.html'),
    (8,  'Alcance del Cargo y Evaluación de Competencias (Profesional Universitario 3PU-17)',          'nivel',     9,  'guias/PU-PRO-COM-04-alcance-cargo-profesional-evaluacion.html'),
    -- Días 9-20: Funcionales 3PU-17
    (9,  'El Ministerio Público: Estructura y Funciones de la PGN (Profesional Universitario 3PU-17)', 'funcional', 10, 'guias/FUN-MP-01-PU-ministerio-publico-estructura-pgn.html'),
    (10, 'Derecho Constitucional aplicado al Control Disciplinario',                                   'funcional', 11, 'guias/FUN-CONST-01-derecho-constitucional-control-disciplinario.html'),
    (11, 'Derecho Disciplinario I: Fundamentos (Profesional Universitario 3PU-17)',                    'funcional', 12, 'guias/FUN-DIS-01-PU-derecho-disciplinario-fundamentos.html'),
    (12, 'Derecho Disciplinario II: Procedimiento, Instrucción y Juzgamiento (Profesional Universitario 3PU-17)', 'funcional', 13, 'guias/FUN-DIS-02-PU-procedimiento-instruccion-juzgamiento.html'),
    (13, 'Derecho Probatorio y Valoración de la Prueba (Profesional Universitario 3PU-17)',            'funcional', 14, 'guias/FUN-PROB-01-PU-derecho-probatorio-valoracion.html'),
    (14, 'Recursos, Segunda Instancia, Grado de Consulta y SIRI (Profesional Universitario 3PU-17)',   'funcional', 15, 'guias/FUN-DIS-03-PU-recursos-segunda-instancia-siri.html'),
    (15, 'Función Preventiva y Control de Gestión (Profesional Universitario 3PU-17)',                 'funcional', 16, 'guias/FUN-PREV-01-PU-funcion-preventiva-control-gestion.html'),
    (16, 'Derecho Penal aplicado al ámbito disciplinario (Profesional Universitario 3PU-17)',          'funcional', 17, 'guias/FUN-PEN-01-PU-derecho-penal-administracion-publica.html'),
    (17, 'Derecho Penal y Procesal Penal (Profesional Universitario 3PU-17)',                          'funcional', 18, 'guias/FUN-PEN-02-PU-derecho-penal-procesal-penal.html'),
    (18, 'Derecho Administrativo y CPACA (Profesional Universitario 3PU-17)',                          'funcional', 19, 'guias/FUN-JUR-01-PU-derecho-administrativo-cpaca.html'),
    (19, 'Contratación Estatal y Estatuto Anticorrupción (Profesional Universitario 3PU-17)',          'funcional', 20, 'guias/FUN-CONT-01-PU-contratacion-estatal-anticorrupcion.html'),
    (20, 'Gestión Documental, Atención al Ciudadano y Sistemas de Gestión (Profesional Universitario 3PU-17)', 'funcional', 21, 'guias/FUN-GDOC-01-PU-gestion-documental-atencion-sistemas.html'),
    -- Día 21: Simulacro Integral Final
    (21, 'Simulacro Integral Final (Profesional Universitario 3PU-17): 50 preguntas funcionales + 20 Likert', 'simulacro', 22, 'simulacro/SIM-PGN-3PU17-001.html')
  ) AS t(dia, titulo, tipo, orden, archivo_path)
  WHERE NOT EXISTS (
    SELECT 1 FROM public.guias_curso gc
    WHERE gc.curso_id = v_curso_id
      AND gc.archivo_path = t.archivo_path
  );

  GET DIAGNOSTICS v_count = ROW_COUNT;
  RAISE NOTICE '✅ Se insertaron % guías nuevas en el curso de María Alejandra.', v_count;
END $$;


-- ############################################################
-- PASO E — VERIFICAR: deben quedar EXACTAMENTE 22 filas, sin duplicados
-- ############################################################
-- E.1 Listado ordenado (revisa que sean las 22 del plan, día 1 con 2 guías)
SELECT gc.dia, gc.orden, gc.tipo, gc.titulo, gc.archivo_path
FROM public.guias_curso gc
JOIN public.cursos c ON c.id = gc.curso_id
JOIN public.profiles p ON p.id = c.usuario_id
WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com'   -- <<< EDITAR
ORDER BY gc.orden;

-- E.2 Conteo total (debe ser 22) y archivo_path repetidos (debe ser 0 filas)
SELECT COUNT(*) AS total_guias
FROM public.guias_curso gc
JOIN public.cursos c ON c.id = gc.curso_id
JOIN public.profiles p ON p.id = c.usuario_id
WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com';   -- <<< EDITAR

SELECT gc.archivo_path, COUNT(*) AS veces
FROM public.guias_curso gc
JOIN public.cursos c ON c.id = gc.curso_id
JOIN public.profiles p ON p.id = c.usuario_id
WHERE LOWER(p.correo) = 'alejandraranzazu@gmail.com'   -- <<< EDITAR
GROUP BY gc.archivo_path
HAVING COUNT(*) > 1;   -- si devuelve filas, hay duplicados (no debería)

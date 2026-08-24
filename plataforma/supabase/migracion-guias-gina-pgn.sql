-- ============================================================
-- MIGRACIÓN: Cargar el curso de Gina (Procurador Judicial II — PGN)
-- ============================================================
-- Ejecutar UNA VEZ en el SQL Editor de Supabase después del merge del PR.
--
-- Gina Alexandra Rojas  (alexandrarojash@gmail.com)
-- Cargo: Procurador Judicial II  ·  Código 3PJ-EC  ·  OPEC 89-2026
-- Convocatoria 89-2026 (Res. 212/2026) — Procuraduría General de la Nación
-- Nivel: Profesional
--
-- Carga las 21 sesiones del plan aprobado. Es IDEMPOTENTE: solo inserta
-- las guías que aún no existan en el curso (no duplica por archivo_path).
-- ============================================================

DO $$
DECLARE
  v_curso_id uuid;
  v_count int;
BEGIN
  -- 1) Buscar el curso de Gina por correo + OPEC exacto del cargo
  SELECT c.id INTO v_curso_id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
    AND c.opec = '89-2026 - 3PJ-EC'
  ORDER BY c.created_at DESC
  LIMIT 1;

  -- Fallback: si no se halló con ese OPEC exacto, buscar solo por correo
  IF v_curso_id IS NULL THEN
    SELECT c.id INTO v_curso_id
    FROM public.cursos c
    JOIN public.profiles p ON p.id = c.usuario_id
    WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
    ORDER BY c.created_at DESC
    LIMIT 1;
  END IF;

  IF v_curso_id IS NULL THEN
    RAISE EXCEPTION 'No se encontró el curso de Gina (alexandrarojash@gmail.com). Verifica que el curso exista en la tabla cursos.';
  END IF;

  RAISE NOTICE 'Curso de Gina encontrado: %', v_curso_id;

  SELECT COUNT(*) INTO v_count FROM public.guias_curso WHERE curso_id = v_curso_id;
  IF v_count > 0 THEN
    RAISE NOTICE 'El curso ya tiene % guías. Se agregarán solo las que falten (sin duplicar).', v_count;
  END IF;

  -- 2) Insertar las 21 sesiones del plan (solo las que no existan por archivo_path)
  INSERT INTO public.guias_curso (curso_id, dia, titulo, tipo, orden, archivo_path)
  SELECT v_curso_id, dia, titulo, tipo::tipo_guia, orden, archivo_path
  FROM (VALUES
    -- Día 1: Presentación + Conoce tu Entidad (PGN)
    (1,  'Presentación del Curso y el Concurso de la Procuraduría',                         'general',    1,  'guias/INTRO-00-PGN-PRO-presentacion-curso.html'),
    (1,  'Conoce tu Entidad: Procuraduría General de la Nación',                            'general',    2,  'guias/ENT-PGN-PRO-01-conoce-entidad-pgn.html'),
    -- Días 2-4: Generales (versión PGN)
    (2,  'Estado y Función Pública',                                                        'general',    3,  'guias/GEN-01-PGN-estado-funcion-publica.html'),
    (3,  'Relación Estado-Ciudadano',                                                       'general',    4,  'guias/GEN-02-PGN-relacion-estado-ciudadano.html'),
    (4,  'Marco Institucional',                                                             'general',    5,  'guias/GEN-03-PGN-marco-institucional.html'),
    -- Días 5-8: Competencias comportamentales (Nivel Profesional)
    (5,  'Responsabilidad con la Organización y Organización del Trabajo (Nivel Profesional)', 'nivel',   6,  'guias/PGN-PRO-COM-01-responsabilidad-organizacion-trabajo.html'),
    (6,  'Orientación a Resultados (C) e Impacto e Influencia (A) (Nivel Profesional)',     'nivel',      7,  'guias/PGN-PRO-COM-02-orientacion-resultados-impacto-influencia.html'),
    (7,  'Investigación (B), Pensamiento Conceptual (A) y Analítico (B) (Nivel Profesional)', 'nivel',    8,  'guias/PGN-PRO-COM-03-investigacion-pensamiento-conceptual-analitico.html'),
    (8,  'Alcance del Cargo Profesional y Evaluación por Niveles A/B/C (Nivel Profesional)', 'nivel',     9,  'guias/PGN-PRO-COM-04-alcance-cargo-profesional-evaluacion-niveles.html'),
    -- Días 9-10: Ministerio Público (funcionales reutilizables)
    (9,  'El Ministerio Público: Estructura y Funciones de la PGN',                         'funcional',  10, 'guias/FUN-MP-01-PRO-ministerio-publico-estructura-pgn.html'),
    (10, 'Función de Intervención del Ministerio Público',                                  'funcional',  11, 'guias/FUN-MP-02-PRO-funcion-intervencion-ministerio-publico.html'),
    -- Días 11-14: Bloque de Intervención Judicial
    (11, 'Intervención Judicial: Técnica, Conceptos y Argumentación Jurídica',              'funcional',  12, 'guias/FUN-INT-01-intervencion-judicial-tecnica-conceptos-argumentacion.html'),
    (12, 'Intervención en lo Constitucional: Tutela, Acciones Constitucionales y Populares','funcional',  13, 'guias/FUN-INT-02-intervencion-constitucional-tutela-acciones.html'),
    (13, 'Intervención en lo Penal y Procesal Penal (Ley 906/2004)',                        'funcional',  14, 'guias/FUN-INT-03-intervencion-penal-procesal-penal.html'),
    (14, 'Intervención en lo Civil, Laboral, de Familia y Contencioso-Administrativo',      'funcional',  15, 'guias/FUN-INT-04-intervencion-civil-laboral-familia-contencioso.html'),
    -- Días 15-18: Bloque funcional especializado
    (15, 'Conciliación, MASC y Comités de Conciliación',                                    'funcional',  16, 'guias/FUN-CONC-01-conciliacion-masc-comites.html'),
    (16, 'Función Preventiva y de Control de Gestión del Ministerio Público',               'funcional',  17, 'guias/FUN-PREV-01-funcion-preventiva-control-gestion.html'),
    (17, 'Derechos Humanos, DIH y Justicia Transicional (Ley 1448/2011)',                   'funcional',  18, 'guias/FUN-DDHH-01-derechos-humanos-dih-justicia-transicional.html'),
    (18, 'Derecho Probatorio, Valoración de la Prueba y Trámite Procesal',                  'funcional',  19, 'guias/FUN-PROB-01-derecho-probatorio-valoracion-prueba.html'),
    -- Días 19-20: Cierre funcional (reutilizables)
    (19, 'Gestión Pública y Normatividad Administrativa',                                   'funcional',  20, 'guias/FUN-JUR-PRO-01-gestion-publica-normatividad-administrativa.html'),
    (20, 'Documentos de Oficina, Informes y Sistemas de Información',                       'funcional',  21, 'guias/FUN-OFI-PRO-01-documentos-oficina-informes-sistemas.html'),
    -- Día 21: Simulacro Integral Final (50 preguntas, Nivel Profesional)
    (21, 'Simulacro Integral Final — Procurador Judicial II (50 preguntas)',                'simulacro',  22, 'simulacro/SIM-PGN-002.html')
  ) AS t(dia, titulo, tipo, orden, archivo_path)
  WHERE NOT EXISTS (
    SELECT 1 FROM public.guias_curso gc
    WHERE gc.curso_id = v_curso_id
      AND gc.archivo_path = t.archivo_path
  );

  GET DIAGNOSTICS v_count = ROW_COUNT;
  RAISE NOTICE '✅ Se insertaron % guías nuevas en el curso de Gina.', v_count;
END $$;

-- ============================================================
-- NOTA: si el OPEC del curso de Gina quedó registrado con otro formato
-- (por ejemplo solo '89-2026' o '3PJ-EC'), el bloque usa el fallback por
-- correo y de todos modos cargará las guías. Verifica con:
--   SELECT id, opec, created_at FROM public.cursos c
--   JOIN public.profiles p ON p.id = c.usuario_id
--   WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com';
-- ============================================================

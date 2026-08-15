-- ============================================================
-- MIGRACIÓN: Cargar guías automáticas al curso de Sandra (PGN)
-- ============================================================
-- Ejecutar UNA VEZ en Supabase SQL Editor después del merge.
--
-- Sandra Johana Marquez Perez (Sandrajmarquezp@gmail.com)
-- Cargo: Sustanciador 4SU-08, Nivel Técnico
-- Convocatoria: 260-2026 (Procuraduría General de la Nación)
--
-- Este script inserta las guías que se auto-cargarían al comprar:
-- Día 1: INTRO-00-PGN (Presentación PGN, no CNSC)
-- Días 2-4: GEN-01, GEN-02, GEN-03 (Generales)
-- Días 5-8: TEC-COM-01, TEC-COM-02, TEC-ESP-01, TEC-ESP-02 (Nivel Técnico)
-- Bonus: BON-01, BON-02
--
-- NO inserta: funcionales (se asignan después), simulacro, ni ENT-PGN-01
-- (esa la asignas desde el desplegable "Conoce tu Entidad" del admin).
-- ============================================================

-- Paso 1: Obtener el curso_id de Sandra
-- (Busca por correo → perfil → curso de la PGN)
DO $$
DECLARE
  v_curso_id uuid;
  v_count int;
BEGIN
  -- Buscar el curso de Sandra (por correo y OPEC del cargo)
  SELECT c.id INTO v_curso_id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'sandrajmarquezp@gmail.com'
    AND c.opec = '260-2026 - 4SU-08'
  ORDER BY c.created_at DESC
  LIMIT 1;

  -- Si no se encontró con ese OPEC exacto, intentar por correo + cargo
  IF v_curso_id IS NULL THEN
    SELECT c.id INTO v_curso_id
    FROM public.cursos c
    JOIN public.profiles p ON p.id = c.usuario_id
    WHERE LOWER(p.correo) = 'sandrajmarquezp@gmail.com'
    ORDER BY c.created_at DESC
    LIMIT 1;
  END IF;

  IF v_curso_id IS NULL THEN
    RAISE EXCEPTION 'No se encontró el curso de Sandra (sandrajmarquezp@gmail.com). Verifica que el curso existe en la tabla cursos.';
  END IF;

  RAISE NOTICE 'Curso encontrado: %', v_curso_id;

  -- Verificar si ya tiene guías cargadas (para no duplicar)
  SELECT COUNT(*) INTO v_count
  FROM public.guias_curso
  WHERE curso_id = v_curso_id;

  IF v_count > 0 THEN
    RAISE NOTICE 'El curso ya tiene % guías cargadas. Se agregarán solo las que falten (sin duplicar).', v_count;
  END IF;

  -- Insertar guías (solo las que NO existan ya por archivo_path)
  INSERT INTO public.guias_curso (curso_id, dia, titulo, tipo, orden, archivo_path)
  SELECT v_curso_id, dia, titulo, tipo::tipo_guia, orden, archivo_path
  FROM (VALUES
    -- Día 1: Presentación PGN
    (1, 'Presentación del Curso y el Concurso de la Procuraduría', 'general', 1, 'guias/INTRO-00-PGN-presentacion-curso-pgn.html'),
    -- Días 2-4: Generales
    (2, 'Estado y Función Pública', 'general', 2, 'guias/GEN-01-estado-funcion-publica.html'),
    (3, 'Relación Estado-Ciudadano', 'general', 3, 'guias/GEN-02-relacion-estado-ciudadano.html'),
    (4, 'Marco Institucional', 'general', 4, 'guias/GEN-03-marco-institucional.html'),
    -- Días 5-8: Nivel Técnico (competencias comportamentales)
    (5, 'Desempeño Individual y Cumplimiento Institucional (Nivel Técnico)', 'nivel', 5, 'guias/TEC-COM-01-desempeno-cumplimiento.html'),
    (6, 'Relación con Usuarios y Trabajo Colaborativo (Nivel Técnico)', 'nivel', 6, 'guias/TEC-COM-02-usuarios-trabajo-colaborativo.html'),
    (7, 'Competencias del Nivel Técnico', 'nivel', 7, 'guias/TEC-ESP-01-competencias-nivel-tecnico.html'),
    (8, 'Alcance del Cargo Técnico', 'nivel', 8, 'guias/TEC-ESP-02-alcance-cargo-tecnico.html'),
    -- Bonus (sin día fijo)
    (NULL::int, 'Estrategia CNSC (Bonus)', 'bonus', 100, 'guias/BON-01-estrategia-cnsc.html'),
    (NULL::int, 'Ofimática (Bonus)', 'bonus', 101, 'guias/BON-02-ofimatica.html')
  ) AS t(dia, titulo, tipo, orden, archivo_path)
  WHERE NOT EXISTS (
    SELECT 1 FROM public.guias_curso gc
    WHERE gc.curso_id = v_curso_id
      AND gc.archivo_path = t.archivo_path
  );

  -- Reportar cuántas se insertaron
  GET DIAGNOSTICS v_count = ROW_COUNT;
  RAISE NOTICE '✅ Se insertaron % guías nuevas en el curso de Sandra.', v_count;

END $$;

-- ============================================================
-- PASO MANUAL ADICIONAL (desde el panel admin):
-- 1. Ir a /admin/cursos/[id-del-curso-de-sandra]
-- 2. En "Conoce tu Entidad", seleccionar ENT-PGN-01 del desplegable
-- 3. Asignar día = 1, orden = 0
-- ============================================================

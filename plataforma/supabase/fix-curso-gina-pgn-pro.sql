-- ============================================================
-- CORRECCIÓN del curso YA cargado de Gina (Procurador Judicial II — PGN)
-- ============================================================
-- Ejecutar UNA VEZ en el SQL Editor de Supabase.
--
-- Qué hace: reemplaza en el curso de Gina las 6 guías que estaban
-- CONTAMINADAS con datos de otro cargo/curso (cargo "Sustanciador 4SU-08",
-- aspirante "Sandra", entidad "URT", "Profesional Especializado", CNSC como
-- organizador) por sus versiones -PRO limpias y específicas del cargo
-- Procurador Judicial II (código 3PJ-EC, Nivel Profesional). También corrige
-- el día de FUN-JUR (19) y de FUN-MP-02 (10) a través del archivo -PRO.
--
-- Gina Alexandra Rojas  (alexandrarojash@gmail.com)
-- Cargo: Procurador Judicial II · Código 3PJ-EC · OPEC 89-2026
-- ============================================================

DO $$
DECLARE
  v_curso_id uuid;
  v_upd int;
  v_dupintro int;
BEGIN
  -- 1) Localizar el curso de Gina (por correo + OPEC; con fallback por correo)
  SELECT c.id INTO v_curso_id
  FROM public.cursos c
  JOIN public.profiles p ON p.id = c.usuario_id
  WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
    AND c.opec = '89-2026 - 3PJ-EC'
  ORDER BY c.created_at DESC
  LIMIT 1;

  IF v_curso_id IS NULL THEN
    SELECT c.id INTO v_curso_id
    FROM public.cursos c
    JOIN public.profiles p ON p.id = c.usuario_id
    WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
    ORDER BY c.created_at DESC
    LIMIT 1;
  END IF;

  IF v_curso_id IS NULL THEN
    RAISE EXCEPTION 'No se encontró el curso de Gina (alexandrarojash@gmail.com).';
  END IF;
  RAISE NOTICE 'Curso de Gina: %', v_curso_id;

  -- 2) Reemplazar las 6 guías contaminadas por las versiones -PRO
  --    (Presentación, Conoce tu Entidad, MP-01, MP-02, Jurídica, Documentos de Oficina)

  UPDATE public.guias_curso SET archivo_path = 'guias/INTRO-00-PGN-PRO-presentacion-curso.html'
   WHERE curso_id = v_curso_id
     AND archivo_path IN (
       'guias/INTRO-00-PGN-presentacion-curso-pgn.html',
       'guias/INTRO-00-presentacion-curso.html'        -- por si el panel cargó la INTRO CNSC genérica
     );

  UPDATE public.guias_curso SET archivo_path = 'guias/ENT-PGN-PRO-01-conoce-entidad-pgn.html'
   WHERE curso_id = v_curso_id
     AND archivo_path = 'guias/ENT-PGN-01-conoce-entidad-pgn.html';

  UPDATE public.guias_curso SET archivo_path = 'guias/FUN-MP-01-PRO-ministerio-publico-estructura-pgn.html'
   WHERE curso_id = v_curso_id
     AND archivo_path = 'guias/FUN-MP-01-ministerio-publico-estructura-pgn.html';

  UPDATE public.guias_curso SET archivo_path = 'guias/FUN-MP-02-PRO-funcion-intervencion-ministerio-publico.html'
   WHERE curso_id = v_curso_id
     AND archivo_path = 'guias/FUN-MP-02-funcion-intervencion-ministerio-publico.html';

  UPDATE public.guias_curso SET archivo_path = 'guias/FUN-JUR-PRO-01-gestion-publica-normatividad-administrativa.html'
   WHERE curso_id = v_curso_id
     AND archivo_path = 'guias/FUN-JUR-01-gestion-publica-normatividad-administrativa.html';

  UPDATE public.guias_curso SET archivo_path = 'guias/FUN-OFI-PRO-01-documentos-oficina-informes-sistemas.html'
   WHERE curso_id = v_curso_id
     AND archivo_path = 'guias/FUN-OFI-02-documentos-oficina-informes-sistemas.html';

  GET DIAGNOSTICS v_upd = ROW_COUNT;
  RAISE NOTICE '✓ Última sentencia UPDATE afectó % fila(s). Revisa el listado final.', v_upd;

  -- 3) Chequeo: ¿quedó alguna guía CNSC genérica (INTRO-00 sin -PGN) colada en el Día 1?
  SELECT COUNT(*) INTO v_dupintro
  FROM public.guias_curso
  WHERE curso_id = v_curso_id
    AND archivo_path = 'guias/INTRO-00-presentacion-curso.html';
  IF v_dupintro > 0 THEN
    RAISE NOTICE '⚠ Aún hay % fila(s) con la INTRO CNSC genérica. Se recomienda revisarlas/eliminarlas.', v_dupintro;
  END IF;
END $$;

-- ============================================================
-- 4) VERIFICACIÓN: listar las guías del curso de Gina tras la corrección.
--    Todas las de las 6 posiciones deben terminar en -PRO / -PGN-PRO.
-- ============================================================
SELECT gc.dia, gc.orden, gc.titulo, gc.archivo_path
FROM public.guias_curso gc
JOIN public.cursos c ON c.id = gc.curso_id
JOIN public.profiles p ON p.id = c.usuario_id
WHERE LOWER(p.correo) = 'alexandrarojash@gmail.com'
ORDER BY gc.orden;

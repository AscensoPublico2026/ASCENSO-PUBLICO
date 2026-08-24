-- ============================================================
-- CREAR (o localizar) el curso de Gina — Procurador Judicial II (PGN)
-- ============================================================
-- Gina Alexandra Rojas · alexandrarojash@gmail.com
-- Cargo: Procurador Judicial II · Código 3PJ-EC · OPEC 89-2026
-- Convocatoria 89-2026 (Res. 212/2026) · Nivel: Profesional
--
-- CONTEXTO: el script de carga de guías falló porque el curso de Gina
-- NO existe todavía en la tabla public.cursos. Este archivo lo crea.
--
-- IMPORTANTE: public.profiles.id referencia a auth.users(id). Por eso
-- Gina debe TENER UNA CUENTA en la plataforma (haberse registrado /
-- iniciado sesión al menos una vez). Si aún no existe su usuario en
-- auth.users, primero pídele que se registre en la plataforma con ese
-- mismo correo, o créalo desde el panel Admin.
-- ============================================================

-- -----------------------------------------------------------
-- PASO 1 (DIAGNÓSTICO): ver qué existe hoy con su correo
-- Ejecuta SOLO este SELECT primero para saber en qué caso estás.
-- -----------------------------------------------------------
SELECT
  u.id                AS auth_user_id,      -- existe cuenta de autenticación?
  p.id                AS profile_id,        -- existe perfil?
  p.nombre, p.correo,
  c.id                AS curso_id,          -- existe curso?
  c.opec, c.nivel, c.estado, c.created_at
FROM auth.users u
LEFT JOIN public.profiles p ON p.id = u.id
LEFT JOIN public.cursos   c ON c.usuario_id = p.id
WHERE LOWER(u.email) = 'alexandrarojash@gmail.com'
   OR LOWER(p.correo) = 'alexandrarojash@gmail.com';

-- Interpreta el resultado del PASO 1:
--   • Si NO devuelve filas  -> Gina no tiene cuenta. Que se registre en la
--     plataforma con ese correo (o créala desde Admin) y repite el PASO 1.
--   • Si devuelve fila con profile_id pero curso_id = NULL -> ve al PASO 2.
--   • Si devuelve fila con curso_id -> el curso YA existe; NO uses el PASO 2,
--     solo ejecuta la migración de guías (migracion-guias-gina-pgn.sql).


-- -----------------------------------------------------------
-- PASO 2 (CREAR EL CURSO): ejecuta este bloque solo si el PASO 1
-- mostró perfil (profile_id) pero SIN curso (curso_id = NULL).
-- Crea el curso de Gina y asegura/actualiza su perfil.
-- -----------------------------------------------------------
DO $$
DECLARE
  v_user_id  uuid;
  v_curso_id uuid;
BEGIN
  -- Ubicar el usuario de autenticación por correo
  SELECT id INTO v_user_id
  FROM auth.users
  WHERE LOWER(email) = 'alexandrarojash@gmail.com'
  LIMIT 1;

  IF v_user_id IS NULL THEN
    RAISE EXCEPTION 'Gina no tiene cuenta en auth.users. Debe registrarse en la plataforma con el correo alexandrarojash@gmail.com (o créala desde el panel Admin) antes de crear el curso.';
  END IF;

  -- Asegurar el perfil (por si el registro no lo generó)
  INSERT INTO public.profiles (id, nombre, correo, rol)
  VALUES (v_user_id, 'Gina Alexandra Rojas', 'alexandrarojash@gmail.com', 'estudiante')
  ON CONFLICT (id) DO UPDATE
    SET nombre = COALESCE(public.profiles.nombre, EXCLUDED.nombre),
        correo = COALESCE(public.profiles.correo, EXCLUDED.correo);

  -- ¿Ya tiene curso?
  SELECT id INTO v_curso_id
  FROM public.cursos
  WHERE usuario_id = v_user_id
  ORDER BY created_at DESC
  LIMIT 1;

  IF v_curso_id IS NOT NULL THEN
    RAISE NOTICE 'Gina ya tiene un curso (%). No se crea otro. Ejecuta la migración de guías.', v_curso_id;
  ELSE
    INSERT INTO public.cursos (usuario_id, opec, cargo_nombre, nivel, estado, fecha_compra)
    VALUES (
      v_user_id,
      '89-2026 - 3PJ-EC',            -- mismo formato usado en el resto de la plataforma
      'Procurador Judicial II',
      'profesional',
      'en_preparacion',
      now()
    )
    RETURNING id INTO v_curso_id;
    RAISE NOTICE '✓ Curso de Gina creado: %', v_curso_id;
  END IF;
END $$;

-- -----------------------------------------------------------
-- PASO 3: una vez creado el curso, ejecuta el archivo
--   plataforma/supabase/migracion-guias-gina-pgn.sql
-- para cargar las 21 sesiones del plan.
-- -----------------------------------------------------------

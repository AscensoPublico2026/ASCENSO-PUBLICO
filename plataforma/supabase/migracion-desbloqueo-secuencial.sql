-- ============================================================
-- Migración: Desbloqueo secuencial de guías (por curso)
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
--
-- En un curso con desbloqueo_secuencial = true, el estudiante ve todo el
-- plan, pero cada guía se abre solo al TERMINAR la anterior (botón
-- "✓ Terminé esta guía" en el visor). Ver plataforma/lib/desbloqueo.ts.
--
-- OPCIONAL: los cursos de OPEC 236897 (Clary) y 236906 (Paula) ya son
-- secuenciales por código (OPECS_SECUENCIALES) aunque no se corra esto.
-- Esta columna sirve para activarlo en otros cursos sin tocar código.
-- ============================================================

alter table public.cursos
  add column if not exists desbloqueo_secuencial boolean not null default false;

update public.cursos
  set desbloqueo_secuencial = true
  where opec in ('236897', '236906');

-- ============================================================
-- Migración: modalidad del curso (21 días o intensivo de 15 días)
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
-- Ejecutar ANTES de crear estudiantes con curso intensivo.
-- ============================================================
alter table public.cursos
  add column if not exists modalidad text not null default '21';

alter table public.cursos
  drop constraint if exists cursos_modalidad_check;
alter table public.cursos
  add constraint cursos_modalidad_check check (modalidad in ('21', '15'));

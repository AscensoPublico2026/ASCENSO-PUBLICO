-- ============================================================
-- Migración: Progreso del estudiante (marcar guías como leídas)
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
-- ============================================================

-- Agregar columna "leida" a guias_curso (si no existe)
alter table public.guias_curso
  add column if not exists leida boolean not null default false;

-- Agregar columna "fecha_leida" para registrar cuándo se leyó (opcional, útil para analytics)
alter table public.guias_curso
  add column if not exists fecha_leida timestamptz;

-- ============================================================
-- Permitir que el estudiante actualice el campo "leida" de SUS propias guías
-- (necesario para marcar guías como leídas desde el visor)
-- ============================================================
drop policy if exists "guias update propia leida" on public.guias_curso;
create policy "guias update propia leida" on public.guias_curso
  for update using (
    public.is_admin() or exists(
      select 1 from public.cursos c
      where c.id = guias_curso.curso_id and c.usuario_id = auth.uid()
    )
  );

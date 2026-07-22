-- ============================================================
-- Ascenso Público — Configuración administrable de cupos
-- Ejecutar una vez en Supabase → SQL Editor → Run.
-- Idempotente: puede volver a ejecutarse sin duplicar datos.
-- ============================================================

-- Singleton de configuración pública del contador de lanzamiento.
create table if not exists public.configuracion_cupos (
  id smallint primary key default 1 check (id = 1),
  vendidos integer not null default 177 check (vendidos >= 0),
  total integer not null default 200 check (total > 0 and vendidos <= total),
  updated_at timestamptz not null default now(),
  updated_by uuid references auth.users(id) on delete set null
);

insert into public.configuracion_cupos (id, vendidos, total)
values (1, 177, 200)
on conflict (id) do nothing;

alter table public.configuracion_cupos enable row level security;

drop policy if exists "configuracion cupos lectura publica" on public.configuracion_cupos;
create policy "configuracion cupos lectura publica" on public.configuracion_cupos
  for select using (true);

drop policy if exists "configuracion cupos admin" on public.configuracion_cupos;
create policy "configuracion cupos admin" on public.configuracion_cupos
  for all using (public.is_admin()) with check (public.is_admin());

comment on table public.configuracion_cupos is
  'Configuración pública del contador de cupos; singleton id=1, editable solo por administradores.';

-- ============================================================
-- Ascenso Público — Configuración de cupos + cédula cifrada
-- Ejecutar una vez en Supabase → SQL Editor → Run.
-- Idempotente: puede volver a ejecutarse sin duplicar datos.
-- ============================================================

-- Cédula: el valor completo se cifra en el servidor antes de llegar a Supabase.
-- En preregistros solo se guardan el texto cifrado y los últimos cuatro dígitos.
alter table public.preregistros
  add column if not exists cedula_encrypted text,
  add column if not exists cedula_last4 varchar(4);

do $$
begin
  if not exists (
    select 1 from pg_constraint
    where conname = 'preregistros_cedula_last4_formato'
      and conrelid = 'public.preregistros'::regclass
  ) then
    alter table public.preregistros
      add constraint preregistros_cedula_last4_formato
      check (cedula_last4 is null or cedula_last4 ~ '^[0-9]{4}$');
  end if;

  if not exists (
    select 1 from pg_constraint
    where conname = 'preregistros_cedula_campos_pareados'
      and conrelid = 'public.preregistros'::regclass
  ) then
    alter table public.preregistros
      add constraint preregistros_cedula_campos_pareados
      check ((cedula_encrypted is null) = (cedula_last4 is null));
  end if;
end $$;

comment on column public.preregistros.cedula_encrypted is
  'Número de cédula cifrado en servidor con AES-256-GCM; nunca guardar texto plano.';
comment on column public.preregistros.cedula_last4 is
  'Últimos 4 dígitos para identificación visual enmascarada.';

-- Las identificaciones de usuarios confirmados viven en una tabla separada y privada.
-- El estudiante no puede leer ni modificar su cédula directamente por la API.
create table if not exists public.identidades_usuarios (
  usuario_id uuid primary key references auth.users(id) on delete cascade,
  cedula_encrypted text not null,
  cedula_last4 varchar(4) not null,
  updated_at timestamptz not null default now(),
  constraint identidades_cedula_last4_formato check (cedula_last4 ~ '^[0-9]{4}$')
);

do $$
begin
  if not exists (
    select 1 from pg_constraint
    where conname = 'identidades_cedula_last4_formato'
      and conrelid = 'public.identidades_usuarios'::regclass
  ) then
    alter table public.identidades_usuarios
      add constraint identidades_cedula_last4_formato
      check (cedula_last4 ~ '^[0-9]{4}$');
  end if;
end $$;

alter table public.identidades_usuarios enable row level security;

drop policy if exists "identidades admin" on public.identidades_usuarios;
create policy "identidades admin" on public.identidades_usuarios
  for all using (public.is_admin()) with check (public.is_admin());

comment on table public.identidades_usuarios is
  'Identificación cifrada; acceso por API limitado a administradores y escrituras internas con service role.';
comment on column public.identidades_usuarios.cedula_encrypted is
  'Número de cédula cifrado en servidor con AES-256-GCM; nunca guardar texto plano.';
comment on column public.identidades_usuarios.cedula_last4 is
  'Últimos 4 dígitos para identificación visual enmascarada.';

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

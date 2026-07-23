-- ============================================================
-- Ascenso Público — Esquema de base de datos (Supabase / PostgreSQL)
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
-- Implementa el modelo de datos de ARQUITECTURA-PLATAFORMA.md (§10).
-- ============================================================

create extension if not exists "pgcrypto";

-- ---------- Tipos (enums) ----------
do $$ begin create type rol_usuario as enum ('estudiante','admin'); exception when duplicate_object then null; end $$;
do $$ begin create type estado_curso as enum ('en_preparacion','listo','vencido'); exception when duplicate_object then null; end $$;
do $$ begin create type estado_conv as enum ('abiertas','cerradas','proxima'); exception when duplicate_object then null; end $$;
do $$ begin create type estado_pago as enum ('pendiente','aprobado','rechazado'); exception when duplicate_object then null; end $$;
do $$ begin create type tipo_guia as enum ('general','nivel','funcional','bonus','simulacro'); exception when duplicate_object then null; end $$;

-- ---------- profiles (extiende auth.users) ----------
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  nombre text,
  correo text,
  celular text,
  rol rol_usuario not null default 'estudiante',
  created_at timestamptz not null default now()
);

-- ---------- convocatorias (gestionadas desde el panel admin) ----------
create table if not exists public.convocatorias (
  id uuid primary key default gen_random_uuid(),
  nombre text not null,
  entidad text,
  estado estado_conv not null default 'proxima',
  etiqueta text,
  vacantes text,
  fecha_prueba_aprox text,
  imagen_url text,
  tema text default 'nacional',
  activa boolean not null default true,
  orden int not null default 0,
  created_at timestamptz not null default now()
);

-- ---------- pre-registros (datos del formulario ANTES de pagar) ----------
create table if not exists public.preregistros (
  id uuid primary key default gen_random_uuid(),
  referencia text unique not null,
  nombre text,
  correo text,
  celular text,
  convocatoria_id uuid references public.convocatorias(id),
  opec text,
  cargo_nombre text,
  nivel text,                       -- asistencial | tecnico | profesional
  manual_pdf_path text,             -- ruta en Storage privado (bucket 'manuales')
  consentimiento boolean not null default false,
  procesado boolean not null default false,
  created_at timestamptz not null default now()
);

-- ---------- cursos ----------
create table if not exists public.cursos (
  id uuid primary key default gen_random_uuid(),
  usuario_id uuid references public.profiles(id) on delete cascade,
  convocatoria_id uuid references public.convocatorias(id),
  opec text,
  numero_inscripcion text,             -- número de inscripción CNSC del candidato (lo agrega el admin)
  cargo_nombre text,
  nivel text,
  manual_pdf_path text,
  estado estado_curso not null default 'en_preparacion',
  fecha_compra timestamptz,
  fecha_vencimiento timestamptz,       -- 60–90 días desde la compra
  preparacion_deadline timestamptz,    -- fecha_compra + 12h (contador del portal)
  progreso_pct int not null default 0,
  created_at timestamptz not null default now()
);

-- ---------- guias_curso ----------
create table if not exists public.guias_curso (
  id uuid primary key default gen_random_uuid(),
  curso_id uuid references public.cursos(id) on delete cascade,
  dia int,
  titulo text not null,
  archivo_path text,                -- ruta en Storage privado (bucket 'guias')
  tipo tipo_guia not null default 'general',
  orden int not null default 0,
  created_at timestamptz not null default now()
);

-- ---------- pagos ----------
create table if not exists public.pagos (
  id uuid primary key default gen_random_uuid(),
  usuario_id uuid references public.profiles(id) on delete set null,
  curso_id uuid references public.cursos(id) on delete set null,
  referencia text unique not null,
  wompi_transaction_id text,
  monto int,                        -- en centavos (COP)
  estado estado_pago not null default 'pendiente',
  created_at timestamptz not null default now()
);

-- ---------- configuración pública de cupos (singleton editable por admin) ----------
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

-- ============================================================
-- Helper: ¿el usuario actual es admin?
-- ============================================================
create or replace function public.is_admin()
returns boolean language sql security definer set search_path = public as $$
  select exists(select 1 from public.profiles where id = auth.uid() and rol = 'admin');
$$;

-- ============================================================
-- Trigger: crear profile automáticamente al registrarse en Auth
-- ============================================================
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into public.profiles (id, nombre, correo)
  values (new.id, new.raw_user_meta_data->>'nombre', new.email)
  on conflict (id) do nothing;
  return new;
end; $$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users for each row execute function public.handle_new_user();

-- ============================================================
-- RLS (seguridad por fila)
-- ============================================================
alter table public.profiles enable row level security;
alter table public.convocatorias enable row level security;
alter table public.preregistros enable row level security;
alter table public.cursos enable row level security;
alter table public.guias_curso enable row level security;
alter table public.pagos enable row level security;
alter table public.configuracion_cupos enable row level security;

-- profiles
drop policy if exists "perfil propio select" on public.profiles;
create policy "perfil propio select" on public.profiles for select using (id = auth.uid() or public.is_admin());
drop policy if exists "perfil propio update" on public.profiles;
create policy "perfil propio update" on public.profiles for update using (id = auth.uid() or public.is_admin());

-- convocatorias: lectura pública (landing); escritura solo admin
drop policy if exists "convocatorias lectura" on public.convocatorias;
create policy "convocatorias lectura" on public.convocatorias for select using (true);
drop policy if exists "convocatorias admin" on public.convocatorias;
create policy "convocatorias admin" on public.convocatorias for all using (public.is_admin()) with check (public.is_admin());

-- preregistros: solo admin (se crean desde el servidor con service role, que omite RLS)
drop policy if exists "preregistros admin" on public.preregistros;
create policy "preregistros admin" on public.preregistros for all using (public.is_admin()) with check (public.is_admin());

-- cursos
drop policy if exists "cursos propios" on public.cursos;
create policy "cursos propios" on public.cursos for select using (usuario_id = auth.uid() or public.is_admin());
drop policy if exists "cursos admin" on public.cursos;
create policy "cursos admin" on public.cursos for all using (public.is_admin()) with check (public.is_admin());

-- guias_curso (el estudiante ve solo las de sus cursos)
drop policy if exists "guias propias" on public.guias_curso;
create policy "guias propias" on public.guias_curso for select using (
  public.is_admin() or exists(select 1 from public.cursos c where c.id = guias_curso.curso_id and c.usuario_id = auth.uid())
);
drop policy if exists "guias admin" on public.guias_curso;
create policy "guias admin" on public.guias_curso for all using (public.is_admin()) with check (public.is_admin());

-- pagos
drop policy if exists "pagos propios" on public.pagos;
create policy "pagos propios" on public.pagos for select using (usuario_id = auth.uid() or public.is_admin());
drop policy if exists "pagos admin" on public.pagos;
create policy "pagos admin" on public.pagos for all using (public.is_admin()) with check (public.is_admin());

-- configuración de cupos: lectura pública; escritura solo admin
drop policy if exists "configuracion cupos lectura publica" on public.configuracion_cupos;
create policy "configuracion cupos lectura publica" on public.configuracion_cupos for select using (true);
drop policy if exists "configuracion cupos admin" on public.configuracion_cupos;
create policy "configuracion cupos admin" on public.configuracion_cupos for all using (public.is_admin()) with check (public.is_admin());

-- ============================================================
-- Storage: buckets PRIVADOS (manuales de funciones y guías)
-- ============================================================
insert into storage.buckets (id, name, public) values ('manuales','manuales', false) on conflict (id) do nothing;
insert into storage.buckets (id, name, public) values ('guias','guias', false) on conflict (id) do nothing;

-- Acceso directo a Storage solo para admin. El estudiante NO accede directo:
-- el servidor genera URLs firmadas temporales para mostrar las guías en un iframe.
drop policy if exists "storage manuales admin" on storage.objects;
create policy "storage manuales admin" on storage.objects
  for all using (bucket_id = 'manuales' and public.is_admin())
  with check (bucket_id = 'manuales' and public.is_admin());
drop policy if exists "storage guias admin" on storage.objects;
create policy "storage guias admin" on storage.objects
  for all using (bucket_id = 'guias' and public.is_admin())
  with check (bucket_id = 'guias' and public.is_admin());

-- ============================================================
-- (Opcional) Convertirte en admin: tras registrarte, ejecuta:
--   update public.profiles set rol = 'admin' where correo = 'ascensopublico@gmail.com';
-- ============================================================


-- ============================================================
-- Migración incremental — ejecutar en Supabase SQL Editor
-- si la base de datos ya existe (no es nueva instalación):
-- ============================================================
-- alter table public.cursos add column if not exists numero_inscripcion text;

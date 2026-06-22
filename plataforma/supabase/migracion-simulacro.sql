-- ============================================================
-- Ascenso Público — Migración: SIMULACRO GRATIS (leads)
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
-- ============================================================

-- Leads capturados al presentar el simulacro gratis.
-- Se insertan desde el servidor (service role), por eso no hay policy pública.
create table if not exists public.leads_simulacro (
  id uuid primary key default gen_random_uuid(),
  nivel text not null,                       -- asistencial | tecnico | profesional
  correo text not null,
  whatsapp text,
  puntaje int,                               -- 0..100
  correctas int,
  total int,
  temas_debiles text[] default '{}',         -- temas a reforzar
  acepta_marketing boolean not null default false,
  consentimiento_fecha timestamptz,
  terminos_version text,                      -- versión de la política aceptada
  user_agent text,
  created_at timestamptz not null default now()
);

create index if not exists idx_leads_simulacro_correo on public.leads_simulacro (correo);
create index if not exists idx_leads_simulacro_creado on public.leads_simulacro (created_at desc);

-- RLS: solo admin puede leer/gestionar. La inserción se hace con service role
-- (createAdminClient) desde la Server Action, que omite RLS.
alter table public.leads_simulacro enable row level security;

do $$ begin
  create policy "leads_simulacro admin" on public.leads_simulacro
    for all using (public.is_admin()) with check (public.is_admin());
exception when duplicate_object then null; end $$;

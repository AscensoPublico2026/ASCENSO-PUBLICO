-- ============================================================
-- Ascenso Público — Migración: ANALÍTICA PROPIA Y ANÓNIMA
-- Ejecutar una vez en Supabase → SQL Editor → Run.
-- No almacena IP, user-agent, correo ni texto escrito en el buscador.
-- ============================================================

create table if not exists public.analytics_events (
  id uuid primary key default gen_random_uuid(),
  event_name text not null check (event_name in (
    'page_view', 'cta_click', 'whatsapp_clicked', 'search_mode_changed',
    'search_used', 'search_zero_results', 'opec_detail_viewed',
    'opec_reference_copied', 'opec_official_clicked', 'simulacro_started',
    'simulacro_progress', 'simulacro_submitted', 'simulacro_completed',
    'simulacro_restarted', 'checkout_form_submitted', 'checkout_started',
    'purchase_completed'
  )),
  anonymous_session_id uuid,
  properties jsonb not null default '{}'::jsonb check (jsonb_typeof(properties) = 'object'),
  event_key text unique,
  occurred_at timestamptz not null default now()
);

create index if not exists idx_analytics_events_occurred_at
  on public.analytics_events (occurred_at desc);
create index if not exists idx_analytics_events_name_date
  on public.analytics_events (event_name, occurred_at desc);
create index if not exists idx_analytics_events_session
  on public.analytics_events (anonymous_session_id)
  where anonymous_session_id is not null;

alter table public.analytics_events enable row level security;

drop policy if exists "analytics admin lectura" on public.analytics_events;
create policy "analytics admin lectura" on public.analytics_events
  for select using (public.is_admin());

drop policy if exists "analytics admin gestion" on public.analytics_events;
create policy "analytics admin gestion" on public.analytics_events
  for delete using (public.is_admin());

comment on table public.analytics_events is
  'Eventos analíticos propios, sin PII ni texto libre; inserción solo desde el servidor con service role.';
comment on column public.analytics_events.anonymous_session_id is
  'Identificador aleatorio de sessionStorage: aproxima sesiones, no identifica personas.';
comment on column public.analytics_events.properties is
  'Propiedades permitidas y saneadas por el servidor; nunca consultas, correos, teléfonos o nombres.';

-- ============================================================
-- Migración: precio por convocatoria
-- Fecha: 2026-10-17
-- Propósito: cada convocatoria define su propio valor a pagar (COP).
--   El formulario /comprar muestra el precio según la convocatoria elegida
--   y el server action lo usa para el checkout de Wompi (ya no es fijo).
--
-- Cómo usar: Supabase → SQL Editor → pega TODO esto → Run.
-- Es idempotente: se puede correr varias veces sin problema.
-- ============================================================

-- 1) Columna de precio (en PESOS COP, no en centavos). Default 200.000.
ALTER TABLE public.convocatorias
  ADD COLUMN IF NOT EXISTS precio_cop integer NOT NULL DEFAULT 200000;

COMMENT ON COLUMN public.convocatorias.precio_cop IS
  'Valor a pagar del curso para esta convocatoria, en pesos COP. Se usa en /comprar y en el checkout de Wompi.';

-- 2) Precios confirmados por convocatoria.
--    DIAN y CNSC (nacionales/territoriales/ESE) = 200.000 ; Procuraduría = 300.000.

-- Procuraduría → 300.000
UPDATE public.convocatorias
  SET precio_cop = 300000
  WHERE nombre ILIKE '%procuradur%';

-- DIAN → 200.000
UPDATE public.convocatorias
  SET precio_cop = 200000
  WHERE nombre ILIKE '%DIAN%';

-- Resto (CNSC: Orden Nacional, Territorial 12, Territorial y UApA, ESE 2) → 200.000
UPDATE public.convocatorias
  SET precio_cop = 200000
  WHERE nombre NOT ILIKE '%procuradur%'
    AND nombre NOT ILIKE '%DIAN%';

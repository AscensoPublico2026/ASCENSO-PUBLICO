-- Migración: agregar campo password a preregistros
-- Fecha: 2026-06-17
-- Propósito: permitir que el cliente defina su contraseña ANTES del pago (en el formulario /comprar)
-- para evitar que pierda acceso si cierra la ventana tras pagar

ALTER TABLE preregistros
ADD COLUMN IF NOT EXISTS password TEXT;

COMMENT ON COLUMN preregistros.password IS 'Contraseña elegida por el cliente en /comprar, antes del pago. Se usa para crear el usuario de Auth tras el pago aprobado.';

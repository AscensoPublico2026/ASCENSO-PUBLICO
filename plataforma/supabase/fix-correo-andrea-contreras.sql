-- ============================================================================
-- Actualizar el correo de Andrea Carolina Contreras
-- Correo nuevo: Andreac.contreras@hotmail.com  (se guarda en minúsculas)
--
-- IMPORTANTE: el correo vive en DOS lugares y ambos deben quedar iguales
-- para que pueda iniciar sesión con el correo nuevo:
--   1) public.profiles.correo   -> lo que muestra la plataforma
--   2) auth.users.email         -> la credencial real de login
--
-- Ejecutar en: Supabase > SQL Editor (en el proyecto de producción).
-- Correr los pasos EN ORDEN y revisar el resultado de cada SELECT antes de
-- ejecutar el UPDATE, para confirmar que es la persona correcta.
-- ============================================================================

-- PASO 1 — Ubicar a Andrea y confirmar su id y su correo actual.
-- (Buscamos por nombre o por el correo que tenga hoy; ajusta si hace falta.)
select id, nombre, correo, celular, rol, created_at
from public.profiles
where nombre ilike '%andrea%'
   or nombre ilike '%contreras%'
order by created_at desc;

-- >>> Copia el UUID correcto de Andrea de la consulta anterior y reemplázalo
--     en los dos UPDATE de abajo (donde dice :ID_ANDREA).

-- PASO 2 — Actualizar el correo en profiles (lo que ve la plataforma).
update public.profiles
set correo = 'andreac.contreras@hotmail.com'
where id = ':ID_ANDREA';   -- << reemplaza por el UUID de Andrea

-- PASO 3 — Actualizar el correo de LOGIN en Supabase Auth.
-- Opción A (recomendada): hacerlo desde el Dashboard
--   Authentication > Users > (buscar a Andrea) > editar Email > Save.
--   Marca el correo como confirmado para que quede usable de inmediato.
--
-- Opción B (SQL directo sobre auth.users; úsala solo si no puedes por el panel):
update auth.users
set email = 'andreac.contreras@hotmail.com',
    email_confirmed_at = coalesce(email_confirmed_at, now())
where id = ':ID_ANDREA';   -- << reemplaza por el UUID de Andrea

-- PASO 4 — Verificar que los dos quedaron iguales.
select p.id, p.nombre, p.correo as correo_profiles, u.email as correo_login
from public.profiles p
join auth.users u on u.id = p.id
where p.id = ':ID_ANDREA';   -- << reemplaza por el UUID de Andrea

-- Listo: Andrea podrá iniciar sesión con andreac.contreras@hotmail.com
-- (su contraseña NO cambia con este script). Si quieres reenviarle las
-- credenciales o la notificación del curso al correo nuevo, hazlo desde el
-- panel admin > Usuarios > (Andrea) > 🔑 Reenviar credenciales / 📧 Reenviar notificación.

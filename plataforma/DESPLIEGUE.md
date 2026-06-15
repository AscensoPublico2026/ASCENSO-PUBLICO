# ✅ Puesta en marcha de la Plataforma (runbook)

Sigue estos pasos en orden. Tiempo aprox: 1–2 horas. Al final tendrás la plataforma en vivo.

> ⚠️ **Importante:** todo el código de `plataforma/` está escrito pero **NO se ha probado** (se generó en un entorno sin internet). Al desplegar es normal encontrar ajustes; ve probando paso a paso. Los puntos marcados con 🔎 conviene verificarlos contra la documentación vigente de Wompi.

---

## Paso 1 — Supabase (base de datos + login + archivos)
1. Crea un proyecto en [supabase.com](https://supabase.com).
2. **SQL Editor** → pega TODO `supabase/schema.sql` → **Run**.
3. **Project Settings → API** → copia: `Project URL`, `anon public key`, `service_role key`.
4. Verifica en **Storage** que existan los buckets privados `manuales` y `guias`.

## Paso 2 — Resend (correos)
1. Crea cuenta en [resend.com](https://resend.com) → **API Keys** → copia la key.
2. (Opcional al inicio) Verifica tu dominio para enviar desde `no-responder@tudominio`. Mientras tanto funciona el remitente de pruebas.

## Paso 3 — Wompi (llaves)
En tu dashboard de Wompi → **Desarrolladores**, copia:
- Llave pública (`pub_...`) y privada (`prv_...`).
- **Secreto de integridad** y **secreto de eventos**.
🔎 Confirma los nombres exactos en el panel de Wompi.

## Paso 4 — Desplegar en Vercel
1. [vercel.com](https://vercel.com) → **Add New → Project** → importa el repo de GitHub.
2. **Root Directory:** `plataforma`.
3. **Environment Variables:** agrega todas las de `.env.example` con tus valores reales:
   - `NEXT_PUBLIC_SUPABASE_URL`, `NEXT_PUBLIC_SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`
   - `NEXT_PUBLIC_WOMPI_PUBLIC_KEY`, `WOMPI_PRIVATE_KEY`, `WOMPI_INTEGRITY_SECRET`, `WOMPI_EVENTS_SECRET`
   - `RESEND_API_KEY`, `ADMIN_EMAIL`
   - `NEXT_PUBLIC_SITE_URL` = tu URL de Vercel (ej. `https://ascenso-publico.vercel.app`)
   - `NEXT_PUBLIC_WOMPI_REDIRECT_URL` = `https://TU-URL/activar`
   - `PRECIO_COP` = `300000`
4. **Deploy.**

## Paso 5 — Webhook de Wompi
En Wompi → configuración de eventos/webhook, apunta a:
```
https://TU-URL/api/webhooks/wompi
```
🔎 Usa el mismo `WOMPI_EVENTS_SECRET` que pusiste en Vercel.

## Paso 6 — Hazte administrador
1. Entra a `https://TU-URL/login` y regístrate una vez (o crea tu cuenta vía el flujo).
   - *(Si no hay registro directo, crea el usuario desde Supabase → Authentication → Add user.)*
2. En Supabase → SQL Editor:
   ```sql
   update public.profiles set rol = 'admin' where correo = 'ascensopublico@gmail.com';
   ```
3. Entra a `https://TU-URL/admin`.

## Paso 7 — Carga inicial
- En `/admin/convocatorias` agrega tus convocatorias reales.
- (Las verás en `/convocatorias`.)

## Paso 8 — Prueba de punta a punta (en SANDBOX de Wompi primero)
1. Ve a `/comprar`, llena el formulario y sube un PDF.
2. Paga con datos de prueba de Wompi (sandbox).
3. Verifica: webhook recibido → en `/admin/cursos` aparece el curso → te llegan los correos.
4. Vuelve del pago a `/activar` → crea contraseña → entra a `/perfil` → ves el curso "en preparación" con la cuenta regresiva de 12h.
5. En `/admin/cursos/[id]` sube una guía HTML y "Habilitar acceso".
6. En `/perfil` el curso pasa a "listo" y abres la guía embebida.
7. Cuando todo funcione en sandbox → cambia las llaves de Wompi a **producción**.

---

## Checklist
- [ ] Supabase creado + schema.sql ejecutado
- [ ] Buckets `manuales` y `guias` (privados)
- [ ] Resend key
- [ ] Wompi: 4 llaves/secretos
- [ ] Vercel desplegado con Root = `plataforma` + variables
- [ ] Webhook configurado
- [ ] Usuario admin (rol = 'admin')
- [ ] Convocatorias cargadas
- [ ] Prueba end-to-end en sandbox OK
- [ ] Llaves Wompi en producción

## Notas de verificación (🔎)
- Formato del evento de Wompi que procesamos: `event === 'transaction.updated'` y `data.transaction.status === 'APPROVED'`. Ajusta en `app/api/webhooks/wompi/route.ts` si tu panel usa otro.
- Firma de integridad (checkout) y firma de eventos (webhook): ver `lib/wompi.ts` y `lib/wompiApi.ts`. Verifica el orden de concatenación con la doc de Wompi vigente.

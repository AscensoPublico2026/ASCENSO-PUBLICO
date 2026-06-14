# 🚀 Plataforma Ascenso Público — Configuración y despliegue

App de la plataforma (portal del estudiante + compra + panel admin), según `../ARQUITECTURA-PLATAFORMA.md`.
**Stack:** Next.js · Supabase · Vercel · Wompi · Resend.

> ⚠️ Este código se escribe en el repo, pero **se instala y despliega en tu computador / en la nube** (el entorno donde se generó no tiene internet). Sigue estos pasos.

---

## 1. Cuentas que debes crear (gratis para empezar)

| Servicio | Para qué | Qué necesitas copiar |
|---|---|---|
| **Supabase** (supabase.com) | Base de datos, login y archivos | `Project URL`, `anon key`, `service_role key` |
| **Vercel** (vercel.com) | Publicar la app (conecta con GitHub) | — (se conecta con tu repo) |
| **Resend** (resend.com) | Correos automáticos | `API key` |
| **Wompi** (ya la tienes) | Pagos | `public key`, `private key`, secreto de integridad y de eventos |

---

## 2. Configurar Supabase
1. Crea un proyecto en Supabase.
2. Ve a **SQL Editor** → pega TODO el contenido de `supabase/schema.sql` → **Run**. Esto crea las tablas, la seguridad (RLS) y los buckets privados.
3. En **Project Settings → API**, copia `URL`, `anon key` y `service_role key`.
4. (Para ser administrador) regístrate luego en la app y ejecuta en SQL Editor:
   ```sql
   update public.profiles set rol = 'admin' where correo = 'ascensopublico@gmail.com';
   ```

## 3. Correr la app en tu computador
Requisitos: **Node.js 18+**.
```bash
cd plataforma
npm install
cp .env.example .env.local      # y rellena tus llaves reales
npm run dev
```
Abre http://localhost:3000

## 4. Variables de entorno
Copia `.env.example` como `.env.local` y rellena con tus llaves (Supabase, Wompi, Resend). **Nunca** subas `.env.local` al repo.

## 5. Desplegar en Vercel
1. En vercel.com → **Add New → Project** → importa tu repo de GitHub.
2. **Root Directory:** selecciona la carpeta `plataforma`.
3. En **Environment Variables**, pega las mismas de tu `.env.local`.
4. **Deploy.** Vercel te da una URL pública (luego conectas tu dominio).

---

## 6. Estructura del proyecto
```
plataforma/
├── app/                 · páginas (Next.js App Router)
│   ├── layout.tsx       · layout raíz + estilos
│   ├── globals.css      · paleta de marca (crema/navy/oro)
│   └── page.tsx         · home (placeholder)
├── lib/supabase/        · clientes de Supabase (navegador, servidor, admin)
├── supabase/schema.sql  · modelo de datos + RLS + buckets
├── .env.example         · plantilla de variables
└── package.json
```

## 7. Estado de construcción (roadmap)
- [x] Cimientos: estructura Next.js, modelo de datos, variables, setup.
- [ ] Convocatorias (lista + detalle)
- [ ] Formulario de compra (datos + PDF + consentimiento)
- [ ] Pago Wompi + webhook
- [ ] Auth (contraseña post-pago + login)
- [ ] Portal del estudiante (estado + contador 12h + guías embebidas)
- [ ] Panel admin
- [ ] Correos (Resend)
- [ ] Legal (privacidad + términos)
- [ ] Despliegue producción

> La construcción avanza por hitos; cada uno se sube al repo para que lo revises.

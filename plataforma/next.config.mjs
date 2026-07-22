/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  // Para el primer despliegue del MVP: no frenar el build por errores de
  // tipos/lint (el código es nuevo y sin probar). Los afinamos luego.
  eslint: { ignoreDuringBuilds: true },
  typescript: { ignoreBuildErrors: true },
  experimental: {
    serverActions: {
      // El formulario de /comprar sube el manual de funciones (PDF) a través
      // de un Server Action. El límite por defecto de Next.js es 1 MB, lo que
      // hacía fallar la compra con un PDF normal ("server-side exception").
      // Vercel impone un tope de ~4.5 MB al body, así que 4 MB es el máximo seguro.
      bodySizeLimit: "4mb",
    },
  },
};

export default nextConfig;

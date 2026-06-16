import type { MetadataRoute } from "next";

const SITE_URL = "https://ascensopublico.com";

export default function robots(): MetadataRoute.Robots {
  return {
    rules: {
      userAgent: "*",
      allow: "/",
      // No indexar rutas privadas ni de API
      disallow: ["/admin", "/api/", "/perfil", "/guia", "/activar", "/reset-password"],
    },
    sitemap: `${SITE_URL}/sitemap.xml`,
  };
}

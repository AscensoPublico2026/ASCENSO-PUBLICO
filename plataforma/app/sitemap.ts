import type { MetadataRoute } from "next";
import opecMeta from "@/data/opec-meta.json";

const SITE_URL = "https://ascensopublico.com";

export default function sitemap(): MetadataRoute.Sitemap {
  return [
    {
      url: SITE_URL,
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 1,
    },
    {
      url: `${SITE_URL}/buscador-opec`,
      lastModified: new Date(`${opecMeta.fechaActualizacion}T12:00:00-05:00`),
      changeFrequency: "daily",
      priority: 0.95,
    },
    {
      url: `${SITE_URL}/convocatorias`,
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 0.9,
    },
    {
      url: `${SITE_URL}/comprar`,
      lastModified: new Date(),
      changeFrequency: "monthly",
      priority: 0.8,
    },
    {
      url: `${SITE_URL}/login`,
      lastModified: new Date(),
      changeFrequency: "yearly",
      priority: 0.3,
    },
  ];
}

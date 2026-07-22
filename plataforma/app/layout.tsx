import type { Metadata } from "next";
import AnalyticsProviders from "./components/AnalyticsProviders";
import "./globals.css";

const SITE_URL = "https://ascensopublico.com";
const TITLE = "Ascenso Público — Curso CNSC personalizado por tu cargo";
const DESCRIPTION =
  "El único curso de la CNSC que estudia el manual de funciones de tu cargo específico. Plan de 21 días, guías y simulacros tipo CNSC según tu OPEC. Prepárate enfocado y gana tu ascenso.";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: {
    default: TITLE,
    template: "%s — Ascenso Público",
  },
  description: DESCRIPTION,
  keywords: [
    "curso concurso de méritos CNSC",
    "preparación prueba escrita CNSC",
    "simulacro CNSC 2026",
    "curso personalizado por cargo CNSC",
    "ascenso público",
    "OPEC",
    "manual de funciones",
    "concurso de ascenso CNSC",
  ],
  authors: [{ name: "Ascenso Público" }],
  icons: {
    icon: [
      { url: "/favicon.svg", type: "image/svg+xml" },
      { url: "/favicon-64.png", sizes: "64x64", type: "image/png" },
      { url: "/favicon-32.png", sizes: "32x32", type: "image/png" },
    ],
    apple: "/favicon-64.png",
  },
  openGraph: {
    type: "website",
    locale: "es_CO",
    url: SITE_URL,
    siteName: "Ascenso Público",
    title: "Ascenso Público — Estudia para tu cargo, no para toda la convocatoria",
    description: DESCRIPTION,
    images: [
      {
        url: "/fotos/hero.jpg",
        width: 1200,
        height: 630,
        alt: "Ascenso Público — Preparación personalizada para concursos CNSC",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Ascenso Público — Estudia para tu cargo, no para toda la convocatoria",
    description: DESCRIPTION,
    images: ["/fotos/hero.jpg"],
  },
  robots: {
    index: true,
    follow: true,
  },
  alternates: {
    canonical: SITE_URL,
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>
        {children}
        <AnalyticsProviders />
      </body>
    </html>
  );
}

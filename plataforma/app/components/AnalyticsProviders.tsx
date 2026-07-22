"use client";

import Link from "next/link";
import Script from "next/script";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
import { isAnalyticsEventName, trackEvent } from "@/lib/analytics";

const CONSENT_KEY = "ascenso_analytics_consent_v1";
type Consent = "accepted" | "anonymous" | "declined" | null;

function readConsent(): Consent {
  if (typeof window === "undefined") return null;
  const value = window.localStorage.getItem(CONSENT_KEY);
  if (value === "necessary") {
    window.localStorage.setItem(CONSENT_KEY, "anonymous");
    return "anonymous";
  }
  return value === "accepted" || value === "anonymous" || value === "declined" ? value : null;
}

export default function AnalyticsProviders() {
  const pathname = usePathname();
  const [consent, setConsent] = useState<Consent>(null);
  const gaId = process.env.NEXT_PUBLIC_GA_MEASUREMENT_ID;
  const clarityId = process.env.NEXT_PUBLIC_CLARITY_PROJECT_ID;
  const clarityAllowed = !["/comprar", "/activar", "/login", "/reset-password", "/perfil", "/admin"]
    .some((route) => pathname.startsWith(route));

  useEffect(() => setConsent(readConsent()), []);

  useEffect(() => {
    if (consent !== "accepted" && consent !== "anonymous") return;
    trackEvent("page_view", {
      path: pathname,
      page_title: document.title,
    });
  }, [consent, pathname]);

  useEffect(() => {
    if (consent !== "accepted" && consent !== "anonymous") return;
    const onClick = (event: MouseEvent) => {
      const target = event.target instanceof Element
        ? event.target.closest<HTMLElement>("[data-analytics-event]")
        : null;
      if (!target) return;

      const eventName = target.dataset.analyticsEvent;
      if (!isAnalyticsEventName(eventName)) return;

      let destination: string | undefined;
      if (target instanceof HTMLAnchorElement) {
        try {
          const url = new URL(target.href, window.location.origin);
          destination = url.origin === window.location.origin ? url.pathname : url.hostname;
        } catch {
          destination = undefined;
        }
      }

      trackEvent(eventName, {
        placement: target.dataset.analyticsPlacement || null,
        level: target.dataset.analyticsLevel || null,
        destination: destination || null,
        source: "click",
      });
    };

    document.addEventListener("click", onClick);
    return () => document.removeEventListener("click", onClick);
  }, [consent]);

  function saveConsent(value: Exclude<Consent, null>) {
    window.localStorage.setItem(CONSENT_KEY, value);
    setConsent(value);
  }

  return (
    <>
      {consent === "accepted" && gaId && (
        <>
          <Script src={`https://www.googletagmanager.com/gtag/js?id=${gaId}`} strategy="afterInteractive" />
          <Script id="ga4-config" strategy="afterInteractive">
            {`window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}window.gtag=gtag;gtag('js',new Date());gtag('config','${gaId}',{anonymize_ip:true});`}
          </Script>
        </>
      )}

      {consent === "accepted" && clarityId && clarityAllowed && (
        <Script id="clarity-config" strategy="afterInteractive">
          {`(function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};t=l.createElement(r);t.async=1;t.src='https://www.clarity.ms/tag/'+i;y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y)})(window,document,'clarity','script','${clarityId}');`}
        </Script>
      )}

      {consent === null && (
        <aside
          role="dialog"
          aria-label="Preferencias de analítica"
          style={{
            position: "fixed", left: 16, right: 16, bottom: 16, zIndex: 10000,
            maxWidth: 760, margin: "0 auto", padding: "18px 20px", borderRadius: 16,
            background: "#071A3D", color: "#fff", boxShadow: "0 12px 40px rgba(0,0,0,.3)",
            display: "flex", gap: 18, alignItems: "center", flexWrap: "wrap",
          }}
        >
          <div style={{ flex: "1 1 360px" }}>
            <strong style={{ display: "block", marginBottom: 4 }}>Ayúdanos a mejorar Ascenso Público</strong>
            <span style={{ fontSize: ".83rem", color: "rgba(255,255,255,.82)", lineHeight: 1.5 }}>
              Tú eliges: podemos usar solo métricas propias anónimas o, con tu permiso, añadir Google
              Analytics y Microsoft Clarity para entender recorridos y clics. Nunca registramos lo que
              escribes en el buscador; Clarity se desactiva en compra, acceso, perfil y administración. {" "}
              <Link href="/privacidad" style={{ color: "#F4C26B", textDecoration: "underline" }}>Más información</Link>
            </span>
          </div>
          <div style={{ display: "flex", gap: 9, flexWrap: "wrap" }}>
            <button
              type="button"
              onClick={() => saveConsent("declined")}
              style={{ border: 0, background: "transparent", color: "rgba(255,255,255,.8)", padding: "10px 4px", fontWeight: 700, cursor: "pointer" }}
            >
              No permitir
            </button>
            <button
              type="button"
              onClick={() => saveConsent("anonymous")}
              style={{ border: "1px solid rgba(255,255,255,.45)", background: "transparent", color: "#fff", borderRadius: 9, padding: "10px 13px", fontWeight: 700, cursor: "pointer" }}
            >
              Solo anónima
            </button>
            <button
              type="button"
              onClick={() => saveConsent("accepted")}
              style={{ border: 0, background: "#E8A33D", color: "#071A3D", borderRadius: 9, padding: "10px 14px", fontWeight: 800, cursor: "pointer" }}
            >
              Aceptar todo
            </button>
          </div>
        </aside>
      )}
    </>
  );
}

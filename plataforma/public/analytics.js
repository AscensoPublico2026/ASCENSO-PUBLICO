(function () {
  "use strict";

  var CONSENT_KEY = "ascenso_analytics_consent_v1";
  var SESSION_KEY = "ascenso_analytics_session";

  function consent() {
    try {
      var value = window.localStorage.getItem(CONSENT_KEY);
      if (value === "necessary") {
        window.localStorage.setItem(CONSENT_KEY, "anonymous");
        return "anonymous";
      }
      return value;
    } catch (_) {
      return null;
    }
  }

  function analyticsAllowed() {
    var value = consent();
    return value === "accepted" || value === "anonymous";
  }

  function sessionId() {
    if (!analyticsAllowed()) return null;
    try {
      var current = window.sessionStorage.getItem(SESSION_KEY);
      if (current) return current;
      var created = window.crypto.randomUUID();
      window.sessionStorage.setItem(SESSION_KEY, created);
      return created;
    } catch (_) {
      return null;
    }
  }

  function cleanProperties(properties) {
    var allowed = [
      "path", "page_title", "source", "placement", "destination", "level", "mode",
      "criteria_count", "has_location", "query_length_bucket", "result_count",
      "convocatoria_id", "employment_level", "empleo_id", "referencia", "answered",
      "total", "percentage", "milestone", "value", "currency"
    ];
    var result = {};
    Object.keys(properties || {}).slice(0, 24).forEach(function (key) {
      if (allowed.indexOf(key) === -1) return;
      var value = properties[key];
      if (typeof value === "string") result[key] = value.slice(0, 120);
      else if (typeof value === "number" && isFinite(value)) result[key] = value;
      else if (typeof value === "boolean" || value === null) result[key] = value;
    });
    result.path = result.path || window.location.pathname.slice(0, 200);
    return result;
  }

  function track(eventName, properties) {
    if (!analyticsAllowed()) return;
    var body = JSON.stringify({
      event_name: eventName,
      anonymous_session_id: sessionId(),
      properties: cleanProperties(properties || {})
    });

    try {
      fetch("/api/analytics/events", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "same-origin",
        keepalive: true,
        body: body
      }).catch(function () {});
    } catch (_) {}
  }

  function saveConsent(value, banner) {
    try { window.localStorage.setItem(CONSENT_KEY, value); } catch (_) {}
    if (banner) banner.remove();
    if (value === "accepted" || value === "anonymous") {
      track("page_view", { page_title: document.title });
      window.dispatchEvent(new CustomEvent("ascenso:analytics-consent"));
    }
  }

  function consentButton(text, value, primary) {
    var button = document.createElement("button");
    button.type = "button";
    button.textContent = text;
    button.style.cssText = primary
      ? "border:0;background:#E8A33D;color:#071A3D;border-radius:8px;padding:9px 12px;font-weight:800;cursor:pointer"
      : "border:1px solid rgba(255,255,255,.45);background:transparent;color:#fff;border-radius:8px;padding:9px 12px;font-weight:700;cursor:pointer";
    button.setAttribute("data-consent-value", value);
    return button;
  }

  function showConsentBanner() {
    var banner = document.createElement("aside");
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Preferencias de analítica");
    banner.style.cssText = "position:fixed;left:14px;right:14px;bottom:14px;z-index:10000;max-width:760px;margin:auto;padding:16px 18px;border-radius:14px;background:#071A3D;color:#fff;box-shadow:0 12px 40px rgba(0,0,0,.3);font-family:Inter,sans-serif";
    banner.innerHTML = '<strong style="display:block;margin-bottom:4px">Ayúdanos a mejorar Ascenso Público</strong><p style="font-size:.8rem;line-height:1.5;color:rgba(255,255,255,.82);margin:0 0 12px">Puedes permitir métricas propias anónimas, aceptar toda la analítica o continuar sin medición. No registramos tus respuestas, correo, teléfono ni el texto que escribes.</p>';
    var actions = document.createElement("div");
    actions.style.cssText = "display:flex;gap:8px;flex-wrap:wrap";
    var decline = consentButton("No permitir", "declined", false);
    var anonymous = consentButton("Solo anónima", "anonymous", false);
    var accept = consentButton("Aceptar todo", "accepted", true);
    [decline, anonymous, accept].forEach(function (button) {
      button.addEventListener("click", function () {
        saveConsent(button.getAttribute("data-consent-value"), banner);
      });
      actions.appendChild(button);
    });
    banner.appendChild(actions);
    document.body.appendChild(banner);
  }

  window.ascensoAnalytics = { track: track };

  document.addEventListener("DOMContentLoaded", function () {
    if (consent() === null) showConsentBanner();
    else track("page_view", { page_title: document.title });

    document.addEventListener("click", function (event) {
      var target = event.target && event.target.closest
        ? event.target.closest("[data-analytics-event]")
        : null;
      if (!target) return;
      var destination = null;
      if (target.href) {
        try {
          var url = new URL(target.href, window.location.origin);
          destination = url.origin === window.location.origin ? url.pathname : url.hostname;
        } catch (_) {}
      }
      track(target.getAttribute("data-analytics-event"), {
        placement: target.getAttribute("data-analytics-placement"),
        level: target.getAttribute("data-analytics-level"),
        destination: destination,
        source: "click"
      });
    });
  });
})();

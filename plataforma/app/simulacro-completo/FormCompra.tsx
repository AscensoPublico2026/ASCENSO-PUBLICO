"use client";

import { useEffect, useState } from "react";
import { useFormState, useFormStatus } from "react-dom";
import { iniciarCompraSimulacro, type EstadoCompra } from "./actions";
import type { ProductoSimulacro } from "@/lib/simulacroPago";
import { waUrl, WA_MENSAJES } from "@/lib/contacto";

function Boton() {
  const { pending } = useFormStatus();
  return (
    <button type="submit" className="btn btn-oro simc-submit" disabled={pending}>
      {pending ? "Abriendo el pago seguro…" : "Pagar $39.000 y presentarlo"}
    </button>
  );
}

export default function FormCompra({ productos }: { productos: ProductoSimulacro[] }) {
  const disponibles = productos.filter((p) => p.disponible);
  const [elegido, setElegido] = useState(disponibles[0]?.id ?? "");
  const [state, formAction] = useFormState<EstadoCompra, FormData>(iniciarCompraSimulacro, {});

  // Cuando el servidor devuelve la URL del checkout, llevamos al comprador a Wompi.
  useEffect(() => {
    if (state?.url) window.location.href = state.url;
  }, [state?.url]);

  return (
    <form action={formAction} className="simc-form" id="comprar">
      <h3>Elige tu simulacro</h3>

      <div className="simc-opciones">
        {productos.map((p) => (
          <label
            key={p.id}
            className={`simc-opcion${elegido === p.id ? " activa" : ""}${p.disponible ? "" : " bloqueada"}`}
          >
            <input
              type="radio"
              name="producto"
              value={p.id}
              checked={elegido === p.id}
              disabled={!p.disponible}
              onChange={() => setElegido(p.id)}
            />
            <span className="simc-opcion-txt">
              <b>{p.convocatoria}</b>
              <em>{p.nivel}</em>
            </span>
            {p.disponible ? (
              <span className="simc-opcion-tag">Disponible</span>
            ) : (
              <span className="simc-opcion-tag proximo">Próximamente</span>
            )}
          </label>
        ))}
      </div>

      <div className="simc-campos">
        <label>
          Nombre completo
          <input name="nombre" type="text" autoComplete="name" required placeholder="Como aparece en tu cédula" />
        </label>
        <label>
          Correo
          <input name="correo" type="email" autoComplete="email" required placeholder="Ahí te llega el acceso" />
        </label>
        <label>
          Celular
          <input name="celular" type="tel" inputMode="numeric" autoComplete="tel" required placeholder="3001234567" />
        </label>
      </div>

      {state?.error && <p className="simc-error">{state.error}</p>}

      <Boton />
      <p className="simc-metodos">Pagas con <strong>PSE, Nequi, Bancolombia o tarjeta</strong> en la pasarela segura de Wompi. El acceso te llega apenas se aprueba el pago.</p>

      <a href={waUrl(WA_MENSAJES.simulacroPago)} target="_blank" rel="noopener" className="simc-wa" data-analytics-event="whatsapp_clicked" data-analytics-placement="simc_fallback">
        ¿Prefieres pagarlo por WhatsApp? Escríbenos
      </a>
    </form>
  );
}

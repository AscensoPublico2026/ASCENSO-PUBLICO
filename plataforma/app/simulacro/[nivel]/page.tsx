import { notFound } from "next/navigation";
import type { Metadata } from "next";
import { preguntasDeNivel, esNivelValido, nombreNivel } from "@/lib/simulacro/preguntas";
import SimulacroQuiz from "../SimulacroQuiz";
import "../../landing.css";
import "../simulacro.css";

export function generateStaticParams() {
  return [{ nivel: "asistencial" }, { nivel: "tecnico" }, { nivel: "profesional" }];
}

export function generateMetadata({ params }: { params: { nivel: string } }): Metadata {
  if (!esNivelValido(params.nivel)) return { title: "Simulacro | Ascenso Público" };
  return {
    title: `Simulacro CNSC nivel ${nombreNivel(params.nivel)} (gratis) | Ascenso Público`,
    description: `Simulacro gratis para el nivel ${nombreNivel(params.nivel)}. Mide tu conocimiento y recibe retroalimentación.`,
  };
}

export default function SimulacroNivelPage({ params }: { params: { nivel: string } }) {
  if (!esNivelValido(params.nivel)) notFound();

  const preguntas = preguntasDeNivel(params.nivel);

  return (
    <SimulacroQuiz
      nivel={params.nivel}
      nivelNombre={nombreNivel(params.nivel)}
      preguntas={preguntas}
    />
  );
}

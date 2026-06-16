/**
 * Script para subir las guías HTML al bucket 'guias' de Supabase Storage.
 * 
 * USO:
 * 1. Instala dependencias: npm install (en /plataforma)
 * 2. Crea un archivo .env.local con tus variables de Supabase
 * 3. Ejecuta: node scripts/subir-guias.mjs
 * 
 * También puedes pasarlas como variables de entorno:
 *   NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co \
 *   SUPABASE_SERVICE_ROLE_KEY=eyJxxx... \
 *   node scripts/subir-guias.mjs
 */

import { createClient } from "@supabase/supabase-js";
import { readFileSync, existsSync } from "fs";
import { resolve, basename } from "path";

// Cargar .env.local si existe
const envPath = resolve(process.cwd(), ".env.local");
if (existsSync(envPath)) {
  const lines = readFileSync(envPath, "utf-8").split("\n");
  for (const line of lines) {
    const [key, ...val] = line.split("=");
    if (key && val.length > 0) process.env[key.trim()] = val.join("=").trim();
  }
}

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL;
const SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;

if (!SUPABASE_URL || !SERVICE_ROLE_KEY) {
  console.error("❌ Falta NEXT_PUBLIC_SUPABASE_URL o SUPABASE_SERVICE_ROLE_KEY");
  console.error("   Agrégalas en .env.local o pásalas como variables de entorno.");
  process.exit(1);
}

const supabase = createClient(SUPABASE_URL, SERVICE_ROLE_KEY);

// Lista de guías a subir (ruta local → ruta en Storage)
const GUIAS = [
  "guias/INTRO-00-presentacion-curso.html",
  "guias/GEN-01-estado-funcion-publica.html",
  "guias/GEN-02-relacion-estado-ciudadano.html",
  "guias/GEN-03-marco-institucional.html",
  "guias/ASI-COM-01-cumplimiento-desarrollo-laboral.html",
  "guias/ASI-COM-02-atencion-colaboracion.html",
  "guias/ASI-ESP-01-competencias-nivel-asistencial.html",
  "guias/ASI-ESP-02-alcance-cargo-asistencial.html",
  "guias/TEC-COM-01-desempeno-cumplimiento.html",
  "guias/TEC-COM-02-usuarios-trabajo-colaborativo.html",
  "guias/TEC-ESP-01-competencias-nivel-tecnico.html",
  "guias/TEC-ESP-02-alcance-cargo-tecnico.html",
  "guias/PRO-COM-01-gestion-cumplimiento.html",
  "guias/PRO-COM-02-servicio-articulacion.html",
  "guias/PRO-ESP-01-competencias-nivel-profesional.html",
  "guias/PRO-ESP-02-alcance-cargo-profesional.html",
  "guias/BON-01-estrategia-cnsc.html",
];

async function main() {
  console.log(`📚 Subiendo ${GUIAS.length} guías al bucket 'guias' de Supabase...\n`);

  let ok = 0;
  let fail = 0;

  for (const storagePath of GUIAS) {
    // El archivo local está en la raíz del repo (../guias/xxx.html desde plataforma/)
    const localPath = resolve(process.cwd(), "..", storagePath);
    
    if (!existsSync(localPath)) {
      console.log(`  ⚠️  No existe: ${localPath}`);
      fail++;
      continue;
    }

    const content = readFileSync(localPath);
    
    const { error } = await supabase.storage
      .from("guias")
      .upload(storagePath, content, {
        contentType: "text/html; charset=utf-8",
        upsert: true, // sobrescribe si ya existe
      });

    if (error) {
      console.log(`  ❌ Error: ${storagePath} → ${error.message}`);
      fail++;
    } else {
      console.log(`  ✅ ${storagePath}`);
      ok++;
    }
  }

  console.log(`\n📊 Resultado: ${ok} subidas, ${fail} errores.`);
  if (ok === GUIAS.length) {
    console.log("🎉 ¡Todas las guías están en el bucket!");
  }
}

main().catch(console.error);

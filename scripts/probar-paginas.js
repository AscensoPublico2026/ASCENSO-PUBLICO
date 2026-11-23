// Prueba en navegador (Chromium) de guías/simulacros: errores JS, clic en cada pregunta, retroalimentación visible.
// Uso: node scripts/probar-paginas.js archivo1.html [archivo2.html ...]
const {chromium}=require('playwright'); const path=require('path');
(async()=>{const b=await chromium.launch(); let malos=0;
for(const f of process.argv.slice(2)){
  const p=await b.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.on('dialog',d=>d.dismiss());
  await p.goto('file://'+path.resolve(f)); await p.waitForTimeout(300);
  const r=await p.evaluate(()=>{const Q=[...document.querySelectorAll('.pregunta')];let sinFb=0;
    document.querySelectorAll('.section').forEach(s=>s.classList.add('visible'));
    Q.forEach(q=>{const o=q.querySelector('.opcion');if(o)o.click();const fb=q.querySelector('.feedback');if(!fb||fb.textContent.trim().length<10)sinFb++;});
    return {n:Q.length,sinFb}});
  const ok=!errs.length && r.sinFb===0; if(!ok) malos++;
  console.log((ok?'OK   ':'FALLA')+' '+f+' preguntas='+r.n+' sin_retro='+r.sinFb+(errs.length?' errores='+JSON.stringify(errs.slice(0,2)):''));
  await p.close();}
await b.close(); process.exit(malos?1:0);})();

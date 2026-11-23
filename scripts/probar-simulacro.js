// Verifica un simulacro en navegador: que rendericen las preguntas y los items
// comportamentales, y que no haya errores de página.
// Uso: node scripts/probar-simulacro.js simulacro/SIM-....html
const {chromium} = require('playwright');
(async () => {
  const f = process.argv[2];
  const b = await chromium.launch();
  const p = await b.newPage();
  const errs = [];
  p.on('pageerror', e => errs.push('pageerror: ' + e.message));
  p.on('console', m => { if (m.type() === 'error' && !/fonts\.googleapis|ERR_TUNNEL/.test(m.text())) errs.push('console: ' + m.text()); });
  await p.goto('file://' + require('path').resolve(f));
  await p.waitForTimeout(1200);

  const nFunc = await p.locator('.question-card').count();
  // responder todas las funcionales eligiendo la primera opción de cada una
  const opts = p.locator('.question-card .option');
  const nOpt = await opts.count();
  for (let i = 0; i < nOpt; i += 4) { try { await opts.nth(i).click({timeout: 1500}); } catch (e) {} }
  await p.waitForTimeout(400);

  // pasar al panel comportamental
  const tabs = p.locator('.tab-btn');
  const nTabs = await tabs.count();
  if (nTabs > 1) { await tabs.nth(1).click(); await p.waitForTimeout(500); }
  const nLik = await p.locator('.likert-card').count();

  console.log((errs.length ? 'ERRORES' : 'OK') + '  ' + f);
  console.log('  bloques funcionales detectados: ' + nFunc + ' · opciones: ' + nOpt + ' · items comportamentales: ' + nLik);
  errs.slice(0, 6).forEach(e => console.log('  ' + e));
  await b.close();
  process.exit(errs.length ? 1 : 0);
})();

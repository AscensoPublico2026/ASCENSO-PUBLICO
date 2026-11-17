"""Añade a los simulacros gratis la barra de examen: cronómetro, progreso en
vivo y una nota honesta de que son un diagnóstico corto frente a la prueba real.

Es idempotente: se puede volver a ejecutar después de regenerar los simulacros.
Uso: python3 scripts/mejorar_simulacros.py
"""
import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parent.parent / "public" / "simulacro-gratis"
MARCA = "<!-- ap-barra-examen -->"

CSS = """
<style>/* ap-barra-examen */
.ap-barra{position:sticky;top:0;z-index:500;background:#0A2A5E;color:#fff;
  box-shadow:0 2px 14px rgba(6,24,52,.35);}
.ap-barra-in{max-width:860px;margin:0 auto;display:flex;align-items:center;gap:16px;
  padding:10px 20px;flex-wrap:wrap;}
.ap-barra-t{font-weight:800;font-size:.86rem;letter-spacing:.02em;margin-right:auto;}
.ap-barra-dato{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.1);
  border:1px solid rgba(255,255,255,.18);border-radius:30px;padding:5px 13px;font-size:.84rem;
  font-weight:700;font-variant-numeric:tabular-nums;}
.ap-barra-dato b{color:#F6C56B;}
.ap-barra-prog{width:100%;height:4px;background:rgba(255,255,255,.16);}
.ap-barra-prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,#E8A33D,#F6C56B);
  transition:width .3s;}
.ap-aviso{background:#FDF4E3;border:1px solid #F0DCB0;border-left:4px solid #E8A33D;
  border-radius:12px;padding:14px 18px;margin:0 0 24px;color:#5B4A2A;font-size:.9rem;line-height:1.55;}
.ap-aviso b{color:#8A5A12;}
@media(max-width:560px){.ap-barra-t{width:100%;margin-bottom:4px;}}
</style>
"""

BARRA = """<!-- ap-barra-examen -->
<div class="ap-barra">
  <div class="ap-barra-in">
    <span class="ap-barra-t">Simulacro en curso</span>
    <span class="ap-barra-dato">⏱ <b id="apTiempo">00:00</b></span>
    <span class="ap-barra-dato">✍️ <b id="apProg">0</b> / <span id="apTotal">20</span></span>
  </div>
  <div class="ap-barra-prog"><i id="apProgBar"></i></div>
</div>
"""

AVISO = """<div class="ap-aviso">
<b>Esto es un diagnóstico, no el examen.</b> La prueba real es mucho más larga y se presenta
en una sola sesión con tiempo límite. Aquí medimos tu criterio con 20 casos del mismo tipo:
tres opciones plausibles, como en la Prueba de Juicio Situacional, donde la trampa es la
respuesta «casi correcta».
</div>
"""

JS = """
<script>/* ap-barra-examen */
(function(){
  var ini=Date.now(), corriendo=true, elTiempo=document.getElementById('apTiempo'),
      elProg=document.getElementById('apProg'), elTotal=document.getElementById('apTotal'),
      elBar=document.getElementById('apProgBar');
  function dos(n){return (n<10?'0':'')+n;}
  function tick(){
    if(corriendo && elTiempo){
      var s=Math.floor((Date.now()-ini)/1000);
      elTiempo.textContent=dos(Math.floor(s/60))+':'+dos(s%60);
    }
    var total=document.querySelectorAll('.question-card').length||20;
    var hechas=document.querySelectorAll('.option.selected').length;
    if(elTotal) elTotal.textContent=total;
    if(elProg) elProg.textContent=hechas;
    if(elBar) elBar.style.width=(total?Math.round(hechas/total*100):0)+'%';
    var area=document.getElementById('quizArea');
    if(area && area.style.display==='none') corriendo=false;
  }
  setInterval(tick,400); tick();
})();
</script>
"""


def mejorar(p: pathlib.Path) -> str:
    s = p.read_text(encoding="utf-8")
    if MARCA in s:
        return "ya estaba"
    s = s.replace("</head>", CSS + "</head>", 1)
    s = re.sub(r"(<body[^>]*>)", r"\1" + BARRA, s, count=1)
    s = s.replace('<div id="quizArea">', AVISO + '<div id="quizArea">', 1)
    s = s.replace("</body>", JS + "</body>", 1)
    p.write_text(s, encoding="utf-8")
    return "ok"


for f in sorted(BASE.glob("*.html")):
    print(mejorar(f), f.name)

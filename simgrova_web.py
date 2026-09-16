import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SIMGROVA | Mekanisk udvikling", page_icon="⚙️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
html,body,[data-testid="stAppViewContainer"],.stApp{background:#ffffff!important}
[data-testid="stHeader"],[data-testid="stToolbar"],#MainMenu,footer{visibility:hidden}
.block-container{max-width:100%!important;padding:0!important}
iframe{display:block}
</style>
""", unsafe_allow_html=True)

page = r"""
<!doctype html><html lang="da"><head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{--paper:#ffffff;--ink:#20353a;--muted:#68797b;--line:#ccd6d2;--blue:#347e8c;--blue2:#8cb8bd;--warm:#d28a57;--green:#799b80;--panel:#e9ece5}
*{box-sizing:border-box} html{scroll-behavior:smooth}
body{margin:0;background:#ffffff;color:var(--ink);font-family:Arial,sans-serif}
.shell{width:100%;max-width:1440px;margin:0 auto;padding:0 clamp(28px,5vw,78px)}
header{height:78px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line);position:sticky;top:0;background:rgba(244,242,235,.96);z-index:30}
.brand{font-size:20px;font-weight:700;letter-spacing:.16em}.brand small{font:10px monospace;color:var(--blue);margin-left:12px}
nav{display:flex;gap:25px} nav button,.ghost{border:0;background:transparent;cursor:pointer;font:11px monospace;letter-spacing:.09em;color:var(--muted)}
nav button:hover{color:var(--blue)}
.hero{min-height:690px;display:grid;grid-template-columns:42% 58%;align-items:center}
.kicker{font:11px monospace;letter-spacing:.18em;color:var(--blue);margin-bottom:20px}
h1{font-size:clamp(31px,3.0vw,46px);font-weight:400;line-height:1.05;letter-spacing:-.035em;margin:0 0 22px;max-width:650px}
.lead{font-size:clamp(16px,1.3vw,20px);line-height:1.6;color:#5d6e70;max-width:600px}
.actions{display:flex;gap:12px;margin-top:30px;flex-wrap:wrap}
.btn{border:1px solid var(--blue);background:var(--blue);color:white;padding:13px 17px;font:11px monospace;letter-spacing:.08em;cursor:pointer}
.btn.alt{background:transparent;color:var(--blue)} .btn:hover{filter:brightness(.96)}
.visual{height:560px;position:relative;border-left:1px solid var(--line);overflow:hidden}
.hero-svg{width:100%;height:100%}.mechanic{stroke:var(--blue);stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}.soft{stroke:var(--blue2);stroke-width:1.4;fill:none}.dim{stroke:#91a6a5;stroke-width:1;fill:none}.warm{stroke:var(--warm);stroke-width:2;fill:none}.label{font:11px monospace;fill:#657779;letter-spacing:1px}
.carriage{animation:carriage 6s ease-in-out infinite alternate}.lift{animation:lift 6s ease-in-out infinite alternate}.wheel{transform-origin:465px 300px;animation:spin 9s linear infinite}
@keyframes carriage{from{transform:translateX(-50px)}to{transform:translateX(60px)}} @keyframes lift{from{transform:translateY(12px)}to{transform:translateY(-35px)}} @keyframes spin{to{transform:rotate(360deg)}}
.section{padding:88px 0;border-top:1px solid var(--line)} .section-title{max-width:850px;margin-bottom:42px}
h2{font-size:clamp(34px,3.4vw,54px);font-weight:400;letter-spacing:-.035em;margin:8px 0 14px}.section-title p{color:var(--muted);line-height:1.65}
.cards{display:grid;grid-template-columns:repeat(4,1fr);border:1px solid var(--line)}
.card{padding:27px;min-height:250px;border-right:1px solid var(--line);cursor:pointer;transition:.2s}.card:last-child{border-right:0}.card:hover,.card.active{background:var(--panel)}
.card .n{font:10px monospace;color:#849291}.card h3{font-size:20px;margin:28px 0 12px}.card p{font-size:14px;line-height:1.6;color:var(--muted)}
.detail{margin-top:26px;display:grid;grid-template-columns:42% 58%;border:1px solid var(--line);min-height:470px}
.detail-copy{padding:40px}.detail-copy h3{font-size:31px;font-weight:400;margin:5px 0 18px}.detail-copy p,.detail-copy li{font-size:14px;line-height:1.65;color:var(--muted)}.detail-copy ul{padding-left:18px}
.detail-visual{position:relative;border-left:1px solid var(--line);min-height:470px;overflow:hidden}
.scene{position:absolute;inset:0;opacity:0;transition:.35s;pointer-events:none}.scene.active{opacity:1;pointer-events:auto}.scene svg{width:100%;height:100%}
.flow{animation:flow 2s linear infinite}.product{animation:product 6s linear infinite}.arm{transform-origin:405px 155px;animation:arm 5s ease-in-out infinite}.press{animation:press 4s ease-in-out infinite}.blade{animation:blade 5s ease-in-out infinite}.load{animation:load 5s ease-in-out infinite}
@keyframes flow{to{stroke-dashoffset:-30}} @keyframes product{from{transform:translateX(-180px)}to{transform:translateX(520px)}} @keyframes arm{0%,20%,100%{transform:rotate(-16deg)}50%,70%{transform:rotate(17deg)}} @keyframes press{0%,30%,100%{transform:translateY(-35px)}55%,75%{transform:translateY(35px)}} @keyframes blade{from{transform:rotate(-5deg)}to{transform:rotate(12deg)}} @keyframes load{from{transform:translateY(0)}to{transform:translateY(-45px)}}
.process{display:grid;grid-template-columns:repeat(5,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}.step{padding:28px 22px;border-right:1px solid var(--line)}.step:last-child{border-right:0}.step b{display:block;font-size:16px;margin:9px 0}.step span{font-size:12px;line-height:1.5;color:var(--muted)}
.about{display:grid;grid-template-columns:1fr 1fr;gap:60px}.about p{color:var(--muted);line-height:1.7}.facts{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--line)}.fact{padding:25px;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}.fact:nth-child(even){border-right:0}.fact b{font-size:25px;font-weight:400;display:block}.fact span{font:10px monospace;color:var(--muted)}
.contact{display:grid;grid-template-columns:1.1fr .9fr;gap:50px}.contactbox{border:1px solid var(--line);padding:30px}.contactbox a{color:var(--blue);text-decoration:none}.footer{padding:35px 0 55px;border-top:1px solid var(--line);display:flex;justify-content:space-between;font:10px monospace;color:var(--muted)}
#cad3d{position:absolute;inset:45px 10px 8px;cursor:grab;perspective:900px;touch-action:none}.cad-grid{position:absolute;left:8%;right:8%;bottom:7%;height:43%;transform:rotateX(66deg);transform-origin:bottom;background-image:linear-gradient(#cdd8d4 1px,transparent 1px),linear-gradient(90deg,#cdd8d4 1px,transparent 1px);background-size:34px 34px;opacity:.7}.cad-object{position:absolute;left:53%;top:48%;width:270px;height:90px;transform-style:preserve-3d}.face{position:absolute;border:2px solid #285863;background:rgba(120,174,184,.58);display:flex;align-items:center;justify-content:center;color:#244b53;font-weight:700;letter-spacing:.13em}.front,.back{width:270px;height:90px}.front{transform:translateZ(55px);font-size:26px}.back{transform:rotateY(180deg) translateZ(55px)}.right,.left{width:110px;height:90px;left:80px;font-size:11px}.right{transform:rotateY(90deg) translateZ(135px)}.left{transform:rotateY(-90deg) translateZ(135px)}.top,.bottom{width:270px;height:110px;top:-10px}.top{transform:rotateX(90deg) translateZ(45px)}.bottom{transform:rotateX(-90deg) translateZ(45px)}
@media(max-width:900px){nav{display:none}.hero,.detail,.about,.contact{grid-template-columns:1fr}.visual,.detail-visual{border-left:0;border-top:1px solid var(--line)}.cards{grid-template-columns:1fr 1fr}.card:nth-child(2){border-right:0}.process{grid-template-columns:1fr}.step{border-right:0;border-bottom:1px solid var(--line)}}

.model3d{position:absolute;inset:0;overflow:hidden;perspective:1050px;cursor:grab;touch-action:none;user-select:none}
.model3d:active{cursor:grabbing}
.model-note{position:absolute;left:26px;top:22px;z-index:6;font:10px monospace;letter-spacing:.09em;color:#6f8081}
.model-stage{position:absolute;left:50%;top:51%;width:1px;height:1px;transform-style:preserve-3d}
.model-grid{position:absolute;left:8%;right:8%;bottom:4%;height:44%;transform:rotateX(67deg);transform-origin:bottom;
background-image:linear-gradient(#ccd7d3 1px,transparent 1px),linear-gradient(90deg,#ccd7d3 1px,transparent 1px);
background-size:32px 32px;opacity:.55}
.box3d{position:absolute;transform-style:preserve-3d}
.box3d .f{position:absolute;border:1px solid rgba(40,88,99,.78);background:rgba(116,171,181,.28);backface-visibility:visible}
.box3d.accent .f{border-color:rgba(183,111,63,.8);background:rgba(210,138,87,.22)}
.box3d.green .f{border-color:rgba(90,125,97,.78);background:rgba(121,155,128,.22)}
.cyl3d{position:absolute;border:1.5px solid #347e8c;border-radius:50%;background:rgba(116,171,181,.18);transform-style:preserve-3d}
.model-caption{position:absolute;right:24px;bottom:18px;font:10px monospace;letter-spacing:.08em;color:#6b7c7e}

.visual,.detail,.contactbox,.facts,.card{background:rgba(255,255,255,.92)}
.visual,.detail-visual{background:
radial-gradient(circle at 72% 28%,rgba(112,181,194,.08),transparent 34%),
linear-gradient(145deg,#ffffff 0%,#fbfdfd 100%)}
.model-grid{opacity:.28!important}
.box3d .f{background:#dce8ea!important;border-color:#6e939a!important;box-shadow:inset 0 0 18px rgba(255,255,255,.62)}
.box3d.accent .f{background:#e8c5aa!important;border-color:#b87950!important}
.box3d.green .f{background:#cbdccf!important;border-color:#78957d!important}
.tank3d{position:absolute;width:150px;height:215px;transform-style:preserve-3d}
.tank-body{position:absolute;left:0;top:25px;width:150px;height:160px;border:1.5px solid #6f8e94;
background:linear-gradient(90deg,#aebfc3 0%,#fdfefe 18%,#d8e3e5 42%,#f8fbfb 60%,#a9bec2 100%);
border-radius:74px/20px;box-shadow:inset -20px 0 24px rgba(58,86,92,.14)}
.tank-cap{position:absolute;left:0;top:12px;width:150px;height:40px;border:1.5px solid #6f8e94;
background:linear-gradient(180deg,#ffffff,#c7d6d9);border-radius:50%}
.tank-cone{position:absolute;left:20px;top:168px;width:110px;height:55px;
background:linear-gradient(90deg,#b5c7ca,#f8fbfb 45%,#aebfc3);
clip-path:polygon(0 0,100% 0,62% 100%,38% 100%);border-top:1.5px solid #6f8e94}
.pipe3d{position:absolute;height:16px;background:linear-gradient(#ffffff,#b7c9cc 48%,#eef4f5);
border:1px solid #718f95;border-radius:9px;transform-origin:left center}
.pipeV{position:absolute;width:16px;background:linear-gradient(90deg,#ffffff,#b7c9cc 48%,#eef4f5);
border:1px solid #718f95;border-radius:9px}
.valve3d{position:absolute;width:28px;height:28px;border-radius:50%;background:#d9e5e7;border:2px solid #718f95}

@media(max-width:900px){.shell{padding:0 24px}}

body{background:#fff!important}
header,.topbar,.nav,.site-header{background:rgba(255,255,255,.96)!important}
section{background:#fff}
.visual,.detail-visual{border-color:#e5eded!important;box-shadow:0 18px 55px rgba(35,72,79,.045)}
.box3d .f{opacity:1!important}


/* v13 — definitive collaboration geometry */
#samarbejde{
  padding-left:0!important;
  padding-right:0!important;
}
#samarbejde .section-title,
#samarbejde .process{
  width:calc(100% - 160px)!important;
  max-width:1180px!important;
  margin-left:auto!important;
  margin-right:auto!important;
}
#samarbejde .process{
  grid-template-columns:repeat(5,minmax(0,1fr))!important;
}
#samarbejde .step{
  min-width:0!important;
  overflow-wrap:anywhere;
}
@media(max-width:1100px){
  #samarbejde .section-title,
  #samarbejde .process{width:calc(100% - 80px)!important}
}
@media(max-width:900px){
  #samarbejde .section-title,
  #samarbejde .process{width:100%!important;max-width:none!important}
  #samarbejde .process{grid-template-columns:1fr!important}
}

/* v14 — same proven safe width for Baggrund/erfaring and Kontakt */
#om .about,
#kontakt .contact{
  width:calc(100% - 160px)!important;
  max-width:1180px!important;
  margin-left:auto!important;
  margin-right:auto!important;
}
#om .about > *,
#kontakt .contact > *{min-width:0!important}

@media(max-width:1100px){
  #om .about,
  #kontakt .contact{width:calc(100% - 80px)!important}
}
@media(max-width:900px){
  #om .about,
  #kontakt .contact{
    width:100%!important;
    max-width:none!important;
  }
}

footer{padding-left:clamp(38px,6vw,95px)!important;padding-right:clamp(38px,6vw,95px)!important}

/* v16 — engineering-model material/detail pass */
.box3d.steel .f{
  background:linear-gradient(135deg,#f9fcfc 0%,#c8d6d9 32%,#eef4f5 58%,#aebfc3 100%)!important;
  border-color:#789097!important;
}
.box3d.darksteel .f{
  background:linear-gradient(135deg,#59676b 0%,#26383d 48%,#718084 100%)!important;
  border-color:#263d43!important;
}
.box3d.solar .f{background:#132c43!important;border-color:#7794a6!important;box-shadow:inset 0 0 0 2px #213e54!important}
.box3d.solar .front,.box3d.solar .back{
  background-color:#122a41!important;
  background-image:
    linear-gradient(rgba(225,239,247,.62) 1px,transparent 1px),
    linear-gradient(90deg,rgba(225,239,247,.62) 1px,transparent 1px)!important;
  background-size:18px 16px!important;
}
.box3d.yellow .f{background:#d5b879!important;border-color:#8e7442!important}
.box3d.black .f{background:#273338!important;border-color:#172125!important}
.cyl3d.roller{background:radial-gradient(circle at 38% 32%,#f8fbfb 0%,#aab8bb 38%,#435156 72%,#1f2a2e 100%)!important;border:2px solid #34464b!important}
.cyl3d.bearing{background:radial-gradient(circle,#dce4e5 0 20%,#4b5a5e 22% 47%,#c7d1d3 49% 65%,#3a494e 67%)!important;border-color:#3b4d52!important}
.cyl3d.pipeend{background:radial-gradient(circle,#f9fbfb 0 28%,#9fb2b6 31% 42%,#e6edef 45% 68%,#748c92 72%)!important}
.detail-visual .model-stage{filter:drop-shadow(0 20px 18px rgba(37,64,70,.12))}

/* v17 — true WebGL 3D */
.model3d{perspective:none!important}
.model3d .model-stage{display:none!important}
.model3d canvas.webgl3d{
  position:absolute;inset:34px 0 20px 0;width:100%!important;height:calc(100% - 54px)!important;
  display:block;touch-action:none;cursor:grab;z-index:2;
}
.model3d canvas.webgl3d:active{cursor:grabbing}
.model3d .model-grid{opacity:.22!important}
.model3d .model-note,.model3d .model-caption{z-index:4}

.hero-config{margin-top:18px;padding:14px 16px 13px;border:1px solid rgba(38,76,83,.16);background:rgba(255,255,255,.62);backdrop-filter:blur(8px)}
.hero-config .cfg-title{font-size:10px;letter-spacing:.14em;font-weight:800;color:#587177;margin-bottom:10px}
.cfg-row{display:grid;grid-template-columns:132px 1fr 66px;gap:12px;align-items:center;margin:8px 0}.cfg-row label{font-size:11px;color:#38545a;font-weight:700}.cfg-row output{font-size:11px;text-align:right;color:#347e8c}.cfg-row input{width:100%;accent-color:#347e8c}
.cfg-actions{display:flex;gap:8px;align-items:center;margin-top:11px;flex-wrap:wrap}.cfg-btn{border:1px solid #347e8c;background:#347e8c;color:#fff;padding:8px 13px;font:800 10px Arial;letter-spacing:.10em;cursor:pointer}.cfg-btn.secondary{background:transparent;color:#347e8c}.cfg-status{font-size:10px;color:#71868b;margin-left:auto}
.view-modes{display:flex;align-items:center;gap:7px;flex-wrap:wrap;margin-top:12px}.view-modes>span{font:800 9px Arial;letter-spacing:.14em;color:#71868b}.view-modes button[data-view]{border:1px solid rgba(52,126,140,.45);background:transparent;color:#347e8c;padding:7px 10px;font:800 9px Arial;cursor:pointer}.view-modes button[data-view].active{background:#347e8c;color:#fff}</style></head><body>
<div class="shell">
<header><div class="brand">SIMGROVA <small>MEKANISK UDVIKLING</small></div>
<nav><button onclick="go('ydelser')">YDELSER</button><button onclick="go('brancher')">BRANCHER</button><button onclick="go('samarbejde')">SAMARBEJDE</button><button onclick="go('om')">OM SIMGROVA</button><button onclick="go('kontakt')">KONTAKT</button></nav></header>

<section class="hero">
<div>
<div class="kicker">MEKANISK UDVIKLING · KONSTRUKTION · PROJEKTLEDELSE</div>
<h1>Mekanisk udvikling<br>og konstruktion.</h1>
<div class="lead">Mekanisk udvikling, konstruktion og teknisk projektarbejde. Opgaver kan løses direkte for en virksomhed eller som ekstern ressource i et eksisterende engineeringteam.</div>
<div class="actions"><button class="btn" onclick="go('kontakt')">KONTAKT</button><button class="btn alt" onclick="go('brancher')">SE OMRÅDER</button></div><div class="hero-config"><div class="cfg-title">KONCEPTKONFIGURATOR · LIVE 3D</div>
<div class="cfg-row"><label>Slædeposition</label><input id="travelSlider" type="range" min="-100" max="100" value="20"><output id="travelOut">20%</output></div>
<div class="cfg-row"><label>Modelstørrelse</label><input id="sizeSlider" type="range" min="1" max="5" value="3" step="1"><output id="sizeOut">M</output></div>
<div class="cfg-row"><label>Arbejdshøjde</label><input id="heightSlider" type="range" min="700" max="1900" value="1300" step="50"><output id="heightOut">1300 mm</output></div>
<div class="cfg-row"><label>Robot-rækkevidde</label><input id="reachSlider" type="range" min="500" max="1500" value="1000" step="50"><output id="reachOut">1000 mm</output></div>
<div class="view-modes"><span>VIEW</span><button type="button" data-view="top">TOP</button><button type="button" data-view="front">FRONT</button><button type="button" data-view="side">SIDE</button><button type="button" data-view="iso" class="active">3D</button><button class="cfg-btn secondary" id="resetCfg" type="button">RESET</button></div></div>
</div>
<div class="visual">
<div class="model3d" id="hero3d">
 <div class="model-note">MEKANISK SYSTEM · ROTATION / LINEÆRAKSE / HÅNDTERING</div>
 <div class="model-grid"></div>
 <div class="model-stage"></div>
 <div class="model-caption">MEKANISK UDVIKLING / KONSTRUKTION</div>
</div></div></section>

<section class="section" id="ydelser"><div class="section-title"><div class="kicker">YDELSER</div><h2>Mekanisk udvikling og konstruktion.</h2><p>Arbejdet kan omfatte mekanisk udvikling, konstruktion, dimensionering og teknisk projektledelse — enten som en afgrænset opgave eller som ekstra kapacitet i et eksisterende projekt.</p></div>
<div class="process">
<div class="step"><span>01</span><b>Konceptudvikling</b><span>Funktionsprincipper, løsningsforslag, layout og valg mellem alternativer.</span></div>
<div class="step"><span>02</span><b>Konstruktion</b><span>3D CAD, maskinelementer, produktionsmodning, tegninger og styklister.</span></div>
<div class="step"><span>03</span><b>Dimensionering</b><span>Belastninger, mekaniske beregninger, FEM/FEA som udviklingsværktøj og optimering.</span></div>
<div class="step"><span>04</span><b>Projektledelse</b><span>Teknisk koordinering fra krav og design til leverandører, montage, test og idriftsættelse.</span></div>
<div class="step"><span>05</span><b>Sikkerhed & CE</b><span>Risikovurdering, dokumentation og konstruktion med maskinsikkerhed tænkt ind fra starten.</span></div>
</div></section>

<section class="section" id="brancher"><div class="section-title"><div class="kicker">ERFARING & ANVENDELSESOMRÅDER</div><h2>Erfarings- og arbejdsområder.</h2><p>Nedenfor er nogle af de områder, hvor erfaringen især ligger. Illustrationerne viser enkle mekaniske principper knyttet til de enkelte områder.</p></div>
<div class="cards">
<div class="card active" onclick="show('energy',this)"><div class="n">01</div><h3>Energi</h3><p>Specialværktøj, løfte- og håndteringsudstyr, mekaniske systemer og udviklingsopgaver til energisektoren.</p></div>
<div class="card" onclick="show('food',this)"><div class="n">02</div><h3>Fødevarer</h3><p>Hygiejnisk og rengøringsvenlig konstruktion, transport, håndtering, fyldning og pakkeløsninger.</p></div>
<div class="card" onclick="show('industry',this)"><div class="n">03</div><h3>Industri</h3><p>Specialmaskiner, produktionsudstyr, automatiserede bevægelser og optimering af eksisterende udstyr.</p></div>
<div class="card" onclick="show('cad',this)"><div class="n">04</div><h3>Udvikling + CAD</h3><p>Fra krav og koncept til NX-konstruktion, interfaces, dokumentation og fremtidige AI-understøttede arbejdsgange.</p></div>
</div>

<div class="detail"><div class="detail-copy">
<div class="kicker" id="dkicker">ENERGI / MEKANISK UDVIKLING</div><h3 id="dtitle">Mekaniske løsninger til energiområdet</h3><div id="dtext"></div>
</div><div class="detail-visual">
<div class="scene active" id="energy">
<div class="model3d" id="energy3d"><div class="model-note">ENERGI · DEPLOYERBART SOLSYSTEM</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">PRINCIPMODEL</div></div>
</div>
<div class="scene" id="food">
<div class="model3d" id="food3d"><div class="model-note">FØDEVARER · TANK / PROCESRØR</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">HYGIENISK PRINCIPMODEL</div></div>
</div>
<div class="scene" id="industry">
<div class="model3d" id="industry3d"><div class="model-note">INDUSTRI · RULLEFORMNING / SPECIALMASKINE</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">PRINCIPMODEL</div></div>
</div>
<div class="scene" id="cad">
<div class="model3d" id="cad3d"><div class="model-note">UDVIKLING + CAD · DEPLOYERBAR SPECIALMASKINE</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">CAD / ENGINEERING</div></div>
</div></div>
</div></div></section>

<section class="section" id="samarbejde"><div class="section-title"><div class="kicker">SAMARBEJDE</div><h2>Indgår dér, hvor der er behov.</h2><p>Opgaverne kan løses direkte for en virksomhed eller som en del af et engineering- eller projektteam. Rollen og omfanget tilpasses den konkrete opgave.</p></div>
<div class="process"><div class="step"><span>01</span><b>Engineering support</b><span>Ekstra kapacitet til mekanisk udvikling og konstruktion i et eksisterende projektteam.</span></div><div class="step"><span>02</span><b>Afgrænset opgave</b><span>En konkret konstruktions-, udviklings- eller beregningsopgave med et tydeligt teknisk scope.</span></div><div class="step"><span>03</span><b>Projektansvar</b><span>Teknisk koordinering af en mekanisk delopgave med grænseflader til kunde, leverandører og øvrige fag.</span></div><div class="step"><span>04</span><b>On-site / remote</b><span>Arbejdet kan indgå tæt i kundens organisation eller udføres mere selvstændigt efter opgavens karakter.</span></div><div class="step"><span>05</span><b>Engineering house</b><span>Kan indgå som ekstern ressource hos engineeringhuse, der har behov for mekanisk kompetence eller ekstra kapacitet.</span></div></div></section>

<section class="section" id="om"><div class="about"><div><div class="kicker">OM SIMGROVA</div><h2>Baggrund og erfaring.</h2><p>Arbejdsområdet er mekanisk udvikling, konstruktion og teknisk projektledelse med fokus på praktiske, gennemarbejdede løsninger.</p><p>Erfaringsområdet spænder fra koncept- og produktudvikling til specialmaskiner, værktøjer, dimensionering, optimering, idriftsættelse, risikovurdering og CE. Arbejdet udføres bl.a. i Siemens NX og Teamcenter.</p><p>Tilgangen er at søge enkle og gennemarbejdede løsninger og holde unødig kompleksitet ude af konstruktionen.</p></div>
<div class="facts"><div class="fact"><b>NX</b><span>3D CAD / KONSTRUKTION</span></div><div class="fact"><b>Teamcenter</b><span>PLM / PROJEKTMILJØ</span></div><div class="fact"><b>Engineering</b><span>UDVIKLING / DIMENSIONERING</span></div><div class="fact"><b>Projekt</b><span>TEKNISK KOORDINERING</span></div></div></div></section>

<section class="section" id="kontakt"><div class="contact"><div><div class="kicker">KONTAKT</div><h2>Kontakt.</h2><p class="lead">Kontakt kan være relevant ved behov for en ekstern maskiningeniør til en konkret opgave, et projektforløb eller som midlertidig engineeringkapacitet.</p><div class="actions"><button class="btn" onclick="location.href='mailto:snc@simgrova.dk?subject=Forespørgsel til SIMGROVA'">E-MAIL</button><button class="btn alt" onclick="location.href='tel:+4521467659'">TELEFON +45 21 46 76 59</button></div></div>
<div class="contactbox"><div style="font-size:24px;font-weight:700;letter-spacing:.08em;color:#20353a;margin-bottom:22px">SIMGROVA <span style="font-size:13px;font-weight:400;color:#788789">ApS</span></div><p><b>Søren Noe Christiansen</b><br>Maskiningeniør</p><p><a href="mailto:snc@simgrova.dk">snc@simgrova.dk</a><br><a href="tel:+4521467659">+45 21 46 76 59</a></p><p style="color:var(--muted);font-size:13px;line-height:1.6">Mekanisk udvikling · Konstruktion · Teknisk projektledelse · Dimensionering · Specialmaskiner · Risikovurdering & CE</p></div></div></section>

<div class="footer"><span>SIMGROVA · SIMPLICITY CREATES GROWTH</span><span>MECHANICAL ENGINEERING / DENMARK</span></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
function go(id){document.getElementById(id).scrollIntoView({behavior:'smooth'})}
const content={
energy:{k:"ENERGI / MEKANISK UDVIKLING",t:"Mekaniske løsninger til energiområdet",html:`<p>På energiområdet har arbejdet blandt andet omfattet mekaniske udviklingsopgaver, specialværktøj og udstyr, hvor belastning, håndtering og sikkerhed er væsentlige designforhold.</p><ul><li>Specialværktøj og hjælpeudstyr</li><li>Løfte- og håndteringskoncepter</li><li>Dimensionering og strukturel optimering</li><li>Hydrauliske og mekaniske funktioner</li><li>Produktionsgrundlag, test og dokumentation</li></ul><p>Relevant erfaring omfatter bl.a. udviklingsopgaver og hydraulisk specialværktøj til vind-/energisektoren.</p>`},
food:{k:"FØDEVARER / HYGIENISK KONSTRUKTION",t:"Fødevareudstyr og hygiejnisk konstruktion",html:`<p>Ved fødevareudstyr indgår materialer, geometri, dræning, rengøring og service som naturlige designhensyn. Erfaringen omfatter konstruktion, hvor disse forhold tænkes ind fra starten.</p><ul><li>Hygiejnisk design: drænbar geometri, egnede samlinger og færre døde zoner</li><li>Rengøringsvenlige løsninger og CIP-principper</li><li>Servicevenlig konstruktion med fokus på kontaminationsrisiko</li><li>Køleteknisk udstyr, transportører, pakkemaskiner, Pick & Place, frysere, volumetriske fyldere og mekaniske pakninger</li></ul><p><b>Designgrundlag:</b> EHEDG · 3-A · CIP (Clean In Place).</p>`},
industry:{k:"INDUSTRI / SPECIALMASKINER",t:"Specialmaskiner og produktionsudstyr",html:`<p>Arbejdet kan omfatte nye specialmaskiner, delsystemer eller ændringer af eksisterende produktionsudstyr med fokus på funktion, fremstilling, montage og service.</p><ul><li>Specialmaskiner og produktionsudstyr</li><li>Automatiserede mekaniske bevægelser og emnehåndtering</li><li>Optimering af eksisterende udstyr og cyklustid</li><li>Design for manufacturing og service</li><li>Layout, konstruktion, leverandørdialog, montage og idriftsættelse</li></ul><p>Erfaringen omfatter bl.a. højhastighedsudstyr med krav til stabil produktion og høj OEE.</p>`},
cad:{k:"UDVIKLING / CAD + ENGINEERING",t:"Udvikling og konstruktion i 3D",html:`<p>3D CAD bruges gennem udviklingsforløbet til at undersøge funktion, pladsforhold, interfaces, montage og forskellige løsningsmuligheder.</p><ul><li>Siemens NX og Teamcenter</li><li>Konceptmodeller og maskinlayout</li><li>Detaljekonstruktion og produktionsmodning</li><li>Dimensionering og FEM/FEA som udviklingsværktøj</li><li>Teknisk dokumentation og design reviews</li></ul><p>AI kan fremover bruges som ekstra værktøj til hurtigere konceptarbejde og systematisering — mens de mekaniske beslutninger fortsat bygger på ingeniørfaglig vurdering.</p>`}
};


function show(id,el){
  document.querySelectorAll(".card").forEach(c=>c.classList.remove("active"));
  if(el) el.classList.add("active");

  document.querySelectorAll(".scene").forEach(s=>s.classList.remove("active"));
  const scene=document.getElementById(id);
  if(scene) scene.classList.add("active");

  const c=content[id];
  if(c){
    document.getElementById("dkicker").textContent=c.k;
    document.getElementById("dtitle").textContent=c.t;
    document.getElementById("dtext").innerHTML=c.html;
  }

  const map={energy:"energy3d",food:"food3d",industry:"industry3d",cad:"cad3d"};
  setupModel(map[id],id);
}

const built={};

function box(stage,x,y,z,w,h,d,kind=""){
 const b=document.createElement("div");
 b.className="box3d "+kind;
 b.style.width=w+"px";
 b.style.height=h+"px";
 b.style.transform=`translate3d(${x}px,${y}px,${z}px)`;

 function face(cls,fw,fh,transform,left=null,top=null){
   const f=document.createElement("div");
   f.className="f "+cls;
   f.style.width=fw+"px";
   f.style.height=fh+"px";
   if(left!==null) f.style.left=left+"px";
   if(top!==null) f.style.top=top+"px";
   f.style.transform=transform;
   b.appendChild(f);
 }
 face("front",w,h,`translateZ(${d/2}px)`);
 face("back",w,h,`rotateY(180deg) translateZ(${d/2}px)`);
 face("right",d,h,`rotateY(90deg) translateZ(${w/2}px)`,(w-d)/2);
 face("left",d,h,`rotateY(-90deg) translateZ(${w/2}px)`,(w-d)/2);
 face("top",w,d,`rotateX(90deg) translateZ(${h/2}px)`,null,(h-d)/2);
 face("bottom",w,d,`rotateX(-90deg) translateZ(${h/2}px)`,null,(h-d)/2);

 stage.appendChild(b);
 return b;
}

function cyl(stage,x,y,z,r,kind=""){
 const c=document.createElement("div");
 c.className="cyl3d "+kind;
 c.style.width=(r*2)+"px";
 c.style.height=(r*2)+"px";
 c.style.transform=`translate3d(${x}px,${y}px,${z}px) rotateX(90deg)`;
 stage.appendChild(c);
 return c;
}


function panel(stage,x,y,z,w,h,d=7,kind=""){
  return box(stage,x,y,z,w,h,d,kind);
}

function faceLabel(obj,html,size=12){
  const f=obj && obj.querySelector(".front");
  if(f){
    f.innerHTML=html;
    f.style.display="flex";
    f.style.alignItems="center";
    f.style.justifyContent="center";
    f.style.font=`700 ${size}px Arial`;
    f.style.letterSpacing=".12em";
    f.style.color="#28474e";
  }
}


const webglModels={};
const heroMechanism={};

function setupModel(id,type){
  if(webglModels[id] || typeof THREE==="undefined") return;
  const host=document.getElementById(id);
  if(!host) return;

  const canvas=document.createElement("canvas");
  canvas.className="webgl3d";
  host.appendChild(canvas);

  const scene=new THREE.Scene();
  const camera=new THREE.PerspectiveCamera(34,1,.1,3000);
  camera.position.set(7,5.3,9.5);

  const renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,2));
  renderer.setClearColor(0xffffff,0);
  renderer.outputColorSpace=THREE.SRGBColorSpace;
  renderer.toneMapping=THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure=1.08;
  renderer.shadowMap.enabled=true;
  renderer.shadowMap.type=THREE.PCFSoftShadowMap;

  scene.add(new THREE.HemisphereLight(0xf8ffff,0x7c8f91,2.25));
  const key=new THREE.DirectionalLight(0xffffff,3.1);
  key.position.set(6,9,7); key.castShadow=true;
  key.shadow.mapSize.set(1024,1024); scene.add(key);
  const rim=new THREE.DirectionalLight(0x9edce5,1.45);
  rim.position.set(-7,4,-6); scene.add(rim);

  const root=new THREE.Group();
  scene.add(root);

  const MAT={
    steel:new THREE.MeshStandardMaterial({color:0xcbd6d7,metalness:.82,roughness:.25}),
    polished:new THREE.MeshStandardMaterial({color:0xe6eeee,metalness:.94,roughness:.16}),
    dark:new THREE.MeshStandardMaterial({color:0x33464b,metalness:.72,roughness:.30}),
    blue:new THREE.MeshStandardMaterial({color:0x347e8c,metalness:.48,roughness:.28}),
    green:new THREE.MeshStandardMaterial({color:0x8eaa78,metalness:.25,roughness:.38}),
    brass:new THREE.MeshStandardMaterial({color:0xb49b62,metalness:.78,roughness:.27}),
    black:new THREE.MeshStandardMaterial({color:0x17252a,metalness:.55,roughness:.25}),
    solar:new THREE.MeshStandardMaterial({color:0x102b43,metalness:.38,roughness:.22}),
    glass:new THREE.MeshPhysicalMaterial({color:0x9ed5df,metalness:.05,roughness:.12,transparent:true,opacity:.42,transmission:.35})
  };

  function mesh(geo,mat=MAT.steel,parent=root){
    const m=new THREE.Mesh(geo,mat); m.castShadow=true; m.receiveShadow=true; parent.add(m); return m;
  }
  function box(x,y,z,sx,sy,sz,mat=MAT.steel,parent=root){
    const m=mesh(new THREE.BoxGeometry(sx,sy,sz),mat,parent); m.position.set(x,y,z); return m;
  }
  function cyl(x,y,z,r,len,axis="x",mat=MAT.polished,parent=root,segments=32){
    const m=mesh(new THREE.CylinderGeometry(r,r,len,segments),mat,parent);
    m.position.set(x,y,z);
    if(axis==="x") m.rotation.z=Math.PI/2;
    if(axis==="z") m.rotation.x=Math.PI/2;
    return m;
  }
  function torus(x,y,z,R,r,axis="x",mat=MAT.dark,parent=root){
    const m=mesh(new THREE.TorusGeometry(R,r,12,36),mat,parent); m.position.set(x,y,z);
    if(axis==="x") m.rotation.y=Math.PI/2;
    if(axis==="y") m.rotation.x=Math.PI/2;
    return m;
  }
  function beam(a,b,r=.045,mat=MAT.steel,parent=root){
    const A=new THREE.Vector3(...a), B=new THREE.Vector3(...b), d=B.clone().sub(A);
    const m=mesh(new THREE.CylinderGeometry(r,r,d.length(),14),mat,parent);
    m.position.copy(A.clone().add(B).multiplyScalar(.5));
    m.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),d.clone().normalize());
    return m;
  }
  function bolt(x,y,z,axis="x",parent=root){
    cyl(x,y,z,.075,.13,axis,MAT.dark,parent,16);
    const head=cyl(x+(axis==="x"?.08:0),y+(axis==="y"?.08:0),z+(axis==="z"?.08:0),.115,.055,axis,MAT.steel,parent,6);
    return head;
  }
  function gear(x,y,z,R,width,axis="x",mat=MAT.steel,parent=root,teeth=18){
    const g=new THREE.Group(); parent.add(g); g.position.set(x,y,z);
    cyl(0,0,0,R*.72,width,axis,mat,g,32);
    for(let i=0;i<teeth;i++){
      const a=i*Math.PI*2/teeth;
      const t=box(0,0,0,R*.24,width*.92,R*.13,mat,g);
      if(axis==="x"){ t.position.set(0,Math.cos(a)*R*.84,Math.sin(a)*R*.84); t.rotation.x=-a; }
      else { t.position.set(Math.cos(a)*R*.84,Math.sin(a)*R*.84,0); t.rotation.z=a; }
    }
    return g;
  }
  function panel(x,y,z,w,h,rotY=0,parent=root){
    const g=new THREE.Group(); parent.add(g); g.position.set(x,y,z); g.rotation.y=rotY;
    box(0,0,0,w+.10,h+.10,.075,MAT.steel,g);
    box(0,0,.045,w,h,.045,MAT.solar,g);
    for(let i=1;i<6;i++) box(-w/2+i*w/6,0,.073,.012,h,.012,MAT.polished,g);
    for(let j=1;j<4;j++) box(0,-h/2+j*h/4,.074,w,.012,.012,MAT.polished,g);
    return g;
  }
  function pipe(points,r=.055,mat=MAT.polished,parent=root){
    const curve=new THREE.CatmullRomCurve3(points.map(p=>new THREE.Vector3(...p)));
    return mesh(new THREE.TubeGeometry(curve,48,r,14,false),mat,parent);
  }
  function frameRect(x,y,z,w,h,t=.08,mat=MAT.dark,parent=root){
    box(x-w/2,y,z,t,h,t,mat,parent); box(x+w/2,y,z,t,h,t,mat,parent);
    box(x,y-h/2,z,w,t,t,mat,parent); box(x,y+h/2,z,w,t,t,mat,parent);
  }

  // HERO — mechanically connected kinematic chain.
  if(type==="hero"){
    const H=new THREE.Group(); root.add(H);
    heroMechanism.machine=H;

    box(0,-1.05,0,5.4,.28,3.25,MAT.dark,H);
    box(0,-.84,0,5.0,.14,2.85,MAT.steel,H);
    for(const x of [-2.25,2.25]) for(const z of [-1.15,1.15]) bolt(x,-.64,z,"y",H);

    // Fixed rotary workstation.
    cyl(-1.55,-.28,0,.92,.72,"y",MAT.blue,H);
    cyl(-1.55,.12,0,.58,.88,"y",MAT.polished,H);
    gear(-1.55,.62,0,.62,.22,"y",MAT.steel,H);
    gear(-.55,.62,0,.34,.22,"y",MAT.brass,H,14);

    // Linear axis.
    heroMechanism.rail1=box(.85,-.38,-.82,3.0,.22,.18,MAT.polished,H);
    heroMechanism.rail2=box(.85,-.38,.82,3.0,.22,.18,MAT.polished,H);
    heroMechanism.screw=cyl(.85,-.12,0,.07,2.8,"x",MAT.brass,H);

    // Entire robot travels as one assembly.
    const moving=new THREE.Group(); H.add(moving);
    heroMechanism.moving=moving; moving.position.set(1.15,0,0);
    box(0,.02,0,1.0,.32,2.0,MAT.steel,moving);
    cyl(0,.42,0,.38,.34,"y",MAT.dark,moving);

    // Cylinder 1 starts at carriage.
    const lift=new THREE.Group(); moving.add(lift);
    lift.position.set(0,.48,0);
    heroMechanism.cyl1=cyl(0,.875,0,.23,1.75,"y",MAT.polished,lift);

    // Joint 1 is parented to the END of cylinder 1.
    const j1=new THREE.Group(); lift.add(j1); j1.position.set(0,1.75,0);
    heroMechanism.joint1Group=j1;
    cyl(0,0,0,.29,.44,"y",MAT.blue,j1);

    // Link/cylinder 2.
    const l2=new THREE.Group(); j1.add(l2); l2.rotation.z=-.48;
    heroMechanism.link2=l2;
    heroMechanism.link2Body=cyl(.48,0,0,.13,.96,"x",MAT.steel,l2);

    // Joint 2 is parented to END of link 2.
    const j2=new THREE.Group(); l2.add(j2); j2.position.set(.96,0,0);
    heroMechanism.joint2Group=j2;
    cyl(0,0,0,.22,.40,"x",MAT.dark,j2);

    // Link/cylinder 3.
    const l3=new THREE.Group(); j2.add(l3); l3.rotation.z=.82;
    heroMechanism.link3=l3;
    heroMechanism.link3Body=cyl(.39,0,0,.11,.78,"x",MAT.steel,l3);

    // Tool is parented to END of link 3.
    const tool=new THREE.Group(); l3.add(tool); tool.position.set(.78,0,0);
    heroMechanism.toolGroup=tool;
    box(0,0,0,.44,.32,.56,MAT.blue,tool);
    box(.25,-.20,-.18,.10,.50,.12,MAT.dark,tool);
    box(.25,-.20,.18,.10,.50,.12,MAT.dark,tool);

    heroMechanism.L1=1.75; heroMechanism.L2=.96; heroMechanism.L3=.78;
    heroMechanism.travel=2.45;
    heroMechanism.applyTravel=v=>{
      const p=Math.max(-100,Math.min(100,+v||0))/100;
      moving.position.x=1.15+p*heroMechanism.travel*.46;
    };
    heroMechanism.liveUpdate=(sizeStep,heightMm,reachMm)=>{
      const sc=[.78,.89,1,1.12,1.25][Math.max(1,Math.min(5,+sizeStep||3))-1];
      const hs=Math.max(700,Math.min(1900,+heightMm||1300))/1300;
      const rs=Math.max(500,Math.min(1500,+reachMm||1000))/1000;
      root.scale.setScalar(sc);

      const L1=heroMechanism.L1*hs;
      heroMechanism.cyl1.scale.y=hs;
      heroMechanism.cyl1.position.y=L1/2;
      heroMechanism.joint1Group.position.y=L1;

      const L2=heroMechanism.L2*rs, L3=heroMechanism.L3*rs;
      heroMechanism.link2Body.scale.y=rs;
      heroMechanism.link2Body.position.x=L2/2;
      heroMechanism.joint2Group.position.x=L2;
      heroMechanism.link3Body.scale.y=rs;
      heroMechanism.link3Body.position.x=L3/2;
      heroMechanism.toolGroup.position.x=L3;

      heroMechanism.applyTravel(document.getElementById("travelSlider")?.value||20);
    };
  }

  // ENERGY — genuinely spatial deployable solar mechanism.
  if(type==="energy"){
    // central container
    box(0,0,0,2.8,1.65,1.55,MAT.steel);
    for(const x of [-1.32,1.32]) for(const z of [-.69,.69]) box(x,0,z,.16,1.78,.16,MAT.dark);
    box(0,.73,0,2.65,.12,1.42,MAT.dark);
    box(0,-.73,0,2.65,.12,1.42,MAT.dark);

    // two telescopic ground rails in true depth
    box(0,-.96,-1.22,10.8,.10,.12,MAT.polished);
    box(0,-.96,1.22,10.8,.10,.12,MAT.polished);

    // panel wings: staggered/folded slightly in Y and Z, each on transverse support
    for(const side of [-1,1]){
      for(let i=0;i<4;i++){
        const x=side*(2.15+i*1.58);
        const y=-.28 + i*.10;
        const z=(i%2===0?.06:-.06);
        const ang=side*(i===0?.12:(i===1?.06:0));
        panel(x,y,z,1.42,2.18,ang);
        box(x,-.72,z,1.25,.10,2.55,MAT.dark);
        cyl(x-side*.76,-.58,z,.11,.30,"z",MAT.brass);
      }
    }
    // center deployment cassette and drive
    box(0,-.34,0,2.25,.48,1.05,MAT.dark);
    cyl(-.88,-.28,.62,.18,.30,"z",MAT.brass);
    cyl(.88,-.28,.62,.18,.30,"z",MAT.brass);
    gear(0,.15,.88,.36,.16,"z",MAT.brass,root,16);
  }

  // FOOD — full-volume hygienic skid.
  if(type==="food"){
    box(0,-1.15,0,5.5,.18,3.2,MAT.steel);
    // frame feet
    for(const x of [-2.35,2.35]) for(const z of [-1.25,1.25]) box(x,-1.48,z,.18,.65,.18,MAT.dark);

    function vessel(x,z,r=0.72,h=2.35){
      cyl(x,.10,z,r,h,"y",MAT.polished);
      const top=mesh(new THREE.SphereGeometry(r,32,16,0,Math.PI*2,0,Math.PI/2),MAT.polished);
      top.scale.y=.35; top.position.set(x,1.28,z); root.add(top);
      const cone=mesh(new THREE.ConeGeometry(r*.92,.55,32),MAT.polished);
      cone.position.set(x,-1.25,z); cone.rotation.x=Math.PI; root.add(cone);
      cyl(x,1.58,z,.18,.28,"y",MAT.dark);
      cyl(x,1.88,z,.26,.34,"y",MAT.green);
      pipe([[x,-1.48,z],[x,-1.72,z],[x+.45,-1.72,z]],.07);
      torus(x,.92,z+r+.02,.18,.035,"x",MAT.dark);
    }
    vessel(-1.35,0,.72,2.35); vessel(.45,.15,.62,2.0);

    // sanitary pipe network with real round tubes and bends
    pipe([[-2.25,-.78,1.08],[-1.35,-.78,1.08],[-1.35,-.20,1.08],[.45,-.20,1.08],[.45,-.72,1.08],[2.05,-.72,1.08]],.075);
    pipe([[-1.35,1.55,-.75],[-1.35,1.55,-1.15],[1.95,1.55,-1.15],[1.95,.55,-1.15]],.065);
    // butterfly valves
    for(const x of [-.45,.65,1.45]){
      cyl(x,-.72,1.08,.16,.13,"x",MAT.blue);
      box(x,.0+(-.45),1.08,.07,.36,.07,MAT.dark);
    }
    // centrifugal pump and motor
    cyl(1.55,-.62,-.48,.42,.34,"z",MAT.polished);
    cyl(2.08,-.62,-.48,.34,.78,"x",MAT.green);
    pipe([[1.55,-.62,-.25],[1.55,-.62,.42],[2.15,-.62,.42]],.085);
    // plate heat exchanger
    for(let i=0;i<10;i++) box(2.10,-.05,-.90+i*.055,.72,1.28,.025,i%2?MAT.steel:MAT.brass);
    box(2.10,-.05,-1.20,.86,1.45,.12,MAT.dark);
    box(2.10,-.05,-.25,.86,1.45,.12,MAT.dark);
  }

  // INDUSTRY — actual shafts and roll tooling through rigid stands.
  if(type==="industry"){
    box(0,-1.25,0,6.4,.30,3.1,MAT.dark);
    box(0,-1.02,0,6.0,.16,2.75,MAT.steel);
    const xs=[-2.45,-1.48,-.50,.48,1.46,2.44];
    xs.forEach((x,i)=>{
      // stand frames on both sides of strip
      frameRect(x,.05,-1.05,.64,2.15,.16,MAT.dark);
      frameRect(x,.05,1.05,.64,2.15,.16,MAT.dark);
      // cross ties
      box(x,1.05,0,.16,.18,2.1,MAT.dark);
      // top/bottom shafts along Z
      cyl(x,.43,0,.105,2.45,"z",MAT.polished);
      cyl(x,-.38,0,.105,2.45,"z",MAT.polished);
      // bearing housings at both ends
      for(const z of [-1.05,1.05]){
        box(x,.43,z,.46,.42,.22,MAT.brass);
        box(x,-.38,z,.46,.42,.22,MAT.brass);
        torus(x,.43,z+(z>0?.13:-.13),.15,.035,"z",MAT.dark);
        torus(x,-.38,z+(z>0?.13:-.13),.15,.035,"z",MAT.dark);
        // adjustment screw
        cyl(x,1.30,z,.07,.48,"y",MAT.polished);
        cyl(x,1.56,z,.13,.10,"y",MAT.dark,root,6);
      }
      // changing roll tooling — several discs per shaft
      const widths=[.18,.22,.26];
      const spread=.24+i*.025;
      for(const yy of [.43,-.38]){
        cyl(x,yy,-spread,.34-i*.012,widths[1],"z",MAT.polished);
        cyl(x,yy,0,.46-i*.018,widths[2],"z",MAT.dark);
        cyl(x,yy,spread,.34-i*.012,widths[1],"z",MAT.polished);
      }
    });
    // strip in pass line
    box(0,.02,0,6.9,.055,.92,MAT.blue);
    // drive side shaft couplings
    for(const x of xs) cyl(x,-.38,-1.42,.15,.48,"z",MAT.dark);
  }

  // CAD — containerised special machine with true open volume and deployed mechanism.
  if(type==="cad"){
    const g=new THREE.Group(); root.add(g);
    // open structural container frame rather than a solid box
    const L=4.8,H=2.25,W=2.25,t=.12;
    for(const x of [-L/2,L/2]) for(const z of [-W/2,W/2]) box(x,0,z,t,H,t,MAT.dark,g);
    for(const y of [-H/2,H/2]){
      box(0,y,-W/2,L,t,t,MAT.dark,g); box(0,y,W/2,L,t,t,MAT.dark,g);
      box(-L/2,y,0,t,t,W,MAT.dark,g); box(L/2,y,0,t,t,W,MAT.dark,g);
    }
    // rear wall ribs
    box(0,0,-W/2+.05,L-.2,H-.2,.08,MAT.steel,g);
    for(let x=-2.0;x<=2.0;x+=.4) box(x,0,-W/2+.11,.035,H-.25,.06,MAT.dark,g);

    // two opened side doors, actually rotated in 3D around vertical hinges
    const dl=new THREE.Group(); g.add(dl); dl.position.set(-L/2,0,W/2);
    const doorL=box(-.82,0,0,1.62,H-.18,.08,MAT.green,dl); dl.rotation.y=-1.15;
    const dr=new THREE.Group(); g.add(dr); dr.position.set(L/2,0,W/2);
    const doorR=box(.82,0,0,1.62,H-.18,.08,MAT.green,dr); dr.rotation.y=1.15;

    // telescopic rails and deployed platform coming out of container
    box(.65,-.88,1.85,3.4,.12,.12,MAT.dark,g);
    box(.65,-.88,2.55,3.4,.12,.12,MAT.dark,g);
    box(1.15,-.72,2.18,2.75,.16,1.25,MAT.steel,g);

    // compact machine on platform: rotary base + column + articulated arm
    cyl(1.05,-.48,2.18,.48,.24,"y",MAT.blue,g);
    cyl(1.05,.08,2.18,.27,.90,"y",MAT.dark,g);
    cyl(1.05,.62,2.18,.24,.30,"z",MAT.brass,g);
    beam([1.05,.62,2.18],[1.72,1.08,2.18],.13,MAT.steel,g);
    cyl(1.72,1.08,2.18,.20,.30,"z",MAT.dark,g);
    beam([1.72,1.08,2.18],[2.22,.72,2.58],.11,MAT.steel,g);
    box(2.22,.72,2.58,.42,.32,.42,MAT.blue,g);
    // deployed stabilisers
    for(const x of [.05,2.25]){
      box(x,-1.12,2.05,.12,.62,.12,MAT.dark,g);
      box(x,-1.43,2.05,.55,.08,.55,MAT.steel,g);
    }
  }

  // floor shadow catcher
  const floor=new THREE.Mesh(new THREE.PlaneGeometry(30,30),
      new THREE.ShadowMaterial({color:0x49666c,opacity:.10}));
  floor.rotation.x=-Math.PI/2; floor.position.y=-1.62; floor.receiveShadow=true; scene.add(floor);

  const presets={
    hero:{dist:10.5,target:[0,.35,0]},
    energy:{dist:12.8,target:[0,-.25,0]},
    food:{dist:9.7,target:[0,.05,0]},
    industry:{dist:10.8,target:[0,.05,0]},
    cad:{dist:10.4,target:[.35,0,.55]}
  };
  const P=presets[type]||presets.hero;
  let yaw=type==="energy"?.18:.48, pitch=type==="industry"?.25:.32, dist=P.dist;
  if(type==="hero") heroMechanism.setView=mode=>{
    // Conventional principal views: no residual oblique tilt.
    if(mode==="top"){yaw=0;pitch=Math.PI/2-.001;dist=P.dist*1.06;}
    else if(mode==="front"){yaw=0;pitch=0;dist=P.dist;}
    else if(mode==="side"){yaw=Math.PI/2;pitch=0;dist=P.dist;}
    else {yaw=.48;pitch=.32;dist=P.dist;}
    auto=false;
  };
  let dragging=false,lastX=0,lastY=0,auto=true;

  function resize(){
    const w=Math.max(10,host.clientWidth), h=Math.max(10,host.clientHeight-54);
    renderer.setSize(w,h,false); camera.aspect=w/h; camera.updateProjectionMatrix();
  }
  function view(){
    const t=new THREE.Vector3(...P.target);
    camera.position.set(
      t.x+dist*Math.sin(yaw)*Math.cos(pitch),
      t.y+dist*Math.sin(pitch),
      t.z+dist*Math.cos(yaw)*Math.cos(pitch)
    );
    camera.lookAt(t);
  }
  canvas.addEventListener("pointerdown",e=>{dragging=true;auto=false;lastX=e.clientX;lastY=e.clientY;canvas.setPointerCapture(e.pointerId)});
  canvas.addEventListener("pointermove",e=>{
    if(!dragging)return;
    yaw-=(e.clientX-lastX)*.008; pitch=Math.max(-.15,Math.min(1.15,pitch+(e.clientY-lastY)*.006));
    lastX=e.clientX;lastY=e.clientY;
  });
  canvas.addEventListener("pointerup",()=>dragging=false);
  canvas.addEventListener("wheel",e=>{e.preventDefault();auto=false;dist=Math.max(5.5,Math.min(18,dist+e.deltaY*.008))},{passive:false});

  const ro=new ResizeObserver(resize); ro.observe(host); resize();
  function animate(){
    requestAnimationFrame(animate);
    if(auto) yaw+=.0010;
    view(); renderer.render(scene,camera);
  }
  animate();
  webglModels[id]={renderer,scene,camera,root};
}

setupModel("hero3d","hero");
setupModel("energy3d","energy");
setupModel("food3d","food");
setupModel("industry3d","industry");
setupModel("cad3d","cad");
document.getElementById("dtext").innerHTML=content.energy.html;


const travelSlider=document.getElementById("travelSlider"),sizeSlider=document.getElementById("sizeSlider"),heightSlider=document.getElementById("heightSlider"),reachSlider=document.getElementById("reachSlider");
function cfgLabels(){document.getElementById("travelOut").textContent=travelSlider.value+"%";document.getElementById("sizeOut").textContent=["XS","S","M","L","XL"][+sizeSlider.value-1];document.getElementById("heightOut").textContent=heightSlider.value+" mm";document.getElementById("reachOut").textContent=reachSlider.value+" mm";}
function liveGeometry(){cfgLabels();heroMechanism.liveUpdate?.(sizeSlider.value,heightSlider.value,reachSlider.value);}
travelSlider.addEventListener("input",()=>{cfgLabels();heroMechanism.applyTravel?.(travelSlider.value);});
[sizeSlider,heightSlider,reachSlider].forEach(s=>s.addEventListener("input",liveGeometry));
document.querySelectorAll(".view-modes button[data-view]").forEach(b=>b.addEventListener("click",()=>{document.querySelectorAll(".view-modes button[data-view]").forEach(x=>x.classList.remove("active"));b.classList.add("active");heroMechanism.setView?.(b.dataset.view);}));
document.getElementById("resetCfg").addEventListener("click",()=>{travelSlider.value=20;sizeSlider.value=3;heightSlider.value=1300;reachSlider.value=1000;cfgLabels();heroMechanism.liveUpdate?.(3,1300,1000);heroMechanism.applyTravel?.(20);heroMechanism.setView?.("iso");document.querySelectorAll(".view-modes button[data-view]").forEach(x=>x.classList.toggle("active",x.dataset.view==="iso"));});
cfgLabels();heroMechanism.liveUpdate?.(3,1300,1000);
</script></body></html>
"""
components.html(page, height=4300, scrolling=True)

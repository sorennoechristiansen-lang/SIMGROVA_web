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
.view-modes{display:flex;align-items:center;gap:7px;flex-wrap:wrap;margin-top:12px}.view-modes>span{font:800 9px Arial;letter-spacing:.14em;color:#71868b}.view-modes button[data-view]{border:1px solid rgba(52,126,140,.45);background:transparent;color:#347e8c;padding:7px 10px;font:800 9px Arial;cursor:pointer}.view-modes button[data-view].active{background:#347e8c;color:#fff}
/* v26 — hero configurator alignment */
.hero>div:first-child{height:560px;display:flex;flex-direction:column;padding-right:clamp(22px,3vw,48px)}
.ai-example{margin-top:auto;margin-bottom:8px;padding-top:18px;font:10px monospace;letter-spacing:.12em;color:#6f8081}
.hero-config{margin-top:0!important}
@media(max-width:900px){
  .hero>div:first-child{height:auto;min-height:0;padding-right:0;padding-bottom:28px}
  .ai-example{margin-top:28px}
}

.concept-static{overflow:hidden;background:#f7faf9}
.concept-static .concept-image{position:absolute;inset:38px 10px 28px;width:calc(100% - 20px);height:calc(100% - 66px);object-fit:contain;display:block}
.concept-static canvas,.concept-static .model-grid,.concept-static .model-stage{display:none!important}

/* v36 — controlled photorealistic business card, without altering contact layout */
#kontakt .premium-card{
  position:relative;
  box-sizing:border-box;
  min-height:300px;
  padding:0!important;
  overflow:hidden;
  border:1px solid #c8cfcc!important;
  border-radius:9px!important;
  background:
    linear-gradient(115deg,rgba(255,255,255,.72),rgba(255,255,255,.08) 32%,rgba(255,255,255,.34) 67%,rgba(255,255,255,.08)),
    linear-gradient(180deg,#f4f5f2 0%,#e8ebe7 100%)!important;
  box-shadow:0 18px 34px rgba(24,42,42,.13),0 3px 8px rgba(24,42,42,.08),inset 0 1px 0 #fff!important;
}
#kontakt .premium-card:before{
  content:"";position:absolute;inset:0;pointer-events:none;opacity:.22;
  background-image:
    repeating-linear-gradient(0deg,rgba(42,59,58,.045) 0,rgba(42,59,58,.045) 1px,transparent 1px,transparent 4px);
}
#kontakt .premium-card .card-edge{
  position:absolute;left:0;right:0;bottom:0;height:5px;
  background:linear-gradient(180deg,#cfd5d1,#aeb8b3);
  box-shadow:inset 0 1px rgba(255,255,255,.8);
}
#kontakt .premium-card .card-content{
  position:relative;z-index:1;
  padding:34px 38px 30px;
}
#kontakt .premium-card .card-brand{
  font-size:25px;font-weight:700;letter-spacing:.10em;color:#20353a;
  text-shadow:0 1px rgba(255,255,255,.85);
}
#kontakt .premium-card .card-brand span{
  font-size:12px;font-weight:500;letter-spacing:.06em;color:#788789;
}
#kontakt .premium-card .card-rule{
  width:42px;height:2px;margin:18px 0 22px;background:#4f7776;
}
#kontakt .premium-card .card-name{
  color:#263b3f;font-size:15px;line-height:1.55;
}
#kontakt .premium-card .card-name span{color:#687a7b;font-size:13px}
#kontakt .premium-card .card-contact{margin-top:18px;line-height:1.7;font-size:14px}
#kontakt .premium-card .card-contact a{color:#244f57;text-decoration:none}
#kontakt .premium-card .card-contact a:hover{text-decoration:underline;text-underline-offset:3px}
#kontakt .premium-card .card-services{
  margin-top:24px;padding-top:15px;border-top:1px solid rgba(66,88,87,.18);
  color:#6f7f80;font-size:11.5px;line-height:1.65;letter-spacing:.01em;
}
@media(max-width:700px){
 #kontakt .premium-card{min-height:0}
 #kontakt .premium-card .card-content{padding:28px 26px}
}
</style></head><body>
<div class="shell">
<header><div class="brand">SIMGROVA <small>MEKANISK UDVIKLING</small></div>
<nav><button onclick="go('ydelser')">YDELSER</button><button onclick="go('brancher')">BRANCHER</button><button onclick="go('samarbejde')">SAMARBEJDE</button><button onclick="go('om')">OM SIMGROVA</button><button onclick="go('kontakt')">KONTAKT</button></nav></header>

<section class="hero">
<div>
<div class="kicker">MEKANISK UDVIKLING · KONSTRUKTION · PROJEKTLEDELSE</div>
<h1>Mekanisk udvikling<br>og konstruktion.</h1>
<div class="lead">Mekanisk udvikling, konstruktion og teknisk projektarbejde. Opgaver kan løses direkte for en virksomhed eller som ekstern ressource i et eksisterende engineeringteam.</div>
<div class="actions"><button class="btn" onclick="go('kontakt')">KONTAKT</button><button class="btn alt" onclick="go('brancher')">SE OMRÅDER</button></div><div class="ai-example">EKSEMPEL PÅ AI-UNDERSTØTTET KONSTRUKTION</div><div class="hero-config"><div class="cfg-title">KONCEPTKONFIGURATOR · LIVE 3D</div>
<div class="cfg-row"><label>Slædeposition</label><input id="travelSlider" type="range" min="-1100" max="1100" value="220" step="10"><output id="travelOut">220 mm</output></div>
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
<div class="card" onclick="show('cad',this)"><div class="n">04</div><h3>Konceptudvikling</h3><p>Fra behov og idé til funktionsprincip, mekanisk koncept, 3D-layout og et grundlag for den videre konstruktion.</p></div>
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
<div class="model3d concept-static" id="cad3d">
<div class="model-note">KONCEPTUDVIKLING · STABELBARE TRANSPORTRAMMER</div>
<img class="concept-image" src="data:image/webp;base64,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" alt="Stabelbare transportrammer 5 x 6 x 3">
<div class="model-caption">5 × 6 × 3 · STABELBARE TRANSPORTRAMMER</div></div>
</div></div>
</div></div></section>

<section class="section" id="samarbejde"><div class="section-title"><div class="kicker">SAMARBEJDE</div><h2>Indgår dér, hvor der er behov.</h2><p>Opgaverne kan løses direkte for en virksomhed eller som en del af et engineering- eller projektteam. Rollen og omfanget tilpasses den konkrete opgave.</p></div>
<div class="process"><div class="step"><span>01</span><b>Engineering support</b><span>Ekstra kapacitet til mekanisk udvikling og konstruktion i et eksisterende projektteam.</span></div><div class="step"><span>02</span><b>Afgrænset opgave</b><span>En konkret konstruktions-, udviklings- eller beregningsopgave med et tydeligt teknisk scope.</span></div><div class="step"><span>03</span><b>Projektansvar</b><span>Teknisk koordinering af en mekanisk delopgave med grænseflader til kunde, leverandører og øvrige fag.</span></div><div class="step"><span>04</span><b>On-site / remote</b><span>Arbejdet kan indgå tæt i kundens organisation eller udføres mere selvstændigt efter opgavens karakter.</span></div><div class="step"><span>05</span><b>Engineering house</b><span>Kan indgå som ekstern ressource hos engineeringhuse, der har behov for mekanisk kompetence eller ekstra kapacitet.</span></div></div></section>

<section class="section" id="om"><div class="about"><div><div class="kicker">OM SIMGROVA</div><h2>Baggrund og erfaring.</h2><p>Arbejdsområdet er mekanisk udvikling, konstruktion og teknisk projektledelse med fokus på praktiske, gennemarbejdede løsninger.</p><p>Erfaringsområdet spænder fra koncept- og produktudvikling til specialmaskiner, værktøjer, dimensionering, optimering, idriftsættelse, risikovurdering og CE. Arbejdet udføres bl.a. i Siemens NX og Teamcenter.</p><p>Tilgangen er at søge enkle og gennemarbejdede løsninger og holde unødig kompleksitet ude af konstruktionen.</p></div>
<div class="facts"><div class="fact"><b>NX</b><span>3D CAD / KONSTRUKTION</span></div><div class="fact"><b>Teamcenter</b><span>PLM / PROJEKTMILJØ</span></div><div class="fact"><b>Engineering</b><span>UDVIKLING / DIMENSIONERING</span></div><div class="fact"><b>Projekt</b><span>TEKNISK KOORDINERING</span></div></div></div></section>

<section class="section" id="kontakt"><div class="contact"><div><div class="kicker">KONTAKT</div><h2>Kontakt.</h2><p class="lead">Kontakt kan være relevant ved behov for en ekstern maskiningeniør til en konkret opgave, et projektforløb eller som midlertidig engineeringkapacitet.</p><div class="actions"><button class="btn" onclick="location.href='mailto:snc@simgrova.dk?subject=Forespørgsel til SIMGROVA'">E-MAIL</button><button class="btn alt" onclick="location.href='tel:+4521467659'">TELEFON +45 21 46 76 59</button></div></div>
<div class="contactbox premium-card">
  <div class="card-edge"></div>
  <div class="card-content">
    <div class="card-brand">SIMGROVA <span>ApS</span></div>
    <div class="card-rule"></div>
    <div class="card-name"><b>Søren Noe Christiansen</b><br><span>Maskiningeniør</span></div>
    <div class="card-contact"><a href="mailto:snc@simgrova.dk">snc@simgrova.dk</a><br><a href="tel:+4521467659">+45 21 46 76 59</a></div>
    <div class="card-services">Mekanisk udvikling · Konstruktion · Teknisk projektledelse<br>Dimensionering · Specialmaskiner · Risikovurdering &amp; CE</div>
  </div>
</div></div></section>

<div class="footer"><span>SIMGROVA · SIMPLICITY CREATES GROWTH</span><span>MECHANICAL ENGINEERING / DENMARK</span></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
function go(id){document.getElementById(id).scrollIntoView({behavior:'smooth'})}
const content={
energy:{k:"ENERGI / MEKANISK UDVIKLING",t:"Mekaniske løsninger til energiområdet",html:`<p>På energiområdet har arbejdet blandt andet omfattet mekaniske udviklingsopgaver, specialværktøj og udstyr, hvor belastning, håndtering og sikkerhed er væsentlige designforhold.</p><ul><li>Specialværktøj og hjælpeudstyr</li><li>Løfte- og håndteringskoncepter</li><li>Dimensionering og strukturel optimering</li><li>Hydrauliske og mekaniske funktioner</li><li>Produktionsgrundlag, test og dokumentation</li></ul><p>Relevant erfaring omfatter bl.a. udviklingsopgaver og hydraulisk specialværktøj til vind-/energisektoren.</p>`},
food:{k:"FØDEVARER / HYGIENISK KONSTRUKTION",t:"Fødevareudstyr og hygiejnisk konstruktion",html:`<p>Ved fødevareudstyr indgår materialer, geometri, dræning, rengøring og service som naturlige designhensyn. Erfaringen omfatter konstruktion, hvor disse forhold tænkes ind fra starten.</p><ul><li>Hygiejnisk design: drænbar geometri, egnede samlinger og færre døde zoner</li><li>Rengøringsvenlige løsninger og CIP-principper</li><li>Servicevenlig konstruktion med fokus på kontaminationsrisiko</li><li>Køleteknisk udstyr, transportører, pakkemaskiner, Pick & Place, frysere, volumetriske fyldere og mekaniske pakninger</li></ul><p><b>Designgrundlag:</b> EHEDG · 3-A · CIP (Clean In Place).</p>`},
industry:{k:"INDUSTRI / SPECIALMASKINER",t:"Specialmaskiner og produktionsudstyr",html:`<p>Arbejdet kan omfatte nye specialmaskiner, delsystemer eller ændringer af eksisterende produktionsudstyr med fokus på funktion, fremstilling, montage og service.</p><ul><li>Specialmaskiner og produktionsudstyr</li><li>Automatiserede mekaniske bevægelser og emnehåndtering</li><li>Optimering af eksisterende udstyr og cyklustid</li><li>Design for manufacturing og service</li><li>Layout, konstruktion, leverandørdialog, montage og idriftsættelse</li></ul><p>Erfaringen omfatter bl.a. højhastighedsudstyr med krav til stabil produktion og høj OEE.</p>`},
cad:{k:"KONCEPTUDVIKLING / MEKANISKE PRINCIPPER",t:"Fra idé til et mekanisk koncept",html:`<p>Konceptudvikling handler om at finde en enkel og robust løsning på funktion, håndtering, pladsforhold og interfaces, før konstruktionen detaljeres.</p><ul><li>Funktionsprincipper og alternative løsningsforslag</li><li>3D-layout og pladsudnyttelse</li><li>Håndtering, transport og stabling</li><li>Interfaces og indledende dimensionering</li><li>Grundlag for efterfølgende detaljekonstruktion i Siemens NX</li></ul><p>Illustrationen viser et koncept med stabelbare transportrammer i en 5 × 6 × 3 matrix, hvor hver ramme bærer en mindre konstruktion eller et produkt.</p>`}
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
    

    // Fixed rotary workstation.
    cyl(-1.55,-.28,0,.92,.72,"y",MAT.blue,H);

    // Linear axis.
    // The guides are mounted ABOVE the machine plate on proper support blocks.
    // Supports sit between the upper plate and each guide — not as loose corner fasteners.
    const railY=-.27;
    heroMechanism.rail1=box(.85,railY,-.82,3.0,.22,.18,MAT.polished,H);
    heroMechanism.rail2=box(.85,railY,.82,3.0,.22,.18,MAT.polished,H);
    // Lead screw emerges from inside the large rotary drive housing.
    // Extended to the left while keeping the original right-hand end position.
    heroMechanism.screw=cyl(.30,-.04,0,.07,3.90,"x",MAT.brass,H);

    // Four mounting/support blocks under each guide.
    const supportXs=[-.35,.45,1.25,2.05];
    supportXs.forEach(x=>{
      box(x,-.55,-.82,.30,.34,.42,MAT.dark,H);
      box(x,-.55,.82,.30,.34,.42,MAT.dark,H);
      // small seated fixing heads on the support blocks
      bolt(x,-.34,-.82,"y",H);
      bolt(x,-.34,.82,"y",H);
    });

    // Entire robot travels as one assembly.
    const moving=new THREE.Group(); H.add(moving);
    heroMechanism.moving=moving; moving.position.set(1.15,-.02,0);
    box(0,.02,0,1.0,.32,2.0,MAT.steel,moving);
    // guide shoes below the carriage, aligned directly over both rails
    box(-.28,-.19,-.82,.34,.18,.34,MAT.blue,moving);
    box(.28,-.19,-.82,.34,.18,.34,MAT.blue,moving);
    box(-.28,-.19,.82,.34,.18,.34,MAT.blue,moving);
    box(.28,-.19,.82,.34,.18,.34,MAT.blue,moving);
    cyl(0,.42,0,.38,.34,"y",MAT.dark,moving);

    // Cylinder 1 starts at carriage.
    const lift=new THREE.Group(); moving.add(lift);
    lift.position.set(0,.35,0);
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
    heroMechanism.maxTravelMm=1100;
    heroMechanism.maxTravelModel=heroMechanism.travel*.46;
    heroMechanism.applyTravel=mm=>{
      const value=Math.max(-heroMechanism.maxTravelMm,Math.min(heroMechanism.maxTravelMm,+mm||0));
      const dx=(value/heroMechanism.maxTravelMm)*heroMechanism.maxTravelModel;
      moving.position.set(1.15+dx,-.02,0);
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

      heroMechanism.applyTravel(document.getElementById("travelSlider")?.value||220);
    };
  }

  // ENERGY — deployable solar field based on the supplied reference:
  // central transport unit, long wings in ±X, panel long edge transverse (Z),
  // and repeated shallow /\ profiles along the deployment direction.
  if(type==="energy"){
    const E=new THREE.Group(); root.add(E);
    const leaves=[];

    // central transport / deployment container
    box(0,-.72,0,2.35,1.12,1.70,MAT.steel,E);
    box(0,-.12,0,2.18,.10,1.54,MAT.dark,E);
    for(const x of [-1.05,1.05]) for(const z of [-.72,.72])
      box(x,-.70,z,.12,1.30,.12,MAT.dark,E);

    // longitudinal deployment rails under both solar wings
    for(const side of [-1,1]){
      const cx=side*4.95;
      for(const z of [-.78,.78])
        box(cx,-1.05,z,7.55,.10,.10,MAT.polished,E);
    }

    function makeLeaf(x,side,half){
      // Each panel is WIDE ACROSS Z and SHORT in X.
      // Its hinge axis is therefore Z: the panel's long side.
      const pivot=new THREE.Group(); E.add(pivot);
      pivot.position.set(x,-.47,0);

      const pg=new THREE.Group(); pivot.add(pg);
      const short=.86, long=1.78;
      pg.position.x=half*short/2;

      // real PV panel mesh, long dimension across the strip
      const frame=box(0,0,0,short,.055,long,MAT.dark,pg);
      box(0,.035,0,short-.07,.025,long-.07,MAT.solar,pg);

      // simple cell grid
      for(let iz=-2;iz<=2;iz++){
        box(0,.052,iz*(long-.10)/5,short-.10,.008,.012,MAT.polished,pg);
      }
      for(const xx of [-.22,.22]){
        box(xx,.052,0,.012,.008,long-.10,MAT.polished,pg);
      }

      // two hinges along the LONG Z hinge edge
      for(const z of [-.52,.52]){
        cyl(-half*short/2,-.025,z,.045,.20,"z",MAT.brass,pg,18);
        box(-half*(short/2-.06),-.07,z,.14,.08,.28,MAT.dark,pg);
      }

      leaves.push({pivot,side,half,x});
    }

    // Eight shallow /\ modules on each side of the central container.
    // Each /\ consists of two short-X leaves sharing a transverse long-Z ridge hinge.
    const pitch=1.56;
    for(const side of [-1,1]){
      for(let i=0;i<5;i++){
        const center=side*(1.62+i*pitch);

        // transverse ridge/support beam
        box(center,-.49,0,.10,.10,1.90,MAT.dark,E);

        // low support feet at both ends of ridge
        for(const z of [-.82,.82]){
          box(center,-.78,z,.10,.58,.10,MAT.steel,E);
          box(center,-1.08,z,.28,.05,.28,MAT.dark,E);
        }

        // one leaf points toward container, the other away from it
        makeLeaf(center,side,-side);
        makeLeaf(center,side, side);
      }
    }

    // Deployed state: shallow repeated inverted V, almost flat.
    leaves.forEach(p=>{
      // slope is determined by whether leaf extends toward -X or +X
      p.pivot.rotation.z=-p.half*.18;
    });

    // One-time unfolding demonstration: rotation is around Z,
    // i.e. the LONG side of every panel.
    const t0=performance.now();
    webglModels._energyAnimate=()=>{
      const elapsed=(performance.now()-t0)/1000;
      const t=Math.min(1,elapsed/4.6);
      const s=t*t*(3-2*t);
      leaves.forEach((p,k)=>{
        const idx=Math.floor(k/2)%5;
        const delay=idx*.055;
        const u=Math.max(0,Math.min(1,(s-delay)/(1-delay)));
        const folded=-p.half*1.18;
        const deployed=-p.half*.18;
        p.pivot.rotation.z=folded+(deployed-folded)*u;
      });
    };
  }

  // FOOD — detailed hygienic process skid; components are deliberately separated
  // so vessels, heat exchanger, pump train and service equipment remain mechanically readable.
  if(type==="food"){
    const F=new THREE.Group(); root.add(F);

    // Main welded skid with cross-members and adjustable machine feet.
    box(0,-1.36,0,6.20,.18,3.45,MAT.dark,F);
    for(const z of [-1.43,1.43]) box(0,-1.14,z,5.92,.18,.16,MAT.steel,F);
    for(const x of [-2.72,-1.36,0,1.36,2.72]) box(x,-1.14,0,.16,.18,2.88,MAT.steel,F);
    for(const x of [-2.72,2.72]) for(const z of [-1.38,1.38]){
      cyl(x,-1.58,z,.09,.50,"y",MAT.dark,F);
      cyl(x,-1.85,z,.18,.055,"y",MAT.steel,F);
    }

    function vessel(x,z,r,h){
      const T=new THREE.Group(); F.add(T);
      cyl(x,-.04,z,r,h,"y",MAT.polished,T);
      const dome=mesh(new THREE.SphereGeometry(r,36,18,0,Math.PI*2,0,Math.PI/2),MAT.polished,T);
      dome.scale.y=.28; dome.position.set(x,h/2-.04,z);
      const cone=mesh(new THREE.ConeGeometry(r*.82,.44,36),MAT.polished,T);
      cone.position.set(x,-h/2-.25,z); cone.rotation.x=Math.PI;
      for(const ang of [0,2*Math.PI/3,4*Math.PI/3])
        cyl(x+Math.cos(ang)*r*.58,-h/2-.62,z+Math.sin(ang)*r*.58,.052,.76,"y",MAT.steel,T);
      // manway, vent and spray/CIP nozzle
      cyl(x,h/2+.12,z,.20,.10,"y",MAT.dark,T);
      cyl(x,h/2+.29,z,.075,.24,"y",MAT.polished,T);
      pipe([[x-.22,h/2+.02,z],[x-.22,h/2+.28,z],[x-.42,h/2+.28,z]],.038,MAT.polished,T);
      // lower product outlet
      pipe([[x,-h/2-.45,z],[x,-h/2-.73,z],[x+.32,-h/2-.73,z]],.062,MAT.polished,T);
      // side temperature transmitter
      pipe([[x+r,.24,z],[x+r+.20,.24,z]],.028,MAT.polished,T);
      cyl(x+r+.28,.24,z,.08,.12,"x",MAT.blue,T);
    }

    // Two vessels, moved to the left/rear half of the skid.
    vessel(-1.82,-.36,.68,2.18);
    vessel(-.18,-.44,.53,1.68);

    // Main hygienic product header along front edge.
    pipe([[-2.58,-.80,1.12],[-1.82,-.80,1.12],[-.18,-.80,1.12],[1.18,-.80,1.12],[2.48,-.80,1.12]],.066,MAT.polished,F);
    pipe([[-1.82,-.80,1.12],[-1.82,-.80,.36]],.066,MAT.polished,F);
    pipe([[-.18,-.80,1.12],[-.18,-.80,.20]],.066,MAT.polished,F);

    // Four butterfly valve stations.
    for(const x of [-1.20,-.62,.62,1.42]){
      cyl(x,-.80,1.12,.13,.11,"x",MAT.blue,F);
      box(x,-.59,1.12,.055,.30,.055,MAT.dark,F);
      box(x,-.43,1.12,.28,.045,.065,MAT.green,F);
    }

    // Pump train at front-right, isolated from the heat exchanger.
    box(1.72,-1.07,.48,1.72,.12,.72,MAT.steel,F);
    cyl(1.22,-.75,.48,.36,.30,"z",MAT.polished,F);
    torus(1.22,-.75,.66,.28,.05,"z",MAT.dark,F);
    cyl(2.04,-.75,.48,.29,.94,"x",MAT.green,F);
    cyl(1.62,-.75,.48,.09,.44,"x",MAT.dark,F);
    pipe([[1.22,-.75,.78],[1.22,-.75,1.12]],.068,MAT.polished,F);

    // Plate heat exchanger at rear-right: dedicated clear footprint, no overlap with pump/motor.
    const hx=new THREE.Group(); F.add(hx); hx.position.set(1.72,-.05,-1.03);
    for(let i=0;i<16;i++) box(0,0,i*.032,.74,1.26,.020,i%2?MAT.steel:MAT.brass,hx);
    box(0,0,-.11,.92,1.44,.10,MAT.dark,hx);
    box(0,0,.62,.92,1.44,.10,MAT.dark,hx);
    // tie rods
    for(const xx of [-.36,.36]) for(const yy of [-.56,.56])
      cyl(xx,yy,.67,.042,.82,"z",MAT.dark,hx);
    // four hygienic ports
    for(const yy of [-.38,.38]){
      cyl(-.50,yy,.12,.085,.22,"x",MAT.polished,hx);
      cyl(.50,yy,.12,.085,.22,"x",MAT.polished,hx);
    }

    // Separate small green CIP/service tank at far rear-left — clear of HX.
    const cip=new THREE.Group(); F.add(cip);
    cyl(-2.45,-.42,-1.00,.34,1.28,"y",MAT.green,cip);
    const cipTop=mesh(new THREE.SphereGeometry(.34,28,14,0,Math.PI*2,0,Math.PI/2),MAT.green,cip);
    cipTop.scale.y=.25; cipTop.position.set(-2.45,.22,-1.00);
    cyl(-2.45,.34,-1.00,.07,.18,"y",MAT.polished,cip);
    for(const dx of [-.20,.20]) cyl(-2.45+dx,-1.02,-1.00,.04,.36,"y",MAT.steel,cip);

    // CIP pump beside the service tank.
    box(-2.32,-1.05,-.42,.82,.10,.50,MAT.steel,F);
    cyl(-2.45,-.83,-.42,.22,.22,"z",MAT.polished,F);
    cyl(-2.03,-.83,-.42,.18,.48,"x",MAT.green,F);
    pipe([[-2.45,-.83,-.20],[-2.45,-.83,.05],[-2.45,-.80,1.12]],.050,MAT.polished,F);

    // Rear CIP/return header, clearly supported.
    pipe([[-2.45,.48,-1.00],[-2.45,1.18,-1.00],[-1.82,1.18,-1.00],[-.18,1.18,-1.00],[.72,1.18,-1.00]],.052,MAT.polished,F);
    pipe([[-1.82,1.18,-1.00],[-1.82,1.03,-.36]],.052,MAT.polished,F);
    pipe([[-.18,1.18,-1.00],[-.18,.82,-.44]],.052,MAT.polished,F);
    for(const x of [-2.30,-1.05,.42]){
      box(x,.36,-1.00,.07,1.48,.07,MAT.steel,F);
      box(x,-.40,-1.00,.22,.06,.22,MAT.dark,F);
    }

    // Instrument rack, fully supported from skid.
    const inst=new THREE.Group(); F.add(inst);
    for(const x of [-.72,.72]){
      box(x,.04,1.38,.075,2.16,.075,MAT.steel,inst);
      box(x,-1.07,1.38,.28,.07,.28,MAT.dark,inst);
    }
    box(0,1.08,1.38,1.62,.08,.08,MAT.steel,inst);
    for(const x of [-.52,0,.52]){
      pipe([[x,1.04,1.38],[x,.74,1.38],[x,.74,1.12],[x,-.76,1.12]],.020,MAT.polished,inst);
      cyl(x,1.25,1.38,.105,.065,"z",MAT.steel,inst);
      torus(x,1.25,1.425,.083,.013,"z",MAT.dark,inst);
      cyl(x,.90,1.30,.050,.11,"y",MAT.blue,inst);
    }

    // Control cabinet on rear-right corner, on real legs and away from HX.
    const ctrl=new THREE.Group(); F.add(ctrl);
    box(2.58,.02,-.82,.62,1.16,.22,MAT.steel,ctrl);
    box(2.58,.18,-.695,.40,.34,.026,MAT.glass,ctrl);
    for(const z of [-.90,-.74]){
      box(2.38,-.78,z,.065,.78,.065,MAT.dark,ctrl);
      box(2.38,-1.19,z,.22,.06,.22,MAT.dark,ctrl);
    }
    // cable tray to main pump motor
    pipe([[2.36,-.42,-.72],[2.36,-.42,.05],[2.18,-.58,.34],[2.10,-.70,.46]],.028,MAT.dark,ctrl);

    // Additional hygienic components: inline filter, sample valve and flow meter.
    // Filter housing on product header.
    cyl(2.36,-.52,1.12,.18,.46,"y",MAT.polished,F);
    cyl(2.36,-.26,1.12,.11,.08,"y",MAT.dark,F);
    // sample valve
    pipe([[-1.20,-.80,1.12],[-1.20,-.54,1.12]],.030,MAT.polished,F);
    cyl(-1.20,-.42,1.12,.055,.12,"y",MAT.green,F);
    // flow meter body
    cyl(.95,-.80,1.12,.13,.28,"x",MAT.polished,F);
    box(.95,-.56,1.12,.18,.22,.12,MAT.blue,F);

    // Small hose station / service connection.
    torus(2.62,-.18,.72,.20,.035,"x",MAT.dark,F);
    pipe([[2.62,-.40,.72],[2.62,-.72,.72]],.025,MAT.dark,F);
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

  // CONCEPT DEVELOPMENT — compact self-leveling scissor work platform concept.
  if(type==="cad"){
    const G=new THREE.Group(); root.add(G);

    // mobile base / chassis
    box(0,-1.18,0,4.70,.38,2.65,MAT.dark,G);
    box(0,-.94,0,4.28,.16,2.30,MAT.steel,G);
    for(const x of [-1.75,1.75]) for(const z of [-1.22,1.22]){
      cyl(x,-1.30,z,.30,.24,"z",MAT.dark,G);
      cyl(x,-1.30,z,.16,.26,"z",MAT.steel,G);
    }

    // four deployable stabilizer beams
    for(const x of [-1.75,1.75]) for(const z of [-1,1]){
      box(x,-.78,z*1.55,1.15,.12,.14,MAT.steel,G);
      cyl(x+(x<0?-.45:.45),-1.05,z*1.98,.08,.54,"y",MAT.dark,G);
      cyl(x+(x<0?-.45:.45),-1.34,z*1.98,.20,.06,"y",MAT.steel,G);
    }

    // scissor mechanism — two planes, real pivot pins
    const lift=new THREE.Group(); G.add(lift); lift.position.y=-.68;
    function scissorPlane(z){
      const L=2.45, h=1.52;
      beam([-L/2,0,z],[L/2,h,z],.14,MAT.blue,lift);
      beam([-L/2,h,z],[L/2,0,z],.14,MAT.blue,lift);
      for(const x of [-L/2,0,L/2]){
        const yy=x===0?h/2:(x<0?0:h);
        cyl(x,yy,z,.13,.24,"z",MAT.brass,lift);
      }
    }
    scissorPlane(-.72); scissorPlane(.72);
    // cross shafts between both scissor planes
    for(const x of [-1.22,0,1.22]) cyl(x,.76,0,.09,1.55,"z",MAT.polished,lift);

    // hydraulic cylinder drives the mechanism
    const ram=new THREE.Group(); lift.add(ram);
    ram.rotation.z=-.55;
    cyl(-.34,.36,0,.12,1.42,"y",MAT.polished,ram);
    cyl(-.34,.82,0,.075,1.20,"y",MAT.brass,ram);

    // upper work platform with two longitudinal support beams
    box(0,1.68,0,3.25,.18,2.02,MAT.steel,lift);
    box(0,1.83,0,3.10,.10,1.88,MAT.dark,lift);
    for(const z of [-.72,.72]) box(0,1.53,z,2.90,.14,.16,MAT.polished,lift);
    for(const x of [-1.18,1.18]) cyl(x,1.53,0,.10,1.62,"z",MAT.brass,lift);

    // guard rails
    for(const z of [-.88,.88]){
      box(0,2.58,z,3.05,.06,.06,MAT.polished,lift);
      for(const x of [-1.48,-.50,.50,1.48]) box(x,2.18,z,.055,.78,.055,MAT.polished,lift);
    }
    for(const x of [-1.48,1.48]){
      box(x,2.58,0,.06,.06,1.76,MAT.polished,lift);
      for(const z of [-.88,0,.88]) box(x,2.18,z,.055,.78,.055,MAT.polished,lift);
    }

    // compact control box
    box(1.18,2.02,.68,.38,.46,.22,MAT.blue,lift);
    box(1.18,2.08,.81,.20,.12,.025,MAT.glass,lift);

    // design reference dimensions / layout markers
    for(const x of [-2.10,2.10]) box(x,-.65,0,.035,.035,3.15,MAT.brass,G);
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
    cad:{dist:10.2,target:[0,.05,0]}
  };
  const P=presets[type]||presets.hero;
  let yaw=type==="energy"?.18:.48, pitch=type==="industry"?.25:.32, dist=P.dist;
  if(type==="hero") heroMechanism.setView=mode=>{
    // Conventional principal views: no residual oblique tilt.
    if(mode==="top"){yaw=0;pitch=Math.PI/2-.001;dist=P.dist*1.06;}
    else if(mode==="front"){yaw=Math.PI/2;pitch=0;dist=P.dist;}
    else if(mode==="side"){yaw=0;pitch=0;dist=P.dist;}
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
    if(type==="energy" && webglModels._energyAnimate) webglModels._energyAnimate();
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
function cfgLabels(){document.getElementById("travelOut").textContent=travelSlider.value+" mm";document.getElementById("sizeOut").textContent=["XS","S","M","L","XL"][+sizeSlider.value-1];document.getElementById("heightOut").textContent=heightSlider.value+" mm";document.getElementById("reachOut").textContent=reachSlider.value+" mm";}
function liveGeometry(){cfgLabels();heroMechanism.liveUpdate?.(sizeSlider.value,heightSlider.value,reachSlider.value);}
travelSlider.addEventListener("input",()=>{cfgLabels();heroMechanism.applyTravel?.(travelSlider.value);});
[sizeSlider,heightSlider,reachSlider].forEach(s=>s.addEventListener("input",liveGeometry));
document.querySelectorAll(".view-modes button[data-view]").forEach(b=>b.addEventListener("click",()=>{document.querySelectorAll(".view-modes button[data-view]").forEach(x=>x.classList.remove("active"));b.classList.add("active");heroMechanism.setView?.(b.dataset.view);}));
document.getElementById("resetCfg").addEventListener("click",()=>{travelSlider.value=220;sizeSlider.value=3;heightSlider.value=1300;reachSlider.value=1000;cfgLabels();heroMechanism.liveUpdate?.(3,1300,1000);heroMechanism.applyTravel?.(220);heroMechanism.setView?.("iso");document.querySelectorAll(".view-modes button[data-view]").forEach(x=>x.classList.toggle("active",x.dataset.view==="iso"));});
cfgLabels();heroMechanism.liveUpdate?.(3,1300,1000);
</script></body></html>
"""
components.html(page, height=4300, scrolling=True)

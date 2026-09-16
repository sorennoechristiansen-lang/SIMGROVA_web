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
</style></head><body>
<div class="shell">
<header><div class="brand">SIMGROVA <small>MEKANISK UDVIKLING</small></div>
<nav><button onclick="go('ydelser')">YDELSER</button><button onclick="go('brancher')">BRANCHER</button><button onclick="go('samarbejde')">SAMARBEJDE</button><button onclick="go('om')">OM SIMGROVA</button><button onclick="go('kontakt')">KONTAKT</button></nav></header>

<section class="hero">
<div>
<div class="kicker">MEKANISK UDVIKLING · KONSTRUKTION · PROJEKTLEDELSE</div>
<h1>Mekanisk udvikling<br>og konstruktion.</h1>
<div class="lead">Mekanisk udvikling, konstruktion og teknisk projektarbejde. Opgaver kan løses direkte for en virksomhed eller som ekstern ressource i et eksisterende engineeringteam.</div>
<div class="actions"><button class="btn" onclick="go('kontakt')">KONTAKT</button><button class="btn alt" onclick="go('brancher')">SE OMRÅDER</button></div>
</div>
<div class="visual">
<div class="model3d" id="hero3d">
 <div class="model-note">3D KONCEPTMODEL · TRÆK FOR AT ROTERE · SCROLL FOR ZOOM</div>
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

function setupModel(id,type){
 if(built[id]) return; built[id]=true;
 const host=document.getElementById(id); if(!host)return;
 const stage=host.querySelector(".model-stage");
 if(type==="hero"){
   box(stage,-230,85,-70,460,22,150);
   box(stage,-205,-95,-55,24,180,24); box(stage,181,-95,-55,24,180,24);
   box(stage,-205,-110,-55,410,24,24);
   box(stage,-75,-75,-25,150,52,80);
   box(stage,-12,-23,-5,24,115,24,"accent");
   box(stage,-62,88,10,125,28,70,"green");
   cyl(stage,125,-35,0,38); cyl(stage,125,-35,5,12);
 }
 if(type==="energy"){
   // Containerised deployable photovoltaic plant:
   // transport module, rail beams, hinge/yoke points and accordion panel wings.
   const cont=box(stage,-105,-42,-55,210,102,110,"steel");
   faceLabel(cont,"SIMGROVA · ENERGY",11);

   // ISO-like corner posts and roof/base rails
   [-105,89].forEach(x=>{
      box(stage,x,-52,-65,16,122,16,"darksteel");
      box(stage,x,-52,49,16,122,16,"darksteel");
   });
   box(stage,-105,-54,-65,210,14,16,"darksteel");
   box(stage,-105,56,-65,210,14,16,"darksteel");
   box(stage,-105,-54,49,210,14,16,"darksteel");
   box(stage,-105,56,49,210,14,16,"darksteel");

   // central deployment cassette
   box(stage,-82,-18,60,164,50,22,"darksteel");
   box(stage,-94,38,60,188,12,18,"accent");

   // two long ground rails
   box(stage,-585,82,-38,1170,10,14,"steel");
   box(stage,-585,82,42,1170,10,14,"steel");

   // accordion-like panel wings. Each module gets a frame + PV face.
   const pw=106, ph=72, gap=9;
   for(let side of [-1,1]){
      for(let i=0;i<4;i++){
         let x = side<0 ? -118-(i+1)*(pw+gap) : 118+i*(pw+gap);
         // support carriage below each panel
         box(stage,x+10,70,-26,pw-20,8,82,"steel");
         box(stage,x+3,4,18,pw,ph,7,"solar");
         // hinge block between modules
         let hx=side<0 ? x+pw-3 : x-7;
         box(stage,hx,26,12,10,28,18,"accent");
      }
   }

   // deployment drive / inverter cabinet
   box(stage,-42,20,-5,84,55,55,"green");
   cyl(stage,-58,30,58,16,"bearing");
   cyl(stage,26,30,58,16,"bearing");
 }
 if(type==="food"){
   // Hygienic CIP/process skid: polished vessels, sanitary headers, pump,
   // plate heat exchanger, valve cluster and control cabinet.
   box(stage,-255,110,-82,510,16,170,"steel");
   box(stage,-242,90,-64,484,12,18,"steel");
   box(stage,-242,90,50,484,12,18,"steel");

   function vessel(cx){
      // faceted stainless vessel silhouette with top/bottom bands
      box(stage,cx-50,-92,-12,100,120,94,"steel");
      box(stage,cx-46,-126,-8,92,34,86,"steel");
      box(stage,cx-38,28,-2,76,28,78,"steel");
      box(stage,cx-32,56,2,14,52,14,"darksteel");
      box(stage,cx+18,56,2,14,52,14,"darksteel");
      // top manway and agitator drive
      cyl(stage,cx-22,-137,46,22,"pipeend");
      box(stage,cx-24,-166,8,48,36,46,"green");
      box(stage,cx-6,-132,10,12,30,12,"darksteel");
      // level / instrument block
      box(stage,cx+34,-55,42,18,46,16,"accent");
   }
   vessel(-108); vessel(78);

   // sanitary lower product header
   box(stage,-220,50,60,372,14,14,"steel");
   box(stage,-108,25,60,14,40,14,"steel");
   box(stage,78,25,60,14,40,14,"steel");

   // upper CIP return header
   box(stage,-216,-120,64,370,12,12,"steel");
   box(stage,-108,-120,64,12,48,12,"steel");
   box(stage,78,-120,64,12,48,12,"steel");

   // hygienic valves / clamp-like faces
   [[-22,42],[118,42],[-122,-96],[64,-96]].forEach(p=>{
      box(stage,p[0],p[1],54,30,30,28,"accent");
      cyl(stage,p[0]+1,p[1]+1,72,14,"pipeend");
   });

   // centrifugal pump + motor
   box(stage,-232,42,2,78,50,60,"darksteel");
   cyl(stage,-170,54,40,28,"pipeend");
   box(stage,-244,92,-2,126,10,72,"steel");

   // plate heat exchanger
   box(stage,150,-50,-12,46,128,62,"yellow");
   box(stage,140,-60,-18,66,12,74,"darksteel");
   box(stage,140,78,-18,66,12,74,"darksteel");
   for(let yy=-36;yy<58;yy+=18) box(stage,155,yy,51,36,4,5,"steel");

   // controls
   const cab=box(stage,208,-108,-58,68,170,48,"steel");
   faceLabel(cab,"CIP",15);
 }
 if(type==="industry"){
   // Roll-forming machine inspired by real modular forming stands:
   // bed, uprights, bearing blocks, adjustment screws, shafts and changing roll tooling.
   box(stage,-285,112,-88,570,18,190,"darksteel");
   box(stage,-270,88,-70,540,16,30,"steel");
   box(stage,-270,88,56,540,16,30,"steel");

   const xs=[-235,-145,-55,35,125,215];
   xs.forEach((x,i)=>{
      // rigid C/portal stand
      box(stage,x,-92,-58,18,180,28,"darksteel");
      box(stage,x+62,-92,-58,18,180,28,"darksteel");
      box(stage,x,-102,-58,80,20,28,"darksteel");

      // upper/lower bearing housings
      box(stage,x+4,-51,-14,26,44,38,"yellow");
      box(stage,x+50,-51,-14,26,44,38,"yellow");
      box(stage,x+4,22,-14,26,44,38,"yellow");
      box(stage,x+50,22,-14,26,44,38,"yellow");

      // vertical adjustment screws + caps
      box(stage,x+15,-80,4,9,32,9,"steel");
      box(stage,x+56,-80,4,9,32,9,"steel");
      cyl(stage,x+7,-91,12,10,"bearing");
      cyl(stage,x+48,-91,12,10,"bearing");

      // shaft ends / bearings
      cyl(stage,x+5,-39,30,13,"bearing");
      cyl(stage,x+49,-39,30,13,"bearing");
      cyl(stage,x+5,34,30,13,"bearing");
      cyl(stage,x+49,34,30,13,"bearing");

      // progressively narrower roll tooling
      const rr=24-i*1.7;
      cyl(stage,x+27,-41,43,rr,"roller");
      cyl(stage,x+27,32,43,rr,"roller");
      cyl(stage,x+27,-41,47,Math.max(9,rr-10),"black");
      cyl(stage,x+27,32,47,Math.max(9,rr-10),"black");
   });

   // sheet/profile path
   box(stage,-310,4,47,625,7,58,"green");
   // entry guide and exit profile supports
   box(stage,-318,-18,34,44,50,12,"steel");
   box(stage,280,-18,34,44,50,12,"steel");
 }
 if(type==="cad"){
   // Deployable containerised machine concept:
   // ISO-like structural frame, opened side doors, telescopic rails,
   // slide-out machine platform and compact handling mechanism.
   const cont=box(stage,-170,-72,-62,340,144,124,"steel");
   faceLabel(cont,"SIMGROVA",18);

   // corner posts + top/bottom rails
   [-170,154].forEach(x=>{
      box(stage,x,-82,-72,16,164,16,"darksteel");
      box(stage,x,-82,52,16,164,16,"darksteel");
   });
   box(stage,-170,-82,-72,340,16,16,"darksteel");
   box(stage,-170,66,-72,340,16,16,"darksteel");
   box(stage,-170,-82,52,340,16,16,"darksteel");
   box(stage,-170,66,52,340,16,16,"darksteel");

   // corrugation/ribs to make the container readable as a container
   for(let x=-142;x<145;x+=28){
      box(stage,x,-66,57,5,130,5,"darksteel");
   }

   // large side doors opened outward
   panel(stage,-272,-62,-8,96,126,9,"green");
   panel(stage,176,-62,-8,96,126,9,"green");
   // door frames / hinges
   box(stage,-184,-62,-8,10,126,14,"accent");
   box(stage,166,-62,-8,10,126,14,"accent");

   // telescopic slide rails
   box(stage,-90,74,-42,310,10,18,"darksteel");
   box(stage,-90,74,30,310,10,18,"darksteel");
   box(stage,5,88,-52,245,14,104,"steel");

   // machine module on slide-out platform
   box(stage,92,26,-20,112,62,82,"accent");
   box(stage,106,-18,-8,84,42,58,"steel");
   box(stage,128,-56,2,20,40,20,"darksteel");

   // compact articulated handling arm
   box(stage,150,-82,12,18,54,18,"darksteel");
   box(stage,150,-84,12,74,16,16,"accent");
   cyl(stage,143,-90,28,14,"bearing");
   cyl(stage,207,-90,28,12,"bearing");
   box(stage,212,-82,15,16,48,16,"darksteel");

   // deployed support feet
   box(stage,18,100,-48,14,48,14,"darksteel");
   box(stage,210,100,-48,14,48,14,"darksteel");
   box(stage,18,140,-58,42,8,34,"steel");
   box(stage,196,140,-58,42,8,34,"steel");
 }
 let rx=(type==="industry"?-14:-18),ry=(type==="energy"?18:28),scale=(type==="energy"?0.58:type==="food"?0.82:type==="industry"?0.66:type==="cad"?0.74:1),drag=false,px=0,py=0,auto=true;
 function draw(){stage.style.transform=`rotateX(${rx}deg) rotateY(${ry}deg) scale(${scale})`}
 function animate(){if(auto&&!drag){ry+=.055;draw()}requestAnimationFrame(animate)}
 draw(); animate();
 host.addEventListener("pointerdown",ev=>{auto=false;drag=true;px=ev.clientX;py=ev.clientY;host.setPointerCapture(ev.pointerId)});
 host.addEventListener("pointerup",()=>drag=false); host.addEventListener("pointercancel",()=>drag=false);
 host.addEventListener("pointermove",ev=>{if(!drag)return;ry+=(ev.clientX-px)*.45;rx-=(ev.clientY-py)*.45;px=ev.clientX;py=ev.clientY;draw()});
 host.addEventListener("wheel",ev=>{ev.preventDefault();scale*=ev.deltaY>0?.92:1.08;scale=Math.max(.55,Math.min(1.7,scale));draw()},{passive:false});
}
setupModel("hero3d","hero");
setupModel("energy3d","energy");
document.getElementById("dtext").innerHTML=content.energy.html;

</script></body></html>
"""
components.html(page, height=4300, scrolling=True)

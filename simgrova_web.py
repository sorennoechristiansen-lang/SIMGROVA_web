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

/* v11: one consistent horizontal safe area across the entire page */
:root{--page-max:1440px;--page-pad:clamp(32px,5vw,78px)}
.shell{width:100%!important;max-width:var(--page-max)!important;margin-left:auto!important;margin-right:auto!important;padding-left:var(--page-pad)!important;padding-right:var(--page-pad)!important}
#services,#branches,#collaboration,#about,#contact,
.services,.branches,.collaboration,.about,.contact{
  width:100%!important;
  max-width:var(--page-max)!important;
  margin-left:auto!important;
  margin-right:auto!important;
  padding-left:var(--page-pad)!important;
  padding-right:var(--page-pad)!important;
}
#collaboration *, .collaboration *{min-width:0}
@media(max-width:900px){
 :root{--page-pad:24px}
}

/* v12: SAMARBEJDE has the actual Danish id #samarbejde */
#samarbejde .process{
  width:calc(100% - clamp(40px,6vw,110px))!important;
  margin-left:auto!important;
  margin-right:auto!important;
}
@media(max-width:900px){
  #samarbejde .process{width:100%!important}
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
<div class="model3d" id="energy3d"><div class="model-note">ENERGI · SPECIALVÆRKTØJ / HÅNDTERING</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">PRINCIPMODEL</div></div>
</div>
<div class="scene" id="food">
<div class="model3d" id="food3d"><div class="model-note">FØDEVARER · TANK / PROCESRØR</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">HYGIENISK PRINCIPMODEL</div></div>
</div>
<div class="scene" id="industry">
<div class="model3d" id="industry3d"><div class="model-note">INDUSTRI · SPECIALMASKINE / AKSER</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">PRINCIPMODEL</div></div>
</div>
<div class="scene" id="cad">
<div class="model3d" id="cad3d"><div class="model-note">SIMGROVA 3D · TRÆK FOR AT ROTERE · SCROLL FOR ZOOM</div><div class="model-grid"></div><div class="model-stage"></div><div class="model-caption">CAD / ENGINEERING</div></div>
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
   box(stage,-215,85,-65,430,20,130);
   box(stage,-190,-95,-50,22,180,22); box(stage,168,-95,-50,22,180,22);
   box(stage,-190,-110,-50,380,22,22);
   box(stage,-75,-82,-15,150,42,70);
   box(stage,-10,-40,0,20,125,20,"accent");
   box(stage,-85,75,5,170,35,85,"green");
   box(stage,-110,40,-5,220,16,25);
 }
 if(type==="food"){
   // Robust process-equipment model built entirely with the same proven 3D box engine.
   // Stainless process skid, two vessels, sanitary pipe headers, pump and cabinet.
   box(stage,-250,108,-80,500,18,165);

   // skid rails
   box(stage,-235,88,-62,470,14,20);
   box(stage,-235,88,48,470,14,20);

   // two simplified vertical process vessels: stacked solid sections
   function vessel(cx){
      box(stage,cx-48,-92,-12,96,118,92);
      box(stage,cx-40,-126,-8,80,34,82);
      box(stage,cx-34,26,-5,68,28,74);
      box(stage,cx-31,54,0,14,54,14);
      box(stage,cx+17,54,0,14,54,14);
      // top agitator / drive
      box(stage,cx-22,-160,4,44,34,44,"green");
      box(stage,cx-6,-128,5,12,28,12);
   }
   vessel(-105); vessel(80);

   // lower sanitary pipe header
   box(stage,-215,48,58,365,16,16);
   box(stage,-105,24,58,16,38,16);
   box(stage,80,24,58,16,38,16);

   // upper CIP/return header and vertical drops
   box(stage,-210,-118,62,360,14,14);
   box(stage,-105,-118,62,14,46,14);
   box(stage,80,-118,62,14,46,14);

   // valve bodies
   box(stage,-20,40,53,28,28,28,"accent");
   box(stage,120,40,53,28,28,28,"accent");
   box(stage,-119,-94,56,28,28,28,"accent");
   box(stage,66,-94,56,28,28,28,"accent");

   // pump + motor
   box(stage,-220,42,5,72,48,58,"accent");
   cyl(stage,-170,58,38,25);
   box(stage,-240,90,0,112,12,70);

   // plate heat exchanger/process module
   box(stage,155,-45,-12,42,122,58,"green");
   box(stage,145,-56,-18,62,12,70);
   box(stage,145,77,-18,62,12,70);

   // control cabinet
   box(stage,205,-105,-58,64,165,44);
 }
 if(type==="industry"){
   box(stage,-225,90,-70,450,22,145);
   box(stage,-200,-105,-55,24,195,24); box(stage,176,-105,-55,24,195,24);
   box(stage,-200,-120,-55,400,24,24);
   box(stage,-135,-75,-20,270,28,45);
   box(stage,-65,-100,0,115,55,70);
   box(stage,-10,-45,5,20,125,20,"accent");
   box(stage,-65,78,10,130,30,70,"green");
   cyl(stage,115,-65,5,32);
 }
 if(type==="cad"){
   const main=box(stage,-145,-45,-50,290,90,110);
   main.querySelector(".front").innerHTML="<div style='width:100%;height:100%;display:flex;align-items:center;justify-content:center;font:700 25px Arial;letter-spacing:.14em;color:#244b53'>SIMGROVA</div>";
   main.querySelector(".top").innerHTML="<div style='width:100%;height:100%;display:flex;align-items:center;justify-content:center;font:700 12px monospace;letter-spacing:.12em;color:#244b53'>ENGINEERING</div>";
 }
 let rx=-18,ry=28,scale=(type==="food"?0.86:1),drag=false,px=0,py=0,auto=true;
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

const oldShow=show;
show=function(id,el){
 oldShow(id,el);
 const map={energy:"energy3d",food:"food3d",industry:"industry3d",cad:"cad3d"};
 setTimeout(()=>setupModel(map[id],id),20);
}
</script></body></html>
"""
components.html(page, height=4300, scrolling=True)

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SIMGROVA | Mechanical Engineering",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
html,body,[data-testid="stAppViewContainer"],.stApp{background:#f4f2eb!important}
[data-testid="stHeader"],[data-testid="stToolbar"],#MainMenu,footer{visibility:hidden}
.block-container{max-width:100%!important;padding:0!important}
iframe{display:block}
</style>
""", unsafe_allow_html=True)

page = r"""
<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
:root{
 --paper:#f4f2eb; --ink:#20353a; --muted:#6e7d7e; --line:#ccd6d2;
 --blue:#347e8c; --blue2:#8cb8bd; --warm:#d28a57; --green:#799b80;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--paper);color:var(--ink);font-family:Arial,sans-serif;overflow:hidden}
.app{height:100vh;min-height:690px;padding:28px 4.5vw 24px;display:grid;grid-template-rows:48px 1fr 92px}
header{display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--line)}
.brand{font-size:20px;font-weight:700;letter-spacing:.16em}
.brand small{font:10px monospace;color:var(--blue);margin-left:12px;letter-spacing:.12em}
nav{display:flex;gap:30px;font:11px monospace;letter-spacing:.1em;color:var(--muted)}
.main{display:grid;grid-template-columns:42% 58%;align-items:center;min-height:0}
.copy{padding-right:4vw}
.kicker{font:11px monospace;letter-spacing:.18em;color:var(--blue);margin-bottom:22px}
h1{font-size:clamp(44px,5.1vw,78px);font-weight:400;line-height:.96;letter-spacing:-.055em;margin:0 0 25px}
.lead{font-size:clamp(16px,1.35vw,21px);line-height:1.55;color:#5d6e70;max-width:570px}
.note{margin-top:28px;font:10px monospace;letter-spacing:.1em;color:#879393}
.visual{height:min(61vh,570px);min-height:430px;position:relative;border-left:1px solid var(--line)}
.scene{position:absolute;inset:0;opacity:0;transition:opacity .45s ease;pointer-events:none}
.scene.active{opacity:1;pointer-events:auto}
svg{width:100%;height:100%}
.label{font:11px monospace;fill:#657779;letter-spacing:1px}
.dim{stroke:#91a6a5;stroke-width:1;fill:none}
.mechanic{stroke:#347e8c;stroke-width:3;fill:none;stroke-linecap:round;stroke-linejoin:round}
.soft{stroke:#8cb8bd;stroke-width:1.4;fill:none}
.solid{fill:#347e8c}
.warm{stroke:#d28a57;fill:none;stroke-width:2}
.green{stroke:#799b80;fill:none;stroke-width:2}
.tabs{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line)}
.tab{border:0;border-right:1px solid var(--line);background:transparent;text-align:left;padding:18px 24px;color:var(--ink);cursor:pointer;transition:.2s}
.tab:last-child{border-right:0}
.tab:hover,.tab.active{background:#e9ece5}
.tab .n{font:10px monospace;color:#83908f}
.tab strong{display:block;margin-top:7px;font-size:15px;letter-spacing:.09em}
.tab span{font-size:11px;color:#738181}
.sun{animation:sunmove 9s ease-in-out infinite alternate}
.panel{transform-origin:425px 315px;animation:track 9s ease-in-out infinite alternate}
.heat{animation:heat 2.4s linear infinite}
.drill{animation:drill 3.2s ease-in-out infinite alternate}
.food1{animation:foodmove 5s linear infinite}
.food2{animation:foodmove 5s linear infinite;animation-delay:-2.5s}
.picker{transform-origin:410px 160px;animation:pick 4s ease-in-out infinite}
.gear{transform-origin:445px 285px;animation:spin 9s linear infinite}
.slider{animation:slide 4s ease-in-out infinite alternate}
@keyframes sunmove{from{transform:translate(-80px,70px)}to{transform:translate(100px,-40px)}}
@keyframes track{from{transform:rotate(-10deg)}to{transform:rotate(13deg)}}
@keyframes heat{to{stroke-dashoffset:-28}}
@keyframes drill{from{transform:translateY(-25px)}to{transform:translateY(65px)}}
@keyframes foodmove{from{transform:translateX(-150px)}to{transform:translateX(500px)}}
@keyframes pick{0%,20%{transform:rotate(-14deg)}45%,65%{transform:rotate(17deg)}100%{transform:rotate(-14deg)}}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes slide{from{transform:translateX(-55px)}to{transform:translateX(55px)}}
@media(max-width:850px){
 html,body{overflow:auto}.app{height:auto;min-height:100vh;grid-template-rows:auto auto auto;padding:20px}
 header{padding-bottom:14px} nav{display:none}
 .main{grid-template-columns:1fr}.copy{padding:55px 0 25px}
 .visual{border-left:0;border-top:1px solid var(--line);height:430px}
 .tabs{grid-template-columns:1fr}.tab{border-right:0;border-bottom:1px solid var(--line)}
}
</style>
</head>
<body>
<div class="app">
<header>
 <div class="brand">SIMGROVA <small>MECHANICAL ENGINEERING</small></div>
 <nav><span>CONCEPT</span><span>PROTOTYPE</span><span>ENGINEERING</span><span>CONTACT</span></nav>
</header>

<section class="main">
 <div class="copy">
   <div class="kicker" id="kicker">ENERGY / CONCEPT 01</div>
   <h1 id="headline">Mechanical ideas.<br>Developed into reality.</h1>
   <div class="lead" id="lead">A solar tracking concept where the panel follows the sun through a simple mechanical rotation. The animation shows the principle — not a completed SIMGROVA project.</div>
   <div class="note">IDEA → CONCEPT → PROTOTYPE → TEST → PRODUCT / MACHINE</div>
 </div>

 <div class="visual">
   <!-- ENERGY: deliberately recognisable solar tracker + geothermal section -->
   <div class="scene active" id="energy">
   <svg viewBox="0 0 720 520">
     <path class="dim" d="M70 420H665M90 430v-20M645 430v-20"/>
     <text class="label" x="285" y="451">SOLAR TRACKING / PRINCIPLE STUDY</text>

     <g class="sun">
       <circle cx="565" cy="115" r="35" class="warm"/>
       <path class="warm" d="M565 62v-18M565 186v-18M512 115h-18M636 115h-18M527 77l-13-13M603 153l13 13M603 77l13-13M527 153l-13 13"/>
     </g>

     <g class="panel">
       <path class="mechanic" d="M300 245L540 205L555 292L315 332Z"/>
       <path class="soft" d="M360 235l15 87M420 225l15 87M480 215l15 87M307 273l240-40M312 302l240-40"/>
       <path class="mechanic" d="M425 315v92M382 407h86"/>
       <circle cx="425" cy="315" r="12" class="mechanic"/>
     </g>
     <path class="dim" d="M425 315A92 92 0 0 1 500 262"/>
     <text class="label" x="488" y="306">TRACKING AXIS</text>

     <g opacity=".75">
       <path class="green" d="M100 420V310h80"/>
       <g class="drill">
         <path class="mechanic" d="M140 315v78"/>
         <path class="soft" d="M132 330l16 12-16 12 16 12-16 12"/>
       </g>
       <path class="green heat" stroke-dasharray="7 9" d="M115 405C80 370 88 335 112 316"/>
       <text class="label" x="74" y="290">GEOTHERMAL</text>
       <text class="label" x="74" y="305">CONCEPT</text>
     </g>
   </svg>
   </div>

   <!-- FOOD: recognisable conveyor + products + pick arm -->
   <div class="scene" id="food">
   <svg viewBox="0 0 720 520">
     <text class="label" x="205" y="85">HIGH-SPEED PRODUCT HANDLING / PRINCIPLE</text>
     <path class="mechanic" d="M75 355H650"/>
     <path class="soft" d="M90 382H635M105 355v27M150 355v27M195 355v27M240 355v27M285 355v27M330 355v27M375 355v27M420 355v27M465 355v27M510 355v27M555 355v27M600 355v27"/>
     <circle cx="105" cy="369" r="22" class="soft"/><circle cx="620" cy="369" r="22" class="soft"/>

     <g class="food1"><rect x="120" y="317" width="48" height="36" rx="7" class="green"/><circle cx="144" cy="335" r="5" class="solid"/></g>
     <g class="food2"><rect x="120" y="317" width="48" height="36" rx="7" class="green"/><circle cx="144" cy="335" r="5" class="solid"/></g>

     <g class="picker">
       <circle cx="410" cy="160" r="24" class="mechanic"/>
       <path class="mechanic" d="M410 184L455 250L430 305"/>
       <path class="mechanic" d="M418 303l12 18M442 304l-12 17"/>
       <circle cx="455" cy="250" r="9" class="mechanic"/>
     </g>
     <path class="dim" d="M300 130H520M300 122v16M520 122v16"/>
     <text class="label" x="357" y="115">PICK / PLACE AXIS</text>
     <path class="warm" d="M535 330h72v-78h-72z"/>
     <text class="label" x="540" y="239">SORT / PROCESS</text>
   </svg>
   </div>

   <!-- INDUSTRY: recognisable gear drive + linear slide + gripper -->
   <div class="scene" id="industry">
   <svg viewBox="0 0 720 520">
     <text class="label" x="205" y="78">SPECIAL MACHINE / MECHANICAL MOTION</text>
     <rect x="105" y="365" width="510" height="42" class="soft"/>
     <path class="mechanic" d="M145 365V170h95v195"/>
     <path class="soft" d="M165 190h55v55h-55z"/>

     <g class="gear">
       <circle cx="445" cy="285" r="64" class="mechanic"/>
       <circle cx="445" cy="285" r="20" class="mechanic"/>
       <path class="mechanic" d="M445 221v-18M445 367v-18M381 285h-18M527 285h-18M400 240l-13-13M503 343l-13-13M490 240l13-13M387 343l13-13"/>
     </g>

     <path class="mechanic" d="M240 275H365"/>
     <g class="slider">
       <rect x="275" y="252" width="70" height="46" rx="5" class="mechanic"/>
       <path class="mechanic" d="M275 275h-52M223 257v36"/>
       <path class="mechanic" d="M210 257l13-12M210 293l13 12"/>
     </g>
     <path class="dim" d="M240 325h125M240 317v16M365 317v16"/>
     <text class="label" x="262" y="348">LINEAR MOTION</text>
     <path class="warm" d="M545 350v-100M530 250h30M530 350h30"/>
     <text class="label" x="570" y="300">WORKPIECE</text>
   </svg>
   </div>

   <!-- AI + CAD: interactive 3D block, drag to rotate -->
   <div class="scene" id="aicad" style="pointer-events:auto">
     <div style="position:absolute;left:28px;top:22px;z-index:3;font:11px monospace;color:#657779;letter-spacing:1px">
       INTERACTIVE 3D / DRAG TO ROTATE · SCROLL TO ZOOM
     </div>
     <div id="cad3d" style="position:absolute;inset:45px 8px 5px 8px"></div>
   </div>
 </div>
</section>

<div class="tabs">
 <button class="tab active" onclick="showScene('energy',this)">
   <div class="n">01</div><strong>ENERGY</strong><span>Solar · geothermal · mechanisms</span>
 </button>
 <button class="tab" onclick="showScene('food',this)">
   <div class="n">02</div><strong>FOOD</strong><span>Handling · sorting · automation</span>
 </button>
 <button class="tab" onclick="showScene('industry',this)">
   <div class="n">03</div><strong>INDUSTRY</strong><span>Special machines · motion · tooling</span>
 </button>
 <button class="tab" onclick="showScene('aicad',this)">
   <div class="n">04</div><strong>AI + CAD</strong><span>Simple geometry · intelligent assembly</span>
 </button>
</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.min.js"></script>
<script>
let cadStarted=false;
function initCad(){
 if(cadStarted || typeof THREE==="undefined") return;
 cadStarted=true;
 const host=document.getElementById("cad3d");
 const scene=new THREE.Scene();
 const camera=new THREE.PerspectiveCamera(40, host.clientWidth/host.clientHeight, 1, 5000);
 camera.position.set(420,330,300);
 const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});
 renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
 renderer.setSize(host.clientWidth,host.clientHeight);
 renderer.setClearColor(0x000000,0);
 host.appendChild(renderer.domElement);

 const group=new THREE.Group();
 scene.add(group);
 const geo=new THREE.BoxGeometry(240,150,100);
 const mat=new THREE.MeshPhongMaterial({color:0x78aeb8,transparent:true,opacity:.78,shininess:25});
 const block=new THREE.Mesh(geo,mat);
 group.add(block);
 const edges=new THREE.LineSegments(
   new THREE.EdgesGeometry(geo),
   new THREE.LineBasicMaterial({color:0x244b53})
 );
 group.add(edges);

 const grid=new THREE.GridHelper(600,12,0x9caaa7,0xd7ded9);
 grid.position.y=-85;
 scene.add(grid);
 scene.add(new THREE.HemisphereLight(0xffffff,0x8aa0a0,2.2));
 const dl=new THREE.DirectionalLight(0xffffff,2.4); dl.position.set(300,400,500); scene.add(dl);

 let dragging=false, px=0, py=0;
 renderer.domElement.addEventListener("pointerdown",e=>{dragging=true;px=e.clientX;py=e.clientY;renderer.domElement.setPointerCapture(e.pointerId)});
 renderer.domElement.addEventListener("pointerup",()=>dragging=false);
 renderer.domElement.addEventListener("pointermove",e=>{
   if(!dragging)return;
   group.rotation.y+=(e.clientX-px)*.012;
   group.rotation.x+=(e.clientY-py)*.012;
   px=e.clientX;py=e.clientY;
 });
 renderer.domElement.addEventListener("wheel",e=>{
   e.preventDefault();
   camera.position.multiplyScalar(e.deltaY>0?1.08:.92);
 },{passive:false});

 function resize(){
   const w=host.clientWidth,h=host.clientHeight;
   if(w&&h){camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h);}
 }
 window.addEventListener("resize",resize);
 function animate(){requestAnimationFrame(animate);renderer.render(scene,camera)}
 animate();
}

const data={
 energy:{
  kicker:"ENERGY / CONCEPT 01",
  headline:"Mechanical ideas.<br>Developed into reality.",
  lead:"A solar tracking concept where the panel follows the sun through a simple mechanical rotation. The animation shows the principle — not a completed SIMGROVA project."
 },
 food:{
  kicker:"FOOD / CONCEPT 02",
  headline:"Move it.<br>Position it. Improve it.",
  lead:"A simple product-handling concept: products travel on a conveyor while a mechanical arm picks, positions or sorts them. A recognisable principle ready to be developed further."
 },
 industry:{
  kicker:"INDUSTRY / CONCEPT 03",
  headline:"Make the movement<br>work simply.",
  lead:"A special-machine concept combining rotary and linear motion with tooling around a workpiece. The purpose is to make the mechanical idea understandable before details take over."
 },
 aicad:{
  kicker:"AI + CAD / R&D CONCEPT 04",
  headline:"Simple geometry.<br>Engineering intelligence.",
  lead:"An experimental SIMGROVA approach: describe components by their key specifications, simplified 3D envelopes and mounting interfaces — then let AI reason about how a machine can be assembled."
 }
};
function showScene(id,btn){
 document.querySelectorAll('.scene').forEach(x=>x.classList.remove('active'));
 document.getElementById(id).classList.add('active');
 document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
 btn.classList.add('active');
 document.getElementById('kicker').innerHTML=data[id].kicker;
 document.getElementById('headline').innerHTML=data[id].headline;
 document.getElementById('lead').innerHTML=data[id].lead;
 if(id==='aicad') setTimeout(initCad,60);
}
</script>
</body>
</html>
"""

components.html(page, height=760, scrolling=False)

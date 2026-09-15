import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SIMGROVA | Mechanical Engineering",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------------------------------------------------------
# SIMGROVA — first clean-sheet web prototype
# No APB logic, login, portfolio code or external image assets.
# -----------------------------------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

:root{
    --bg:#07090b;
    --panel:#0d1115;
    --line:rgba(173,205,215,.18);
    --text:#eef4f5;
    --muted:#8e9da2;
    --accent:#b9e7ef;
}

html, body, [data-testid="stAppViewContainer"], .stApp {
    background:var(--bg);
    color:var(--text);
}
[data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer {
    visibility:hidden;
}
.block-container{
    max-width:100% !important;
    padding:0 !important;
}
div[data-testid="stVerticalBlock"]{gap:0 !important;}
.simgrova-section{
    max-width:1220px;
    margin:auto;
    padding:92px 48px;
}
.kicker{
    font-family:'Space Mono',monospace;
    color:var(--accent);
    font-size:12px;
    letter-spacing:.18em;
    text-transform:uppercase;
}
h2.sg{
    font-family:'Inter',sans-serif;
    font-size:clamp(34px,5vw,68px);
    line-height:1.02;
    font-weight:300;
    letter-spacing:-.045em;
    margin:14px 0 28px;
}
.sg-copy{
    color:#a9b5b8;
    font:300 18px/1.75 'Inter',sans-serif;
    max-width:720px;
}
.sg-grid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:1px;
    background:var(--line);
    border:1px solid var(--line);
    margin-top:54px;
}
.sg-card{
    background:var(--bg);
    padding:34px;
    min-height:210px;
}
.sg-num{
    font:400 11px 'Space Mono',monospace;
    color:#647278;
    letter-spacing:.15em;
}
.sg-card h3{
    font:400 20px 'Inter',sans-serif;
    margin:38px 0 12px;
    color:#edf3f4;
}
.sg-card p{
    color:#849297;
    font:300 14px/1.7 'Inter',sans-serif;
}
.process{
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-top:62px;
    border-top:1px solid var(--line);
    border-bottom:1px solid var(--line);
    padding:24px 0;
    font:400 11px 'Space Mono',monospace;
    color:#9ba9ad;
    letter-spacing:.08em;
}
.arrow{color:#405056;}
.contact{
    border-top:1px solid var(--line);
    text-align:center;
    padding:110px 30px 130px;
}
.contact .mail{
    font:300 clamp(28px,5vw,62px) 'Inter',sans-serif;
    color:#eef4f5;
    margin-top:18px;
}
@media(max-width:800px){
    .simgrova-section{padding:70px 24px}
    .sg-grid{grid-template-columns:1fr}
    .process{display:grid;grid-template-columns:1fr 20px 1fr;gap:14px}
}
</style>
""", unsafe_allow_html=True)

hero = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box} html,body{margin:0;background:#07090b;overflow:hidden}
.hero{
  height:760px;position:relative;background:
  radial-gradient(circle at 70% 45%,rgba(107,157,168,.08),transparent 29%),
  linear-gradient(#07090b,#090c0f);
  color:#eef4f5;font-family:Arial,sans-serif;
}
.grid{
 position:absolute;inset:0;opacity:.15;
 background-image:linear-gradient(rgba(170,210,220,.13) 1px,transparent 1px),
 linear-gradient(90deg,rgba(170,210,220,.13) 1px,transparent 1px);
 background-size:54px 54px;
 mask-image:linear-gradient(to right,transparent 0,#000 35%,#000 100%);
}
.top{position:absolute;left:6%;right:6%;top:34px;display:flex;justify-content:space-between;
font:11px monospace;letter-spacing:.18em;color:#819096}
.brand{color:#dce9eb;font-weight:bold}
.copy{position:absolute;left:7%;top:210px;z-index:5}
.eyebrow{font:11px monospace;letter-spacing:.24em;color:#a7d6de;margin-bottom:22px}
h1{font-size:clamp(62px,9vw,132px);font-weight:300;line-height:.82;letter-spacing:-.07em;margin:0}
.sub{font-size:clamp(18px,2vw,27px);font-weight:300;color:#8f9da1;margin-top:30px;letter-spacing:.01em}
.motto{font:11px monospace;letter-spacing:.18em;color:#607076;margin-top:62px}
.machine{position:absolute;right:3%;top:80px;width:52%;height:620px}
.machine svg{width:100%;height:100%}
.ring1{transform-origin:410px 300px;animation:spin 28s linear infinite}
.ring2{transform-origin:410px 300px;animation:spin2 18s linear infinite}
.arm{transform-origin:410px 300px;animation:sweep 7s ease-in-out infinite alternate}
.pulse{animation:pulse 2.6s ease-in-out infinite}
.scan{animation:scan 6s ease-in-out infinite}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes spin2{to{transform:rotate(-360deg)}}
@keyframes sweep{from{transform:rotate(-13deg)}to{transform:rotate(17deg)}}
@keyframes pulse{50%{opacity:.25}}
@keyframes scan{0%,100%{transform:translateY(-80px);opacity:0}20%,80%{opacity:.5}50%{transform:translateY(410px)}}
.bottom{position:absolute;left:7%;right:7%;bottom:34px;border-top:1px solid rgba(180,215,220,.15);
padding-top:15px;display:flex;justify-content:space-between;font:10px monospace;letter-spacing:.12em;color:#526167}
</style>
</head>
<body>
<div class="hero">
 <div class="grid"></div>
 <div class="top"><span class="brand">SIMGROVA / ENGINEERING</span><span>SKANDERBORG · DENMARK</span></div>
 <div class="copy">
   <div class="eyebrow">MECHANICAL ENGINEERING / DEVELOPMENT</div>
   <h1>SIMGROVA</h1>
   <div class="sub">From idea to production.</div>
   <div class="motto">SIMPLICITY CREATES GROWTH</div>
 </div>
 <div class="machine">
 <svg viewBox="0 0 700 600" fill="none">
   <g stroke="#9bc5cd" stroke-width="1" opacity=".18">
    <path d="M40 300H660M410 25V575"/><path d="M110 85L625 510M120 520L620 70"/>
   </g>
   <g class="ring1" stroke="#b6dce3" opacity=".45">
    <circle cx="410" cy="300" r="188"/><circle cx="410" cy="300" r="172" stroke-dasharray="2 17"/>
    <path d="M410 98v30M410 472v30M208 300h30M582 300h30"/>
   </g>
   <g class="ring2" stroke="#8ebbc4" opacity=".33">
    <circle cx="410" cy="300" r="122" stroke-dasharray="65 14 5 14"/>
    <circle cx="410" cy="300" r="96"/>
   </g>
   <g class="arm">
    <path d="M410 300L555 215" stroke="#d5eef2" stroke-width="2"/>
    <circle cx="555" cy="215" r="18" stroke="#d5eef2"/>
    <circle cx="555" cy="215" r="4" fill="#d5eef2"/>
   </g>
   <circle cx="410" cy="300" r="42" stroke="#d5eef2" stroke-width="2"/>
   <circle class="pulse" cx="410" cy="300" r="8" fill="#d5eef2"/>
   <g stroke="#8fb7bf" opacity=".35">
    <path d="M260 505h300M260 498v14M560 498v14"/>
    <path d="M280 520h260"/><path d="M280 515v10M540 515v10"/>
   </g>
   <g fill="#81999e" font-family="monospace" font-size="10">
    <text x="360" y="535">Ø 376.00 / REF</text><text x="575" y="210">P-04</text>
    <text x="420" y="286">AXIS 01</text>
   </g>
   <line class="scan" x1="155" y1="130" x2="650" y2="130" stroke="#c5edf4" opacity=".4"/>
 </svg>
 </div>
 <div class="bottom"><span>CONCEPT / DESIGN / ANALYSIS / REALISATION</span><span>01 — 04</span></div>
</div>
</body>
</html>
"""
components.html(hero, height=760, scrolling=False)

st.markdown("""
<div class="simgrova-section">
  <div class="kicker">01 / Engineering</div>
  <h2 class="sg">Complex engineering.<br>Made simple.</h2>
  <div class="sg-copy">
    SIMGROVA develops mechanical solutions from the first idea to a production-ready result.
    The focus is on projects where mechanics, development, calculation and practical
    implementation have to work as one system.
  </div>

  <div class="sg-grid">
    <div class="sg-card"><div class="sg-num">01.01</div><h3>Concept development</h3><p>Turning requirements and ideas into robust mechanical concepts that can actually be built.</p></div>
    <div class="sg-card"><div class="sg-num">01.02</div><h3>Mechanical design</h3><p>Construction, dimensioning and detailed engineering with focus on function, simplicity and production.</p></div>
    <div class="sg-card"><div class="sg-num">01.03</div><h3>Multidisciplinary projects</h3><p>Mechanical development coordinated across interfaces, suppliers, manufacturing and commissioning.</p></div>
  </div>
</div>

<div class="simgrova-section">
  <div class="kicker">02 / Process</div>
  <h2 class="sg">From sketch<br>to working machine.</h2>
  <div class="process">
    <span>IDEA</span><span class="arrow">→</span><span>CONCEPT</span><span class="arrow">→</span>
    <span>ENGINEERING</span><span class="arrow">→</span><span>ANALYSIS</span><span class="arrow">→</span>
    <span>PROTOTYPE</span><span class="arrow">→</span><span>PRODUCTION</span>
  </div>
</div>

<div class="simgrova-section">
  <div class="kicker">03 / Capability</div>
  <h2 class="sg">One engineering partner.<br>Across the development chain.</h2>
  <div class="sg-grid">
    <div class="sg-card"><div class="sg-num">A</div><h3>Product & machine development</h3><p>Mechanical systems, tools, special machines and equipment from concept through detailed design.</p></div>
    <div class="sg-card"><div class="sg-num">B</div><h3>Calculation & optimisation</h3><p>Dimensioning, structural assessment and engineering optimisation supporting sound design decisions.</p></div>
    <div class="sg-card"><div class="sg-num">C</div><h3>Project execution</h3><p>Technical project management, supplier coordination, risk assessment, CE and commissioning.</p></div>
  </div>
</div>

<div class="contact">
  <div class="kicker">04 / Start a project</div>
  <div class="mail">Have a mechanical challenge?</div>
  <div class="sg-copy" style="margin:24px auto 0">Bring the idea. SIMGROVA can help turn it into a practical engineering solution.</div>
</div>
""", unsafe_allow_html=True)

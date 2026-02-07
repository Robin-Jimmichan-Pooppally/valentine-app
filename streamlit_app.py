import streamlit as st
import time
import random
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="❤️", layout="wide")

NAME = st.secrets.get("NAME", "You")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "finale" not in st.session_state:
    st.session_state.finale = False

# ---------------- STYLES + JS ----------------
st.markdown("""
<style>
html, body {
    height: 100%;
    background: radial-gradient(circle at top, #1a1a1a, #000);
    color: white;
    overflow-x: hidden;
    animation: heartbeat 3s infinite;
}

@keyframes heartbeat {
    0% { background-size: 100% 100%; }
    50% { background-size: 104% 104%; }
    100% { background-size: 100% 100%; }
}

.text {
    text-align: center;
    font-size: 22px;
    line-height: 1.9;
    max-width: 900px;
    margin: 120px auto 40px;
    animation: fadeUp 1.2s ease forwards;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.buttons {
    position: relative;
    height: 200px;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 60px;
}

button {
    font-size: 20px;
    padding: 14px 36px;
    border-radius: 30px;
    border: none;
    cursor: pointer;
}

#yes {
    background: #ff4d6d;
    color: white;
}

#no {
    background: #444;
    color: white;
    position: absolute;
}

#fadeBlack {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: black;
    opacity: 0;
    pointer-events: none;
    transition: opacity 3s ease;
    z-index: 9999;
}

#fadeBlack.show {
    opacity: 1;
}

svg {
    position: fixed;
    top: 0;
    left: 0;
    pointer-events: none;
    z-index: 9998;
}
</style>

<script>
function moveNo(btn){
    const x = Math.random() * (window.innerWidth - 150);
    const y = Math.random() * (window.innerHeight - 150);
    btn.style.left = x + "px";
    btn.style.top = y + "px";
}

function heartFireworks(){
    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", window.innerWidth);
    svg.setAttribute("height", window.innerHeight);

    for(let i=0;i<40;i++){
        const heart = document.createElementNS("http://www.w3.org/2000/svg", "path");
        heart.setAttribute("d","M10 30 A20 20 0 0 1 50 30 Q50 60 10 90 Q-30 60 -30 30 A20 20 0 0 1 10 30 Z");
        heart.setAttribute("fill","pink");

        const x = Math.random() * window.innerWidth;
        const y = window.innerHeight;
        const scale = Math.random() * 0.6 + 0.4;

        heart.setAttribute("transform", `translate(${x},${y}) scale(${scale})`);

        svg.appendChild(heart);

        heart.animate([
            { transform: `translate(${x}px,${y}px) scale(${scale})`, opacity: 1 },
            { transform: `translate(${x + (Math.random()*200-100)}px,${y-600}px) scale(${scale})`, opacity: 0 }
        ], {
            duration: 2500,
            easing: "ease-out"
        });
    }

    document.body.appendChild(svg);
    setTimeout(()=>svg.remove(),3000);
}

function finale(){
    heartFireworks();
    document.getElementById("fadeBlack").classList.add("show");
}
</script>

<div id="fadeBlack"></div>
""", unsafe_allow_html=True)

# ---------------- TYPEWRITER ----------------
def typewriter(text):
    placeholder = st.empty()
    shown = ""
    for c in text:
        shown += c
        placeholder.markdown(f"<div class='text'>{shown}</div>", unsafe_allow_html=True)
        time.sleep(0.03)

# ---------------- STORY ----------------
story = [
    f"{NAME}, before you scroll away… 💖",
    "I know we had a lot of fights.",
    "I know I was never a perfect boyfriend.",
    "There were moments I didn’t understand you the way I should have.",
    "Moments where my silence hurt more than words.",
    "But through every argument, every misunderstanding…",
    "One thing never changed.",
    "I loved you.",
    "Not the easy kind of love.",
    "But the kind that stays.",
    "Even when things get messy, confusing, or difficult.",
    "I don’t promise perfection.",
    "I promise effort.",
    "Effort to listen more.",
    "To understand you deeper.",
    "To grow — not just for myself, but for us.",
    "If love is choosing someone again and again…",
    "Then my heart has always chosen you. ❤️"
]

# ---------------- FLOW ----------------
if st.session_state.step < len(story):
    typewriter(story[st.session_state.step])

    if st.button("Continue 💫"):
        st.session_state.step += 1
        st.rerun()

else:
    st.markdown("""
    <div class="text">
        Will you be my Valentine? 💘
    </div>

    <div class="buttons">
        <button id="yes" onclick="finale()">YES 💖</button>
        <button id="no" onmouseover="moveNo(this)">NO 🙃</button>
    </div>
    """, unsafe_allow_html=True)

    if st.button("I clicked YES 💕"):
        st.balloons()

# ---------------- COUNTDOWN ----------------
val_day = datetime(datetime.now().year, 2, 14)
days = (val_day - datetime.now()).days

st.markdown(f"""
<div style="text-align:center; margin-top:60px; opacity:0.8;">
⏳ {days} days until Valentine’s Day 💞
</div>
""", unsafe_allow_html=True)

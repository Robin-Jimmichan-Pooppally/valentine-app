import streamlit as st
import streamlit.components.v1 as components
import time
import base64
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="❤️", layout="wide")

NAME = st.secrets.get("NAME", "You")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "accepted" not in st.session_state:
    st.session_state.accepted = False

# CHECK IF YES WAS CLICKED - FIXED VERSION
query_params = st.query_params.to_dict()
if "yes" in query_params:
    st.session_state.accepted = True

# ---------------- TYPEWRITER ----------------
def typewriter(text):
    placeholder = st.empty()
    shown = ""
    for c in text:
        shown += c
        placeholder.markdown(f"<div class='text'>{shown}</div>", unsafe_allow_html=True)
        time.sleep(0.02)

# ---------------- STORY ----------------
story = [
    f"{NAME}, before you scroll away… 💖",
    "May 5th — that's when things changed between us.",
    "June 7th — that's when we became *us*.",
    "Then life happened.",
    "I had to leave for Kerala… for six long months.",
    "And you waited.",
    "You really waited for me.",
    "Every hug when I came back felt like home.",
    "Every cuddle reminded me I was safe.",
    "You made me happier than I ever expected.",
    "Thank you for always being there.",
    "Thank you for loving me on my worst days.",
    "Thank you for seeing the best in me, even when I couldn't see it myself.",
    "I know we had a lot of fights.",
    "I know I was never a perfect boyfriend.",
    "There were moments I didn't understand you the way I should have.",
    "Moments where my silence hurt more than words.",
    "Times where I wish I could go back and do things better.",
    "But through every argument…",
    "Every misunderstanding…",
    "One thing never changed — I loved you.",
    "Not the easy kind of love.",
    "But the kind that stays.",
    "Even when things get messy, confusing, or difficult.",
    "Thank you for never giving up on us.",
    "Thank you for your patience, your kindness, your heart.",
    "You've given me more than I ever deserved.",
    "I don't want to promise perfection.",
    "I want to promise effort.",
    "Effort to listen more.",
    "To understand you deeper.",
    "To grow — not just for myself, but for us.",
    "If love is choosing someone again and again…",
    "Then my heart has always chosen you. 💗",
    "Thank you for choosing me too.",
]

# ---------------- STYLES ----------------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background: radial-gradient(circle at top, #1a1a1a, #000) !important;
    color: white;
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
</style>
""", unsafe_allow_html=True)

# ---------------- BACKGROUND MUSIC ----------------
try:
    # Read and encode the audio file
    audio_file = open('song.mp3', 'rb')
    audio_bytes = audio_file.read()
    audio_base64 = base64.b64encode(audio_bytes).decode()
    
    # Hidden autoplay audio
    st.markdown(f"""
    <audio autoplay loop style="display:none">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>
    """, unsafe_allow_html=True)
except:
    pass  # If music file not found, just continue without it

# ---------------- FLOW ----------------
if not st.session_state.accepted and st.session_state.step < len(story):
    typewriter(story[st.session_state.step])

    if st.button("Continue 💫"):
        st.session_state.step += 1
        st.rerun()

elif not st.session_state.accepted:
    st.markdown("""
    <div class="text">
        Will you be my Valentine? 💘
    </div>
    """, unsafe_allow_html=True)
    
    # Use components.html for interactive buttons with JavaScript
    components.html("""
    <style>
    body {
        margin: 0;
        background: transparent;
        overflow: hidden;
    }
    
    .buttons {
        position: relative;
        height: 200px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 80px;
    }

    button {
        font-size: 20px;
        padding: 14px 36px;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        font-weight: bold;
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

    <div id="fadeBlack"></div>
    
    <div class="buttons">
        <button id="yes" onclick="finale()">YES 💖</button>
        <button id="no" onmouseover="moveNo(this)">NO 🙃</button>
    </div>

    <script>
    function moveNo(btn){
        const x = Math.random() * (window.innerWidth - 150);
        const y = Math.random() * (window.innerHeight - 100);
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
        setTimeout(() => {
            window.parent.location.href = window.parent.location.origin + window.parent.location.pathname + "?yes=1";
        }, 1500);
    }
    </script>
    """, height=300)

else:
    # THIS IS THE MESSAGE AFTER SHE SAYS YES
    st.balloons()
    st.markdown(f"""
    <div class="text">
        💖 You're officially my Valentine 💖<br><br>
        
        Thank you for saying yes, {NAME}.<br>
        Thank you for being mine.<br>
        Thank you for being you.<br><br>
        
        I promise to love you better every day.<br>
        I promise to make you smile more than I make you cry.<br>
        I promise to always choose you.<br><br>
        
        I love you. Today, tomorrow, always. ❤️
    </div>
    """, unsafe_allow_html=True)

# ---------------- COUNTDOWN ----------------
val_day = datetime(datetime.now().year, 2, 14)
days = (val_day - datetime.now()).days

st.markdown(f"""
<div style="text-align:center; margin-top:60px; opacity:0.8;">
⏳ {days} days until Valentine's Day 💞
</div>
""", unsafe_allow_html=True)

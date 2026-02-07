# streamlit_app.py
# Ultra-Polished Valentine Experience 💖🎆🎵
# Includes: smooth music fade-in + heart-shaped fireworks

import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="One Question 💘", layout="centered")

# ---------- SECRETS ----------
NAME = st.secrets.get("NAME", "Someone Special")

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------- STYLES ----------
st.markdown("""
<style>
body {
  background: radial-gradient(circle at top, #1a1a2e, #000);
}
.big { font-size: 36px; font-weight: 700; text-align: center; color: white; }
.text { font-size: 20px; text-align: center; color: #ddd; }
.name {
  font-size: 46px; font-weight: 800; text-align: center; color: #ff4d6d;
  animation: glow 2s infinite alternate;
}
.card {
  background: rgba(255,255,255,0.08);
  border-radius: 22px;
  padding: 30px;
  margin-top: 25px;
}
@keyframes glow {
  from { text-shadow: 0 0 10px #ff4d6d; }
  to { text-shadow: 0 0 30px #ff85a1; }
}
</style>
""", unsafe_allow_html=True)

# ---------- COUNTDOWN ----------
now = datetime.now()
valentine = datetime(now.year, 2, 14)
if now > valentine:
    valentine = datetime(now.year + 1, 2, 14)
remaining = valentine - now

# ---------- FLOW ----------

# ACT 1
if st.session_state.step == 1:
    st.markdown('<div class="big">Hey… I need a moment of your time ✨</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">This isn’t random. It’s intentional.</div>', unsafe_allow_html=True)
    if st.button("Continue"):
        st.session_state.step = 2

# ACT 2
elif st.session_state.step == 2:
    for line in [
        "Some people make ordinary days feel different.",
        "Some moments deserve courage.",
        "This… is one of them."
    ]:
        st.markdown(f'<div class="text">{line}</div>', unsafe_allow_html=True)
        time.sleep(0.8)
    if st.button("I’m listening"):
        st.session_state.step = 3

# ACT 3
elif st.session_state.step == 3:
    st.markdown('<div class="text">This question is only for…</div>', unsafe_allow_html=True)
    time.sleep(0.6)
    st.markdown(f'<div class="name">{NAME} 💖</div>', unsafe_allow_html=True)
    if st.button("Okay…"):
        st.session_state.step = 4

# ACT 4
elif st.session_state.step == 4:
    st.markdown('<div class="big">Will you be my Valentine? 💘</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">No pressure. Just honesty.</div>', unsafe_allow_html=True)
    if st.button("Yes 💖"):
        st.session_state.step = 5

# ACT 5 — Heart Fireworks + Smooth Music Fade-in
elif st.session_state.step == 5:
    st.markdown('<div class="big">You just created a memory ✨</div>', unsafe_allow_html=True)

    st.components.v1.html(
        """
        <audio id="bgm" src="love.mp3"></audio>
        <canvas id="c"></canvas>
        <script>
        const audio = document.getElementById('bgm');
        audio.volume = 0;
        audio.play();
        let v = 0;
        const fade = setInterval(() => {
          if (v < 0.6) { v += 0.02; audio.volume = v; }
          else clearInterval(fade);
        }, 200);

        const canvas = document.getElementById('c');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        let particles = [];
        function heart(t) {
          return {
            x: 16 * Math.pow(Math.sin(t), 3),
            y: -(13 * Math.cos(t) - 5 * Math.cos(2*t) - 2 * Math.cos(3*t) - Math.cos(4*t))
          }
        }

        for (let i = 0; i < 300; i++) {
          let t = Math.random() * Math.PI * 2;
          let h = heart(t);
          particles.push({
            x: canvas.width/2 + h.x * 15,
            y: canvas.height/2 + h.y * 15,
            r: Math.random() * 2 + 1
          });
        }

        function draw() {
          ctx.clearRect(0,0,canvas.width,canvas.height);
          ctx.fillStyle = '#ff4d6d';
          particles.forEach(p => {
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
            ctx.fill();
          });
          requestAnimationFrame(draw);
        }
        draw();
        </script>
        """,
        height=500
    )

    st.session_state.step = 6

# ACT 6 — Final card
elif st.session_state.step == 6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<div class="big">{NAME}, it’s a date 💖</div>', unsafe_allow_html=True)
    st.markdown('<div class="text">Coffee ☕ • Long walk 🚶‍♂️🚶‍♀️ • No rush</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="text">Countdown to Valentine’s Day:</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="big">{remaining.days} days {remaining.seconds//3600} hours</div>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<div class="text">Screenshot this moment 💌</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

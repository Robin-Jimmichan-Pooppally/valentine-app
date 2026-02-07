import streamlit as st
import streamlit.components.v1 as components
import time
from datetime import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="❤️", layout="wide")

NAME = st.secrets.get("NAME", "You")

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ---------------- FAST TYPEWRITER ----------------
def typewriter(text):
    if not text or text.strip() == "":  # Empty line - just show it
        st.markdown(f"<div class='text'><br></div>", unsafe_allow_html=True)
        return
    
    placeholder = st.empty()
    shown = ""
    for c in text:
        shown += c
        placeholder.markdown(f"<div class='text'>{shown}</div>", unsafe_allow_html=True)
        time.sleep(0.03)  # Fast typing effect

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

.stButton > button {
    background: #ff4d6d !important;
    color: white !important;
    font-size: 20px !important;
    padding: 14px 36px !important;
    border-radius: 30px !important;
    border: none !important;
    font-weight: bold !important;
}

.stButton > button:hover {
    background: #ff6b9d !important;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- BACKGROUND MUSIC ----------------
# Centered compact player at top
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("<div style='text-align: center; font-size: 14px; color: #ff6b9d; margin-top: 10px;'>🎵 A Thousand Years - Christina Perri</div>", unsafe_allow_html=True)
    
    try:
        audio_file = open('song.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')
    except:
        try:
            audio_file = open('Christina Perri - A Thousand Years [Official Music Video].mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/mp3')
        except:
            pass

st.markdown("<hr style='border: 1px solid #333; margin: 20px 0;'>", unsafe_allow_html=True)

# ---------------- FLOW ----------------
if not st.session_state.accepted and st.session_state.step < len(story):
    typewriter(story[st.session_state.step])

    if st.button("Continue 💫", key=f"continue_{st.session_state.step}"):
        st.session_state.step += 1
        st.rerun()

elif not st.session_state.accepted:
    st.markdown("""
    <div class="text">
        Will you be my Valentine? 💘
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # YES button
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col2:
        if st.button("YES 💖", key="yes_main", use_container_width=True):
            st.session_state.accepted = True
            st.balloons()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # NO button
    components.html("""
    <style>
    body {
        margin: 0;
        background: transparent;
        overflow: hidden;
    }

    #noBtn {
        font-size: 20px;
        padding: 14px 36px;
        border-radius: 30px;
        border: none;
        cursor: pointer;
        font-weight: bold;
        background: #444;
        color: white;
        position: absolute;
        left: 50%;
        top: 20px;
        transform: translateX(-50%);
        transition: all 0.3s;
    }
    </style>

    <button id="noBtn" onmouseover="moveNo(this)">NO 🙃</button>

    <script>
    function moveNo(btn){
        const x = Math.random() * (window.innerWidth - 150);
        const y = Math.random() * (window.innerHeight - 80);
        btn.style.left = x + "px";
        btn.style.top = y + "px";
        btn.style.transform = "none";
    }
    </script>
    """, height=150)

else:
    # Message after YES - PROPERLY FIXED!
    st.balloons()
    
    # Build the HTML properly
    message_html = f"""
    <div class="text" style="margin-top: 80px;">
        💖 You're officially my Valentine 💖
    </div>
    <div class="text" style="margin-top: 40px; font-size: 20px;">
        Thank you for saying yes, {NAME}.<br>
        Thank you for being mine.<br>
        Thank you for being you.
    </div>
    <div class="text" style="margin-top: 30px; font-size: 20px;">
        I promise to love you better every day.<br>
        I promise to make you smile more than I make you cry.<br>
        I promise to always choose you.
    </div>
    <div class="text" style="margin-top: 30px; font-size: 20px;">
        I love you. Today, tomorrow, always. ❤️
    </div>
    """
    
    st.markdown(message_html, unsafe_allow_html=True)

# ---------------- COUNTDOWN ----------------
val_day = datetime(datetime.now().year, 2, 14)
days = (val_day - datetime.now()).days

st.markdown(f"""
<div style="text-align:center; margin-top:60px; opacity:0.8;">
⏳ {days} days until Valentine's Day 💞
</div>
""", unsafe_allow_html=True)

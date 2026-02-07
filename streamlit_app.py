import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="❤️", layout="wide")

# ----------------- SECRETS -----------------
NAME = st.secrets.get("NAME", "You")

# ----------------- SESSION STATE -----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "no_x" not in st.session_state:
    st.session_state.no_x = 200
    st.session_state.no_y = 40

# ----------------- STYLES -----------------
st.markdown(
    f"""
    <style>
    body {{
        background: radial-gradient(circle at top, #1b1b1b, #000);
        color: white;
        animation: heartbeat 3s infinite;
    }}

    @keyframes heartbeat {{
        0% {{ background-size: 100% 100%; }}
        50% {{ background-size: 104% 104%; }}
        100% {{ background-size: 100% 100%; }}
    }}

    .fade {{
        animation: fadeUp 1.2s ease forwards;
    }}

    @keyframes fadeUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .text {{
        text-align: center;
        font-size: 22px;
        line-height: 1.9;
        max-width: 900px;
        margin: 120px auto 40px;
    }}

    .buttons {{
        display: flex;
        justify-content: center;
        gap: 40px;
        position: relative;
        height: 140px;
    }}

    button {{
        font-size: 20px;
        padding: 14px 36px;
        border-radius: 30px;
        border: none;
        cursor: pointer;
    }}

    #yes {{
        background: #ff4d6d;
        color: white;
    }}

    #no {{
        background: #444;
        color: white;
        position: absolute;
        left: {st.session_state.no_x}px;
        top: {st.session_state.no_y}px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------- TYPEWRITER -----------------
def typewriter(text):
    placeholder = st.empty()
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(f"<div class='text fade'>{displayed}</div>", unsafe_allow_html=True)
        time.sleep(0.03)

# ----------------- CONTENT -----------------
paragraphs = [
    f"{NAME}, before you scroll away… 💖",

    "I know we had a lot of fights.",

    "I know I was never a perfect boyfriend.",

    "There were moments I didn’t understand you the way I should have.",

    "Moments where my silence hurt more than words.",

    "But through every argument, every misunderstanding… one thing never changed.",

    "I loved you.",

    "Not the easy kind of love.",

    "The kind that stays even when things get messy, confusing, or difficult.",

    "I don’t promise perfection.",

    "I promise effort.",

    "Effort to listen more. To understand you deeper.",

    "To grow — not just for myself… but for us.",

    "If love is choosing someone again and again…",

    "Then my heart has always chosen you. ❤️"
]

# ----------------- DISPLAY -----------------
if st.session_state.step < len(paragraphs):
    typewriter(paragraphs[st.session_state.step])

    if st.button("Continue 💫"):
        st.session_state.step += 1
        st.rerun()

else:
    st.markdown(
        """
        <div class="text fade">
        Will you be my Valentine? 💘
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💖"):
            st.balloons()
            st.markdown("## ❤️💥❤️💥❤️")
            st.markdown("### You just made my heart explode 💖")

    with col2:
        if st.button("NO 🙃"):
            st.session_state.no_x = random.randint(50, 400)
            st.session_state.no_y = random.randint(10, 90)
            st.rerun()

# ----------------- COUNTDOWN -----------------
valentine = datetime(datetime.now().year, 2, 14)
days = (valentine - datetime.now()).days

st.markdown(
    f"""
    <div style="text-align:center; margin-top:60px; opacity:0.8;">
        ⏳ {days} days until Valentine’s Day 💕
    </div>
    """,
    unsafe_allow_html=True
)

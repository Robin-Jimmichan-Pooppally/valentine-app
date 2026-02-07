import streamlit as st
import random
import time
import datetime

# ---------------- CONFIG ----------------
st.set_page_config(page_title="💖 Valentine 💖", layout="wide")

NAME = st.secrets["NAME"]

# ---------------- SESSION STATE ----------------
if "story_index" not in st.session_state:
    st.session_state.story_index = 0

if "finished" not in st.session_state:
    st.session_state.finished = False

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "no_x" not in st.session_state:
    st.session_state.no_x = random.randint(-200, 200)

if "no_y" not in st.session_state:
    st.session_state.no_y = random.randint(-80, 80)

# ---------------- STORY ----------------
story = [
    f"{NAME}, before you scroll away… 💖",
    "There’s something I’ve been meaning to ask.",
    "",
    "May 5th — that’s when things changed between us.",
    "June 7th — that’s when we became *us*.",
    "",
    "Then life happened.",
    "I had to leave for Kerala… for six long months.",
    "And you waited.",
    "You really waited for me.",
    "",
    "Every hug when I came back felt like home.",
    "Every cuddle reminded me I was safe.",
    "You made me happier than I ever expected.",
    "",
    "I know we had a lot of fights.",
    "I know I was never a perfect boyfriend.",
    "There were moments I didn’t understand you the way I should have.",
    "Moments where my silence hurt more than words.",
    "Times where I wish I could go back and do things better.",
    "",
    "But through every argument…",
    "Every misunderstanding…",
    "One thing never changed — I loved you.",
    "",
    "Not the easy kind of love.",
    "But the kind that stays.",
    "Even when things get messy, confusing, or difficult.",
    "",
    "I don’t want to promise perfection.",
    "I want to promise effort.",
    "Effort to listen more.",
    "To understand you deeper.",
    "To grow — not just for myself, but for us.",
    "",
    "If love is choosing someone again and again…",
    "Then my heart has always chosen you. 💗",
]

# ---------------- HELPERS ----------------
def valentine_countdown():
    now = datetime.datetime.now()
    year = now.year
    target = datetime.datetime(year, 2, 14, 0, 0)
    if now > target:
        target = datetime.datetime(year + 1, 2, 14, 0, 0)
    delta = target - now
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, _ = divmod(rem, 60)
    return days, hours, minutes

# ---------------- STYLES ----------------
st.markdown(
    """
    <style>
    body {
        background: radial-gradient(circle at top, #1c1c1c, #000);
        color: white;
        animation: heartbeat 3s infinite;
    }

    @keyframes heartbeat {
        0% { background-size: 100% 100%; }
        50% { background-size: 105% 105%; }
        100% { background-size: 100% 100%; }
    }

    .story {
        text-align: center;
        margin-top: 100px;
        font-size: 22px;
        line-height: 1.9;
        max-width: 850px;
        margin-left: auto;
        margin-right: auto;
        animation: fadeUp 1.2s ease forwards;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(25px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .buttons {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 40px;
        position: relative;
        height: 140px;
    }

    button {
        font-size: 20px;
        padding: 12px 30px;
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
        left: %dpx;
        top: %dpx;
    }
    </style>
    """ % (st.session_state.no_x, st.session_state.no_y),
    unsafe_allow_html=True
)

# ---------------- TYPEWRITER ----------------
def typewriter(text):
    placeholder = st.empty()
    shown = ""
    for char in text:
        shown += char
        placeholder.markdown(
            f"<div class='story'>{shown}</div>",
            unsafe_allow_html=True
        )
        time.sleep(0.03)

# ---------------- STORY FLOW ----------------
if not st.session_state.finished:
    typewriter(story[st.session_state.story_index])

    st.write("")
    if st.button("Continue 💫"):
        if st.session_state.story_index < len(story) - 1:
            st.session_state.story_index += 1
            st.rerun()
        else:
            st.session_state.finished = True
            st.rerun()

elif not st.session_state.accepted:
    # ---------------- QUESTION ----------------
    st.markdown(
        """
        <div class="story">
            So here’s my question… 💖<br><br>
            <strong>Will you be my Valentine?</strong>
            <div class="buttons">
                <button id="yes">YES 💘</button>
                <button id="no">NO 🙃</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💘"):
            st.session_state.accepted = True
            st.rerun()

    with col2:
        if st.button("NO 🙃"):
            st.session_state.no_x = random.randint(-300, 300)
            st.session_state.no_y = random.randint(-120, 120)
            st.rerun()

else:
    # ---------------- FINALE ----------------
    days, hours, minutes = valentine_countdown()

    st.markdown(
        f"""
        <div class="story">
            <h1>YAY 💖</h1>
            <h2>You’re officially my Valentine 😌</h2>
            <p>⏳ {days} days, {hours} hours, {minutes} minutes to go</p>
        </div>

        <canvas id="fireworks"></canvas>

        <script>
        const canvas = document.getElementById("fireworks");
        const ctx = canvas.getContext("2d");
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        function firework() {{
            const x = Math.random() * canvas.width;
            const y = Math.random() * canvas.height / 2;
            for (let i = 0; i < 40; i++) {{
                ctx.beginPath();
                ctx.arc(x + Math.random()*80-40, y + Math.random()*80-40, 6, 0, 2*Math.PI);
                ctx.fillStyle = ["#ff4d6d","#ff9ff3","#feca57","#ff6b81"][Math.floor(Math.random()*4)];
                ctx.fill();
            }}
        }}

        setInterval(() => {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            firework();
        }}, 350);
        </script>
        """,
        unsafe_allow_html=True
    )

    # 🎶 music ready (upload later)
    # st.audio("love.mp3", loop=True)

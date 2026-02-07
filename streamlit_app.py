import streamlit as st
import datetime

st.set_page_config(page_title="For You 💖", layout="centered")

NAME = st.secrets.get("NAME", "You")

# ---------- STORY ----------
story = [
    "May 6th. I didn’t know it that day, but that was the beginning of something that would quietly change my life.",

    "Then June 7th happened — and somehow it felt natural, like the universe nudged us and said, ‘Yes, this makes sense.’",

    "Not long after that, I had to leave for Kerala for six months. Different places, different routines, different time zones… but the same feeling.",

    "You waited. And that still amazes me.",

    "Through the distance, you never made it feel heavy. You made it feel worth it.",

    "And when I finally came back — your hugs felt like home, and our cuddles felt like comfort I didn’t know I needed that much.",

    "You’ve made me laugh on days I didn’t feel like smiling, and somehow turned ordinary moments into memories.",

    # 🔥 NEW LONG DIALOGUE ADDED (WITHOUT REMOVING ANYTHING)
    """I know we had a lot of fights.
    I know I was never a perfect boyfriend.
    There were moments I didn’t understand you the way I should have,
    moments where my silence hurt more than words,
    and times where I wish I could go back and do things better.

    But through every argument, every misunderstanding,
    one thing never changed — I loved you.
    Not the easy kind of love, but the kind that stays,
    even when things get messy, confusing, or difficult.

    I don’t want to promise perfection.
    I want to promise effort.
    Effort to listen more, to understand you deeper,
    to grow — not just for myself, but for us.

    If love is choosing someone again and again,
    then my heart has always chosen you.""",

    "So this is me saying thank you — for the patience, the warmth, the happiness, and for being you."
]

# ---------- HELPERS ----------
def days_to_valentine():
    today = datetime.date.today()
    year = today.year
    target = datetime.date(year, 2, 14)
    if today > target:
        target = datetime.date(year + 1, 2, 14)
    return (target - today).days

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0

if "story_index" not in st.session_state:
    st.session_state.story_index = 0

# ---------- STEP 0 ----------
if st.session_state.step == 0:
    st.markdown(
        f"""
        <div style="text-align:center; margin-top:120px;">
            <h2>{NAME}, before you scroll away… 💖</h2>
            <p>there’s something I’ve been meaning to ask.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Continue 💫"):
        st.session_state.step = 1
        st.rerun()

# ---------- STEP 1 (STORY) ----------
elif st.session_state.step == 1:
    st.markdown(f"""
        <div style="
            text-align:center;
            margin-top:90px;
            font-size:20px;
            line-height:1.8;
            max-width:800px;
            margin-left:auto;
            margin-right:auto;
        ">
            {story[st.session_state.story_index]}
        </div>
    """, unsafe_allow_html=True)

    if st.button("Next 💖"):
        st.session_state.story_index += 1
        if st.session_state.story_index >= len(story):
            st.session_state.step = 2
            st.session_state.story_index = 0
        st.rerun()

# ---------- STEP 2 (QUESTION) ----------
elif st.session_state.step == 2:
    st.markdown(
        """
        <style>
        .container {
            display:flex;
            flex-direction:column;
            align-items:center;
            justify-content:center;
            height:65vh;
            text-align:center;
        }
        .buttons {
            position:relative;
            width:320px;
            height:140px;
            margin-top:20px;
        }
        button {
            padding:14px 34px;
            font-size:18px;
            border:none;
            border-radius:30px;
            cursor:pointer;
        }
        #yes {
            background:#ff4b6e;
            color:white;
        }
        #no {
            position:absolute;
            background:#444;
            color:white;
        }
        </style>

        <div class="container">
            <h2>So here’s my question… 💖</h2>
            <h2>Will you be my Valentine?</h2>

            <div class="buttons">
                <button id="yes">YES 💘</button>
                <button id="no">NO 🙃</button>
            </div>
        </div>

        <script>
        const noBtn = document.getElementById("no");
        const yesBtn = document.getElementById("yes");

        function moveNo() {
            const x = Math.random() * 220 - 110;
            const y = Math.random() * 90 - 45;
            noBtn.style.transform = `translate(${x}px, ${y}px)`;
        }

        noBtn.addEventListener("mouseover", moveNo);
        noBtn.addEventListener("touchstart", moveNo);
        noBtn.addEventListener("click", () => yesBtn.click());

        yesBtn.addEventListener("click", () => {
            window.location.search = "?yes=1";
        });
        </script>
        """,
        unsafe_allow_html=True
    )

    if "yes" in st.query_params:
        st.session_state.step = 3
        st.rerun()

# ---------- STEP 3 (CELEBRATION) ----------
elif st.session_state.step == 3:
    st.markdown(f"""
        <style>
        body {{
            background: radial-gradient(circle at bottom, #0b0d2b, #000);
            overflow:hidden;
        }}
        .firework {{
            position: fixed;
            width: 8px;
            height: 8px;
            border-radius: 50%;
            animation: explode 1.4s ease-out infinite;
        }}
        @keyframes explode {{
            0% {{ transform: scale(0); opacity:1; }}
            100% {{ transform: scale(18); opacity:0; }}
        }}
        </style>

        <div style="
            text-align:center;
            margin-top:120px;
            color:white;
        ">
            <h1>YAY 🎆🎆</h1>
            <h2>See you on Valentine’s Day, {NAME} 💖</h2>
            <p>Only {days_to_valentine()} days to go… ⏳</p>
        </div>

        <script>
        function firework() {{
            const fw = document.createElement("div");
            fw.className = "firework";
            fw.style.left = Math.random() * window.innerWidth + "px";
            fw.style.top = Math.random() * window.innerHeight + "px";
            fw.style.background = ["#ff4b6e","#ffd700","#00eaff","#ff9aff","#7CFF00"][Math.floor(Math.random()*5)];
            document.body.appendChild(fw);
            setTimeout(() => fw.remove(), 1400);
        }}
        setInterval(firework, 200);
        </script>
    """, unsafe_allow_html=True)

    st.audio("love.mp3")

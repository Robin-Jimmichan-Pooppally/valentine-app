import streamlit as st
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="💖 Valentine 💖", layout="wide")

NAME = st.secrets["NAME"]

# ---------------- SESSION STATE ----------------
if "story_index" not in st.session_state:
    st.session_state.story_index = 0

if "finished" not in st.session_state:
    st.session_state.finished = False

if "no_pos" not in st.session_state:
    st.session_state.no_pos = random.randint(-120, 120)

# ---------------- STORY ----------------
story = [
    f"{NAME}, before you scroll away… 💖",
    "There’s something I’ve been meaning to ask.",
    "",
    "May 6th — that’s when I met you.",
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

# ---------------- UI + ANIMATIONS ----------------
st.markdown(
    """
    <style>
    body {
        background: radial-gradient(circle at top, #1c1c1c, #000);
        color: white;
    }

    .story {
        text-align: center;
        margin-top: 100px;
        font-size: 22px;
        line-height: 1.9;
        max-width: 850px;
        margin-left: auto;
        margin-right: auto;
        animation: cinematic 1.2s ease forwards;
    }

    @keyframes cinematic {
        from {
            opacity: 0;
            transform: translateY(25px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .buttons {
        display: flex;
        justify-content: center;
        gap: 40px;
        margin-top: 40px;
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
        position: relative;
        left: VARLEFTpx;
    }

    /* ❤️ Heart fireworks */
    .hearts {
        position: fixed;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        pointer-events: none;
        animation: rise 2s ease-out forwards;
    }

    @keyframes rise {
        from { opacity: 1; transform: translate(-50%, 0); }
        to { opacity: 0; transform: translate(-50%, -600px); }
    }
    </style>
    """.replace("VARLEFT", str(st.session_state.no_pos)),
    unsafe_allow_html=True
)

# 🎶 Background music placeholder (add later)
# st.audio("love.mp3", loop=True)

# ---------------- STORY FLOW ----------------
if not st.session_state.finished:

    st.markdown(
        f"""
        <div class="story">
            {story[st.session_state.story_index]}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    if st.button("Continue 💫"):
        if st.session_state.story_index < len(story) - 1:
            st.session_state.story_index += 1
        else:
            st.session_state.finished = True

else:
    # ---------------- FINAL QUESTION ----------------
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
            for _ in range(6):
                st.markdown(
                    "<div class='hearts'>❤️ 💖 💘 💝 💗</div>",
                    unsafe_allow_html=True
                )
            st.success("YAY 💖 I LOVE YOU!")

    with col2:
        if st.button("NO 🙃"):
            st.session_state.no_pos = random.randint(-200, 200)
            st.warning("Nope 😈 Try again")

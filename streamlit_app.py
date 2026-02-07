import streamlit as st
import time
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="💖 A Question From My Heart", layout="centered")

# Get name from Streamlit Secrets
NAME = st.secrets["NAME"]

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
}

.main {
    text-align: center;
}

.big-text {
    font-size: 28px;
    font-weight: 600;
    margin-top: 40px;
}

.story {
    font-size: 20px;
    margin-top: 25px;
}

.buttons {
    margin-top: 40px;
}

button {
    font-size: 20px !important;
    padding: 12px 30px !important;
    border-radius: 30px !important;
}

#no-btn {
    position: relative;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "step" not in st.session_state:
    st.session_state.step = 0

if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

# ---------------- INTRO ----------------
if st.session_state.step == 0:
    st.markdown(f"<div class='big-text'>{NAME}, before you scroll away… 💖</div>", unsafe_allow_html=True)
    st.markdown("<div class='story'>there’s something I’ve been meaning to ask.</div>", unsafe_allow_html=True)

    if st.button("Continue 💫"):
        st.session_state.step = 1
        st.rerun()

# ---------------- STORY (AUTO TYPING) ----------------
elif st.session_state.step == 1:
    story_lines = [
        "May 6th — that’s when I met you. A normal day… that became unforgettable.",
        "By June 7th, we were committed. Somehow, so naturally, my heart already knew.",
        "Then life tested us. I had to leave for Kerala for six long months.",
        "And you waited. Patiently. Faithfully. Loving me even from miles away.",
        "Your hugs, our cuddles — they became my safest place.",
        "Even when days were hard, you made me feel like home."
    ]

    placeholder = st.empty()

    for i in range(len(story_lines)):
        placeholder.markdown(
            "<div class='story'>" + "<br>".join(story_lines[:i+1]) + "</div>",
            unsafe_allow_html=True
        )
        time.sleep(1.2)

    if st.button("One more thing… 💭"):
        st.session_state.step = 2
        st.rerun()

# ---------------- EMOTIONAL PART ----------------
elif st.session_state.step == 2:
    emotional_lines = [
        "I know we had a lot of fights.",
        "I know I was never a perfect boyfriend.",
        "There were moments I didn’t understand you the way I should have.",
        "Moments where my silence hurt more than words.",
        "But through every argument, one thing never changed — I loved you.",
        "Not the easy kind of love… but the kind that stays.",
        "I don’t promise perfection.",
        "I promise effort. Growth. Choosing you — again and again."
    ]

    placeholder = st.empty()

    for i in range(len(emotional_lines)):
        placeholder.markdown(
            "<div class='story'>" + "<br>".join(emotional_lines[:i+1]) + "</div>",
            unsafe_allow_html=True
        )
        time.sleep(1.2)

    if st.button("So… 💘"):
        st.session_state.step = 3
        st.rerun()

# ---------------- QUESTION ----------------
elif st.session_state.step == 3 and not st.session_state.yes_clicked:
    st.markdown("<div class='big-text'>Will you be my Valentine? 💌</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES 💘"):
            st.session_state.yes_clicked = True
            st.balloons()
            st.rerun()

    with col2:
        # Fake NO button that "moves"
        if st.button("NO 🙃"):
            st.warning("Nice try 😈")

# ---------------- YES SCREEN ----------------
elif st.session_state.yes_clicked:
    st.markdown(f"<div class='big-text'>YAYYY 💖</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='story'>I love you, {NAME}. You just made me the happiest person alive 🥹💞</div>",
        unsafe_allow_html=True
    )
    st.balloons()

# ---------------- MUSIC (Optional) ----------------
# When you add love.mp3 to GitHub root, uncomment this:
# st.audio("love.mp3", loop=True)

# 💖 Valentine's Day Proposal Web App

An interactive, romantic web application to ask your special someone to be your Valentine! Built with Python and Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_DEPLOYED_LINK_HERE)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"The best gifts aren't bought - they're built with love."** 💕

---

## ✨ Features

- 📝 **Typewriter Effect Storytelling** - Your love story unfolds one message at a time
- 🎵 **Background Music Player** - Add your favorite romantic song
- 💘 **Interactive Question** - "Will you be my Valentine?"
- ✅ **YES Button** - Triggers celebration with balloons!
- 😄 **Playful NO Button** - Runs away when hovered over (inspired by viral Valentine memes)
- 🎈 **Balloons Animation** - Celebration when they say yes
- ⏳ **Live Countdown** - Days until Valentine's Day
- 🎨 **Beautiful Dark Theme** - Romantic gradient background with smooth animations
- 🔒 **Privacy First** - Keep names and personal messages private
- 📱 **Mobile Friendly** - Works perfectly on all devices

---

## 🚀 Quick Start (5 Minutes!)

### Prerequisites

- Python 3.7 or higher
- A romantic heart ❤️
- Your favorite love song (MP3 format)

### Installation

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/valentine-proposal.git
cd valentine-proposal
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Set up your configuration:**

**Option A: Using Streamlit Secrets (Recommended)**
```bash
mkdir .streamlit
echo 'NAME = "Their Name"' > .streamlit/secrets.toml
```

**Option B: Using Config File**
```bash
cp config_template.py config.py
# Then edit config.py with their name
```

**4. Add your music file:**
- Download your favorite romantic song as MP3
- Rename it to `song.mp3`
- Place it in the project folder

**5. Run the app:**
```bash
streamlit run app.py
- Share the link with your Valentine! 💖

---

## 🎨 Customization Guide

### 1. Change Your Love's Name

**Using secrets.toml:**
```toml
# .streamlit/secrets.toml
NAME = "Sarah"
```

**Or using config.py:**
```python
# config.py
NAME = "Sarah"
```

### 2. Customize Your Story

Edit the `story` array in `app.py`:
```python
story = [
    f"{NAME}, before you scroll away… 💖",
    "Remember when we first met?",
    "That moment changed everything.",
    "",  # Empty string = line break
    "Every day with you is a gift.",
    # Add your own messages here!
]
```

**💡 Pro Tips:**
- Use `""` (empty string) for line breaks between sections
- Keep messages short and heartfelt (3-10 words per line)
- Use emojis to add emotion 💕
- Tell YOUR unique story - that's what makes it special!

### 3. Customize the Final Message

Find the "Message after YES" section in the `else:` block:
```python
Thank you for saying yes, {NAME}.<br>
Thank you for being mine.<br>
Thank you for being you.
```

Replace with your own heartfelt message!

### 4. Adjust Typing Speed

In the `typewriter()` function:
```python
time.sleep(0.03)  # Lower = faster, Higher = slower
```

**Speed Guide:**
- `0.01` = Very fast ⚡⚡
- `0.03` = Fast (recommended) ⚡
- `0.05` = Medium
- `0.1` = Slow
- `0.2` = Very slow 🐌

### 5. Change Colors & Styling

Edit the CSS in the `STYLES` section:
```python
# Background gradient
background: radial-gradient(circle at top, #1a1a1a, #000)

# Button color
background: #ff4d6d  # Pink/red - change to any hex color

# Text color
color: white
```

**Color Palette Ideas:**
- Classic Red: `#ff4d6d`
- Rose Gold: `#b76e79`
- Purple Love: `#9d4edd`
- Ocean Blue: `#4cc9f0`

### 6. Music Setup

**Option A: Local File (Fastest)**
1. Download romantic song as MP3
2. Rename to `song.mp3`
3. Place in project folder

**Option B: Google Drive (For large files)**
1. Upload MP3 to Google Drive
2. Share → Anyone with link can view
3. Copy file ID from URL: `https://drive.google.com/file/d/FILE_ID_HERE/view`
4. Update code:
```python
file_id = "YOUR_FILE_ID_HERE"
music_url = f"https://drive.google.com/uc?export=download&id={file_id}"
```

---

## 🌐 Deploy Online (Free!)

### Deploy on Streamlit Cloud

**Step 1: Push to GitHub**
```bash
git add .
git commit -m "My Valentine's Day app"
git push origin main
```

**Step 2: Deploy**
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub repository
4. Select your repo and `app.py`
5. Click "Deploy"

**Step 3: Add Secrets**
1. Go to App Settings → Secrets
2. Add:
```toml
NAME = "Their Name"
```

**Step 4: Share the link!** 💖

---

## 🔒 Privacy & Security

Your personal information stays private:

✅ **Names** - Stored in gitignored files (`.streamlit/secrets.toml` or `config.py`)  
✅ **Messages** - You customize them locally  
✅ **Music** - Can be gitignored (add `*.mp3` to `.gitignore`)  
✅ **Deployment** - Use Streamlit Cloud secrets for production

**What's shared publicly:**
- The code framework
- The app structure
- Generic instructions

**What stays private:**
- Your Valentine's name
- Your personal story
- Your music choice (optional)

---

## 📱 Mobile Friendly

The app is fully responsive and works beautifully on:
- 📱 iPhone & Android phones
- 💻 Tablets (iPad, etc.)
- 🖥️ Desktop computers
- All modern browsers

---

## 🎯 How It Works
```
1. Story Phase
   ↓
   Your custom love story appears with typewriter effect
   
2. Continue Buttons
   ↓
   They click through each message at their own pace
   
3. The Big Question
   ↓
   "Will you be my Valentine?" appears
   
4. Interactive Buttons
   ↓
   YES → 🎈 Balloons + Romantic message
   NO → 😄 Button runs away (impossible to click!)
   
5. Celebration
   ↓
   Beautiful thank you message when they say YES!
```

---

## 💡 Creative Story Ideas

### 🌟 First Date Story
```python
story = [
    f"{NAME}, remember our first date?",
    "The coffee shop on 5th street...",
    "You laughed at my terrible joke.",
    "I knew right then you were special.",
    "",
    "Will you be my Valentine?",
]
```

### 🌍 Long Distance Love
```python
story = [
    f"{NAME}, 1,247 miles apart...",
    "But you've never felt far away.",
    "Every video call, every text...",
    "Made my heart feel closer to yours.",
    "",
    "Distance means nothing when someone means everything.",
]
```

### 📅 Anniversary Edition
```python
story = [
    f"{NAME}, it's been 365 days...",
    "365 days of laughter.",
    "365 days of adventures.",
    "365 days of falling deeper in love.",
    "",
    "Here's to 365 more. 💕",
]
```

### 💍 Proposal Style
```python
story = [
    f"{NAME}, before I ask you something...",
    "I want you to know...",
    "Every moment with you is perfect.",
    "You're my best friend, my soulmate.",
    "",
    "Will you be my Valentine?",
    "Today, tomorrow, and forever?",
]
```

---

## 🎵 Recommended Songs

**Classic Romantic:**
- "A Thousand Years" - Christina Perri ⭐ (Used in demo)
- "Perfect" - Ed Sheeran
- "All of Me" - John Legend
- "Thinking Out Loud" - Ed Sheeran
- "Can't Help Falling in Love" - Elvis Presley

**Modern Love:**
- "Lover" - Taylor Swift
- "Die With A Smile" - Lady Gaga & Bruno Mars
- "Beautiful Things" - Benson Boone
- "Enchanted" - Taylor Swift

**Bollywood (Romantic):**
- "Tum Hi Ho" - Arijit Singh
- "Pehla Nasha" - Udit Narayan
- "Tujhe Kitna Chahne Lage" - Arijit Singh

**Or use YOUR special song!** 💖

---

## 🛠️ Tech Stack

- **Python 3.7+** - Core language
- **Streamlit** - Web framework for rapid development
- **JavaScript** - Interactive button animations
- **HTML/CSS** - Custom styling and animations
- **Streamlit Components** - Advanced interactivity

---

## 📂 Project Structure
```
valentine-proposal/
│
├── .streamlit/
│   └── secrets.toml           # Your private config (gitignored)
│
├── streamlit_app.py           # Main application
├── song.mp3                   # Your music file (add this)          
├── requirements.txt           # Python dependencies

```

## 🐛 Troubleshooting

### Music not playing?
- ✅ Check file is named exactly `song.mp3`
- ✅ Try clicking play manually (browsers may block autoplay)
- ✅ Verify file is in same folder as `app.py`
- ✅ Check file format is MP3

### Typewriter too slow/fast?
- Change `time.sleep(0.03)` in the `typewriter()` function
- Smaller number = faster
- Larger number = slower

### App won't run?
- ✅ Install Streamlit: `pip install streamlit`
- ✅ Check Python version: `python --version` (needs 3.7+)
- ✅ Verify you're in the correct directory

### Name not showing?
- ✅ Check `.streamlit/secrets.toml` exists
- ✅ Verify format: `NAME = "Their Name"` (with quotes)
- ✅ Or use `config.py` method instead

### Deployment issues?
- ✅ All files pushed to GitHub
- ✅ Check file size limits (100MB max per file)
- ✅ Add secrets in Streamlit Cloud settings
- ✅ Verify `song.mp3` is included (or use Google Drive link)

**Still stuck?** Open an issue on GitHub!

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contributions:
- [ ] Photo gallery slideshow
- [ ] Multiple music options with playlist
- [ ] Different animation styles (hearts, stars, etc.)
- [ ] Customizable themes (light mode, etc.)
- [ ] Video background option
- [ ] Multiple language support
- [ ] Download/share feature
- [ ] Memory timeline feature

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**TL;DR:** You can use this freely for personal or commercial use! Just keep the license notice.

---

## 💝 Made With Love

Created for Valentine's Day 2026 with ❤️

### Why I Built This

I wanted to create something special for my Valentine that was more meaningful than a generic gift. This app combines:
- 💻 My coding skills
- ❤️ My feelings
- 🎨 Creativity
- 🎵 Our favorite song

The result? A unique, personalized experience that she'll never forget!

---

## 🎉 Success Stories

*Did this help you win someone's heart? Share your story!*

**Want to be featured?** 
- ⭐ Star this repo
- 📧 Share your success story
- 🐦 Tag me on social media

> "Your story could be here! Open an issue or PR to share how it went!" 💕

---

## 🙏 Acknowledgments

- Inspired by viral Valentine's Day memes
- Built with [Streamlit](https://streamlit.io)
- Music: "A Thousand Years" by Christina Perri
- Special thanks to everyone who believes in building love, not just buying it 💕

---

## ⭐ Show Your Support

If this project helped you:
- ⭐ **Star this repository**
- 🔄 **Share with friends** who need romantic inspiration
- 💬 **Tell me your story** - I'd love to hear how it went!
- ☕ **Buy me a coffee** (optional link)

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/valentine-proposal?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/valentine-proposal?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/YOUR_USERNAME/valentine-proposal?style=social)

---

### 💌 Final Words

> "In a world of generic gifts and last-minute flowers, dare to create something unique. Code your love story. Build your memories. Show them that they're worth the effort."

**Happy Valentine's Day!** 💖

---

*Built with ❤️ and Python | © 2025 Your Name*

---

**P.S.** Don't forget to actually tell them you love them IRL too! The app is just the beginning. 😊💕

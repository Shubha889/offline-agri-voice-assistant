# 🌾 Voice-Based Crop Advisory Assistant

## 📌 Overview
This project is a voice-enabled crop advisory system that allows users to interact using speech.

The system:
- Converts speech to text (STT)
- Matches user input with crop data
- Returns results via text and speech (TTS)

---

## ⚙️ Features
- Voice input using Whisper
- Voice output using pyttsx3
- Supports crop → phase → stage → topic navigation
- Handles speech errors using fuzzy matching
- Works offline

---

## 🧠 Tech Stack
- Python
- Pandas
- Whisper (STT)
- pyttsx3 (TTS)
- rapidfuzz (fuzzy matching)

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py


## 🌱 Supported Crops
- Rice
- Maize
- Ragi
- Sugarcane
- Ginger
- Potato
- Arecanut
- Coffee
- Coconut
- Pepper

## 🚀 Future Improvements
- Kannada voice support
- Better intent detection
- GUI/Web application
- AI/LLM integration
- Real-time crop recommendations
- Multi-language support
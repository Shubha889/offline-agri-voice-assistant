# 🌾 Offline Agricultural Voice Assistant

A lightweight offline voice-enabled crop advisory assistant built using Python, Whisper Speech-to-Text (STT), and local Text-to-Speech (TTS) systems.

The project is designed for low-cost agricultural environments where internet access and cloud API costs may be restrictive.

---

# 🚀 Features

* 🎙️ Offline Speech-to-Text using Whisper
* 🔊 Local Text-to-Speech responses
* 🌱 Crop advisory dataset integration
* 🧠 Fuzzy matching for speech error handling
* 📊 Multi-stage crop → phase → stage → topic navigation
* 💻 Fully offline execution
* ❌ No paid APIs
* ❌ No cloud dependency

---

# 🧠 Tech Stack

* Python
* OpenAI Whisper
* FFmpeg
* Pandas
* NumPy
* pyttsx3
* RapidFuzz
* Torch

---

# 🌱 Supported Crops

* Rice
* Maize
* Ragi
* Sugarcane
* Ginger
* Potato
* Arecanut
* Coffee
* Coconut
* Pepper

---

# ▶️ How to Run

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Run the application

```bash
python main.py
```

---

# ⚙️ System Workflow

1. User speaks crop-related query
2. Whisper converts speech → text
3. Fuzzy matching identifies crop/stage/topic
4. Dataset response is fetched
5. Bot speaks response using local TTS

---

# 🚀 Future Improvements

* Kannada Text-to-Speech support
* Better intent detection
* GUI/Web application
* RAG/LLM integration
* Real-time conversational interaction
* Advanced crop recommendation engine

---

# 📌 Project Background

This project began as an exploration into building a fully offline, low-cost multilingual agricultural voice assistant without relying on paid APIs or LLM services.

The primary goal was to create a practical speech-based system suitable for resource-constrained rural environments.

Development was paused after completing the foundational architecture and deployment pipeline alongside full-time employment responsibilities.

Even in its current state, the project demonstrates practical voice AI integration, local deployment concepts, and dataset-driven conversational workflows.

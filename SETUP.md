```markdown
# ⚙️ Setup Instructions

Follow these steps to run the project locally.

---

## 1. Extract Project
Unzip the project folder.

---

## 2. Install Python
Ensure Python 3.9+ is installed.

Check:
```bash
python --version

# ---

# ## 3. Create Virtual Environment
# ```bash
# python -m venv venv

# ---

# ## 4. Activate Virtual Environment
# ```bash
# Windows (PowerShell)
# .\venv\Scripts\Activate
# Windows (CMD)
# venv\Scripts\activate.bat

# # After activation, you should see: (venv)

# ---

# ## 5. Install Dependencies
# ```bash
# pip install -r requirements.txt

# # This will install:

# pandas
# numpy
# sounddevice
# openai-whisper
# pyttsx3
# rapidfuzz
# torch

# ---

# ## 6. Run the Application
# ```bash
# python main.py

# ---

# ## 7. How to Use
# Press ENTER to start recording
# Speak clearly (e.g., "rice", "vegetative phase")
# Press ENTER again to stop recording
# Follow the voice prompts

# ---

# ## Supported Crops
# Rice
# Maize
# Ragi
# Sugarcane
# Ginger
# Potato
# Arecanut
# Coffee
# Coconut
# Pepper

# ---

# ## Important Notes
# Ensure microphone access is enabled
# Use a quiet environment for better accuracy
# First run may take time (Whisper model loads)
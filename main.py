import pandas as pd
import sounddevice as sd
import numpy as np
import whisper
from rapidfuzz import process
from tts import speak

# =========================
# LOAD MODEL (LIGHT)
# =========================
model = whisper.load_model("tiny")

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("crop_data.csv", encoding="latin1")
df.columns = df.columns.str.strip()
df = df.fillna("")

print("Columns:", df.columns.tolist())

# =========================
# RECORD AUDIO
# =========================
def record_audio():
    input("\n👉 Press ENTER to START recording...")
    print("🎙️ Recording... Press ENTER to STOP")

    recording = []

    def callback(indata, frames, time, status):
        recording.append(indata.copy())

    stream = sd.InputStream(callback=callback, channels=1, samplerate=16000)
    stream.start()

    input()
    stream.stop()
    stream.close()

    if len(recording) == 0:
        return np.array([], dtype="float32")

    audio = np.concatenate(recording, axis=0)
    return audio.flatten()

# =========================
# TRANSCRIBE
# =========================
def transcribe(audio):
    if len(audio) == 0:
        return ""

    try:
        result = model.transcribe(audio, language="en", fp16=False)
        text = result["text"].strip().lower()
        print("You said:", text)
        return text
    except Exception as e:
        print("Error:", e)
        return ""

# =========================
# FUZZY MATCH
# =========================
def fuzzy_match(user_input, choices):
    if not user_input:
        return None

    match, score, _ = process.extractOne(user_input, choices)

    if score > 60:
        return match
    return None

# =========================
# MAIN BOT
# =========================
def main():

    speak("Hello! I am your crop advisory assistant.")

    crops = df["Crop"].str.lower().unique().tolist()
    speak("Available crops are " + ", ".join(crops))

    while True:

        # -------- CROP --------
        audio = record_audio()
        user_input = transcribe(audio)

        crop = fuzzy_match(user_input, crops)

        if not crop:
            speak("Could not understand crop. Try again.")
            continue

        speak(f"{crop} selected")

        crop_df = df[df["Crop"].str.lower() == crop]

        # -------- PHASE --------
        phases = crop_df["Phase"].str.lower().unique().tolist()
        speak("Available phases are " + ", ".join(phases))

        while True:
            audio = record_audio()
            user_input = transcribe(audio)

            phase = fuzzy_match(user_input, phases)

            if not phase:
                speak("Please select a valid phase.")
                continue

            speak(f"{phase} selected")

            phase_df = crop_df[crop_df["Phase"].str.lower() == phase]

            # -------- STAGE --------
            stages = phase_df["Stage"].str.lower().unique().tolist()
            speak("Available stages are " + ", ".join(stages))

            while True:
                audio = record_audio()
                user_input = transcribe(audio)

                stage = fuzzy_match(user_input, stages)

                if not stage:
                    speak("Please select a valid stage.")
                    continue

                speak(f"{stage} selected")

                stage_df = phase_df[phase_df["Stage"].str.lower() == stage]

                # -------- TOPIC --------
                topics = stage_df["Topic"].str.lower().unique().tolist()
                speak("Available topics are " + ", ".join(topics))

                while True:
                    audio = record_audio()
                    user_input = transcribe(audio)

                    topic = fuzzy_match(user_input, topics)

                    if not topic:
                        speak("Please select a valid topic.")
                        continue

                    speak(f"{topic} selected")

                    topic_df = stage_df[stage_df["Topic"].str.lower() == topic]

                    # -------- OUTPUT (FIXED TTS OVERLOAD) --------
                    results = topic_df["Content"].tolist()

                    if results:
                        speak("Here are the results")
                        speak(". ".join(results))   # ✅ FIXED
                    else:
                        speak("No data found")

                    return


# =========================
# RUN
# =========================
if __name__ == "__main__":
    main()
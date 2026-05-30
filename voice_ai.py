import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import pyttsx3
import numpy as np
import tempfile


# ==========================================
# TEXT TO SPEECH
# ==========================================

engine = pyttsx3.init()

def speak(text):

    engine.say(text)

    engine.runAndWait()


# ==========================================
# LISTEN FUNCTION
# ==========================================

def listen():

    fs = 44100

    seconds = 5

    try:

        print("Listening...")

        # RECORD AUDIO
        recording = sd.rec(
            int(seconds * fs),
            samplerate=fs,
            channels=1,
            dtype='int16'
        )

        sd.wait()

        # SAVE TEMP WAV FILE
        temp_wav = tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        )

        write(
            temp_wav.name,
            fs,
            np.array(recording, dtype=np.int16)
        )

        recognizer = sr.Recognizer()

        # READ AUDIO
        with sr.AudioFile(temp_wav.name) as source:

            audio = recognizer.record(source)

        # CONVERT SPEECH TO TEXT
        text = recognizer.recognize_google(audio)

        return text

    except Exception as e:

        return f"Voice recognition error: {str(e)}"
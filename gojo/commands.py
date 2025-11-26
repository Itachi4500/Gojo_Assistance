import webbrowser
import datetime
import os
from .tts_engine import speak
from .ai_engine import ask_ai

def execute_command(cmd: str):
    if not cmd:
        speak("I didn't catch that.")
        return

    # --- Basic Commands ---
    if "time" in cmd:
        t = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {t}.")
        return

    if "date" in cmd:
        d = datetime.datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {d}.")
        return

    if "open youtube" in cmd:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
        return

    if "open google" in cmd:
        speak("Opening Google.")
        webbrowser.open("https://google.com")
        return

    if "search for" in cmd:
        query = cmd.replace("search for", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return

    # --- AI fallback ---
    speak("Thinking...")
    reply = ask_ai(cmd)
    speak(reply)

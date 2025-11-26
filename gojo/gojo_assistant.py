from .speech_engine import listen
from .tts_engine import speak
from .commands import execute_command

def start_gojo():
    speak("Gojo online. Say 'Gojo' to wake me up.")

    while True:
        text = listen()

        if text and "gojo" in text:
            speak("Yes, I'm listening.")
            command = listen()
            execute_command(command)

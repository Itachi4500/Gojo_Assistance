import pyttsx3

engine = pyttsx3.init()

def speak(text: str):
    print("Gojo:", text)
    engine.say(text)
    engine.runAndWait()

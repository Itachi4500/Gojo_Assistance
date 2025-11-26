import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen():
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.4)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        text = recognizer.recognize_google(audio).lower()
        print("You:", text)
        return text
    except:
        return None

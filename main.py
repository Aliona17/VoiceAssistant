import pyttsx3
from SpeechRecognition import SpeechRecognition as sp

def Voice():
    d = sp()
    engine = pyttsx3.init()

    if d.isdigit():
        engine.say("You said digit, say string")
        engine.runAndWait()
        return Voice()
    elif d.isalpha():
        engine.say("All is OK")
        engine.runAndWait()
    return d



Voice()


# print(sp())




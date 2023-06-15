import pyttsx3

def Voice():
    d = input('Write something: ')
    if d.isdigit():
        engine = pyttsx3.init()
        engine.say("You wrote digit, write string")
        engine.runAndWait()
        Voice()
    elif d.isalpha():
        engine = pyttsx3.init()
        engine.say("All is OK")
        engine.runAndWait()

Voice()





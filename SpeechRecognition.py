import speech_recognition as s_r

print(s_r.__version__)
r = s_r.Recognizer()

my_mic = s_r.Microphone(device_index=0)

with my_mic as source:
    print("Say now!!!!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
text = r.recognize_google(audio)
print(text)

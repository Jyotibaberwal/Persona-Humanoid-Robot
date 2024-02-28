import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    said = r.recognize_google(audio)
    said = said.lower()
    print(said)
    
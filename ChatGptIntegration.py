import openai
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)
vol = engine.getProperty('volume')
engine.setProperty('volume', 0.9)
engine.setProperty('rate', 190)
rate = engine.getProperty('rate')
print(vol)
print(rate)

openai.api_key = "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"
modelengine = "text-davinci-003"

while True:
    s = input()
    completion = openai.Completion.create(
        engine = modelengine,
        prompt = s,
        max_tokens = 50,
        n = 1,
        stop = None,
        temperature = 1.5,
    )
    print("Output:")
    response = completion.choices[0].text
    print(response)
    import pyttsx3
    engine.say(response)
    engine.runAndWait()
    
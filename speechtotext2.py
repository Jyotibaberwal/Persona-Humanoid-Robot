from gtts import gTTS
from playsound import playsound
import os

tts = gTTS("Hello World How are you ")
tts.save("speech.mp3")
playsound("speech.mp3")
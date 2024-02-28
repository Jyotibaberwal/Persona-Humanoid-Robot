import wave
import numpy as np
import sys
import matplotlib.pyplot as plt
from pydub import AudioSegment

import speech_recognition as sr
from pyfirmata import Arduino, SERVO, util
from time import sleep
import openai
from gtts import gTTS
from playsound import playsound
import cv2
import numpy as np
import threading

sound = AudioSegment.from_mp3("speech.mp3")
sound.export("wvfile.wav", format="wav")


w = wave.open("wvfile.wav", "rb")

print("Number of channels ", w.getnchannels())
print("sample width ", w.getsampwidth())
print("frame rate ", w.getframerate())
print("Number of frames ", w.getnframes())
print("parameter", w.getparams())

raw = w.readframes(-1)
raw = np.frombuffer(raw, 'int16')
raw = abs(raw)
mx = max(raw)
raw = raw/mx
r = []
for i in range(0,len(raw),12):
    r.append(raw[i])

plt.plot(r)
plt.show()
plt.plot(raw)
plt.show()
     



# raw = abs(raw)
# mx = max(raw)
# raw = raw/ mx
# mx = max(raw)
# plt.plot(raw)
# plt.show()
# n = min(raw)
# print(mx)
# print(n)

# port = '/dev/ttyUSB0'
# board = Arduino(port)


# pinMouth = 5
# pinEyeX = 4
# pinEyeY = 3
# pinNeck = 6
# pinLEDRed1 = 13
# pinLEDRed2 = 12
# pinLEDBlue1 = 10
# pinLEDBlue2 = 11
# NeckPos = 120
# EyeYPos = 40
# thread_bool = True


# board.digital[pinMouth].mode = SERVO
# board.digital[pinEyeX].mode = SERVO
# board.digital[pinEyeY].mode = SERVO
# board.digital[pinNeck].mode = SERVO
# print("Start")
# print(len(raw))
# for j in range(0,10000):
#     i = raw[j]
#     y = (1-i)*75
#     board.digital[pinMouth].write(y)

# print("Stop")









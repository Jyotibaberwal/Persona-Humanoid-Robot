import speech_recognition as sr
from pyfirmata import Arduino, SERVO, util
from time import sleep
import openai
from gtts import gTTS
from playsound import playsound
import cv2
import numpy as np
import threading

##############################################################

r = sr.Recognizer()
mic = sr.Microphone()

##############################################################

openai.api_key = "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"
modelengine = "text-davinci-003"
##############################################################

port = '/dev/ttyUSB0'
board = Arduino(port)
##############################################################

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
vid = cv2.VideoCapture(0)
##############################################################


pinMouth = 5
pinEyeX = 4
pinEyeY = 3
pinNeck = 6
pinLEDRed1 = 13
pinLEDRed2 = 12
pinLEDBlue1 = 10
pinLEDBlue2 = 11
NeckPos = 120
EyeYPos = 40
thread_bool = True
##############################################################

def LedBlue(x):
    board.digital[pinLEDBlue1].write(x)
    board.digital[pinLEDBlue2].write(x)
##############################################################

def LedRed(x):
    board.digital[pinLEDRed1].write(x)
    board.digital[pinLEDRed2].write(x)   
##############################################################

board.digital[pinMouth].mode = SERVO
board.digital[pinEyeX].mode = SERVO
board.digital[pinEyeY].mode = SERVO
board.digital[pinNeck].mode = SERVO
LedBlue(1)
LedRed(1)

##############################################################

def moveall():
    board.digital[pinEyeY].write(40)
    board.digital[pinEyeX].write(90)
    board.digital[pinMouth].write(0)
    sleep(0.5)
    board.digital[pinMouth].write(75)  
    board.digital[pinNeck].write(120)
    # board.digital[pinEyeX].write(70)
    
    # board.digital[pinEyeY].write(60)
    # board.digital[pinEyeX].write(120)
    # board.digital[pinEyeX].write(90)
##############################################################

def orientation():
    global EyeYPos
    global NeckPos
    global pinEyeY
    global pinNeck
    global thread_bool
    while thread_bool:
        
        _, frame = vid.read()#reads the current frame to the variable frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#converts frame -> grayscaled image
        faces = face_cascade.detectMultiScale(gray, minSize=(80, 80), minNeighbors=3)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)#draws a rectangle around the face
            Xpos = x+(w/2)#calculates the X co-ordinate of the center of the face.
            Ypos = y+(h/2)
            y= int((70-Ypos)*(0.118)+55)
            x = int(((50-Xpos)/9 + 150))
            if x >  NeckPos:
                for i in range(NeckPos, x):
                    board.digital[pinNeck].write(i)
                    sleep(0.005)
                NeckPos = x
            else:
                for i in range(NeckPos, x, -1):
                    board.digital[pinNeck].write(i)
                    sleep(0.005)
                NeckPos = x
            if y > EyeYPos:
                for i in range(EyeYPos, y):
                    board.digital[pinEyeY].write(i)
                    sleep(0.005)
                EyeYPos = y
            else:
                for i in range(EyeYPos, y, -1):
                    board.digital[pinEyeY].write(i)
                    sleep(0.05)
                EyeYPos = y
                
##############################################################

def interaction():
    while True:
        try:        
            with mic as source:
                r.adjust_for_ambient_noise(source)        
                print("LISTENING.........")
                LedBlue(0)
                LedRed(1)
                audio = r.listen(source)
                LedRed(0)
                LedBlue(1)
                said = r.recognize_google(audio).lower()
                LedRed(1)
                LedBlue(1)
                print(said)
                completion = openai.Completion.create(
                engine = modelengine,
                prompt = said,
                max_tokens = 50,
                n = 1,
                stop = None,
                temperature = 0.5,
                )
                print("Output:")
                response = completion.choices[0].text
                print(response)
                tts  = gTTS(response)
                tts.save("speech.mp3")
                playsound("speech.mp3")
                if said == "close persona":
                    break
        except:
            print("Program stopped")
            
##############################################################  
    

thread_orientation = threading.Thread(target=orientation)
thread_interaction = threading.Thread(target=interaction)

##############################################################

moveall()
thread_orientation.start()
thread_interaction.start()



    
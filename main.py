import pyttsx3 
import speech_recognition as sr 
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
from PyQt5 import Qtwidgets,QtGui,QtCore
from PyQt5.QtGui import QMovie
from PyQt5.Qtwidgets import  *
from PyQt5.Qtcore import *
from PyQt5.QtGui import *
from PyQt5.uic import LoadUiType
import time




flags = QtCore.Qt.WindowFlags(QtCore.Qt.FrameLessWindowHint)




engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty('rate',180)


#text to speech
def speak(audio):
    engine.say(audio)
    print (audio)
    engine.runAndWait()

#to wish you
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning !")
    elif hour>=12 and hour < 18:
        speak("good afternoon !")
    else :
        speak("good evening !")
    speak("sir,how can i help you..  ") 

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()
    @pyqtslot
    def run(self):
        self.JARVIS()



#to convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("listing....")
        r.pause_thresold = 1 #wait 1sec if u don't say anything
        audio = r.listen(source)#,timeout=1,phrase_time_limit=5)

        try:
            print("recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said: {query}\n")

        except Exception as e :
            print("please say it again....")
            return "none"
        return query

#to send email
def sendEmail(to,content) :
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()  #to connect our server to email server
    server.starttls() #to provide security
    server.login("sajanbiswal754@gmail.com","SajanBiswal1234")
    server.sendmail("sajanbiswal754@gmail.com", to,content)
    server.close()

def JARVIS(self):          
if __name__== "__main__":
    wish()
   # takecommand()
    while True:  

        query = takecommand().lower() #logic building for task
        if "open notepad" in query:
            npath ="C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif " close notepad" in query :
            speak("okay ,closing notepad")
            os.system("TASKKILL/F /IM notepad.exe") 

        elif "open command prompt" in query:
            os.system("start cmd") 

        elif "open camera" in query :
            cap = cv2.VideoCapture(0) # use 0 for the internal camera or use 1 for others
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k ==27:
                    break ;
            cap.release()
            cv2.destroyAllWindows() 

        elif "play music" in query:
             music_dir ="D:\\music"  
             songs = os.listdir(music_dir)
             rd = random.choice(songs)
            # for song in songs:           
           #      if song.endwith('.mp3'): # if u only want to play songs in a folder
             os.startfile(os.path.join(music_dir,rd))  #(music_dir,songs[0]) use this to start music from index 0       

        elif " wikipedia" in query :
            speak("searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            speak(results)
            #print(results)   


        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak("sir,what should I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")


        elif 'open linkedin' in query:
            webbrowser.open("www.linkedin.com")
            
        elif "open facebook" in query :
            webbrowser.open("www.facebook.com")  

        elif 'open amazon' in query:
            speak("opening amazon.com")
            webbrowser.open("https://www.amazon.in/")

        elif "today's weather" in query:
            speak("looking for the weather...")
            # r = sr.Recognizer()
            results = webbrowser.open("https://www.accuweather.com/en/in/bhubaneswar/189781/daily-weather-forecast/189781")

        elif " send email " in query :
            try:
                speak("what should i say ?")
                content = takecommand().lower()
                to = "satyamsuryajyoti007@gmail.com "
                sendEmail(to,content)
                speak("email has been sent successfully")

            except Exception as e:
                print(e)
                speak("sorry sir can not send email")    

        elif "exit" in query:
            speak("thanks for using me have a nice day ")
            sys.exit()
        speak("sir, dou you have any other work ?")
        

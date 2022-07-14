#import pyttsx3
#from datetime import datetime
#from tkinter import *
#import speech_recognition as sr
#import subprocess


#root=Tk()
#root.geometry("500x500")
#root.configure(background="Light Blue")
#text_to_speech=pyttsx3.init()
#
#
#label=Label(root,text="Welcome To IndiaX.",bg="lightblue")
#label.place(relx=0.5,rely=0.1,anchor=CENTER)
#
#def speak(audio):
#	text_to_speech.say(audio)
#	text_to_speech.runAndWait()
#
#
#def r_audio():
#	speak("Hi, My Name Is Anand. How May I Help You ?")
#	speech_recognisor=sr.Recognizer()
#	with sr.Microphone() as source:
#		audio=speech_recognisor.listen(source)
#		voice_data=''
#		try:
#			voice_data=speech_recognisor.recognize_google(audio,language="en-in")
#		except sr.UnknownValueError:
#			error_noget="Anand: Sorry, I Didn't Get That"
#			print(error_noget)
#			speak(error_noget)
#	respond(voice_data)
#	print("You: "+voice_data)
#
#
#def respond(voice_data):
#	voice_data=voice_data.lower()
#	print(voice_data)
#	if "What's your name?" in voice_data:
#		speak("My Name Is Anand")
#		print("My Name Is Anand")
#	if "Where are you from?" in voice_data:
#		speak("I am from burdwan, west bengal, india, asia")
#		print("I am from burdwan, west bengal, india, asia")
#
#	if "What's the time?" in voice_data:
#		now=datetime.now()
#		current_time=now.strftime("%H Hours : %M Minutes And %S Seconds")
#		speak("Accroding To Your Local Zone, The Current Time Is: "+current_time)
#		print("Accroding To Your Local Zone, The Current Time Is: "+current_time)
#	if "Open Google" in voice_data:
#		speak("Opening Google")
#		print("Opening Google")
#		webbrowser.get().open("https://www.google.com")
#	if "Open Bing" in voice_data:
#		speak("Opening Bing")
#		print("Opening Bing")
#		webbrowser.get().open("https://www.bing.com")
#	if "Visit YouTube" in voice_data:
#		speak("Opening YouTube")
#		print("Opening YouTube")
#		webbrowser.get().open("https://www.youtube.com/?refer=IndiaX.Windows.Py")
#	if "Open Notepad" in voice_data:
#		speak("Opening SUSPad")
#		print("Opening SUSPad")
#		subprocess.Popen(["notepad.exe"])
#
#
#btn=Button(root,text="Launch")
#btn.place(relx=0.5,rely=0.5,anchor=CENTER)
#
#
#r_audio()
#root.mainloop()


#speech_recognisor= sr.Recognizer() sr.Microphone(device_index=1) with sr.Microphone() as source: speech_recognisor.adjust_for_ambient_noise(source) audio= speech_recognisor.listen(source) voice_data='' try: voice_data= speech_recognisor.recognize_google(audio, language='en-in')










from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root = Tk()
root.geometry("500x500")
root.configure(background="Light Blue")

label=Label(root,text="Welcome To Your Personal Desktop Assistant",bg="Light Blue",font=("Bahnschrift Light",15,"bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()
    
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("How can i help you..?")   
    with sr.Microphone() as source:
        audio=  speech_recognisor.listen(source) 
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('Please repeat i did not get that')
            speak('Please repeat i did not get that')
            r_audio()
        respond(voice_data)
       
        
def respond(voice_data):
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Jarvis")
        print('My name is Jarvis')
            
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
            
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com/")
            
    if "videos" in voice_data:
        speak("Opening YouTube")
        print("Opening YouTube")
        webbrowser.get().open("https://youtube.com/")
            
    if "text editor" in voice_data:
        speak("Opening the app")
        print("Opening the app")
        subprocess.Popen(["notepad.exe"])
        #for mac
        #subprocess.call(["/usr/bin/open", "/Applications/TextEdit.app"])        
        
btn= Button(root, text="Start", command=r_audio,bg="red3", fg="white", padx=10, pady=1,  font=("Arial",11, "bold"), relief=FLAT)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
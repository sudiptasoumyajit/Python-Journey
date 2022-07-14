import pyttsx3
from datetime import datetime
from tkinter import *
import speech_recognition as sr
root=Tk()
root.geometry("500x500")
text_to_speech=pyttsx3.init()
def speak(audio):
	text_to_speech.say(audio)
	text_to_speech.runAndWait()
def r_audio():
	speak("Hi, My Name Is Anand. How May I Help You ?")
	speech_recognisor=sr.Recognizer()
	with sr.Microphone() as source:
		audio=speech_recognisor.listen(source)
		voice_data=''
		try:
			voice_data=speech_recognisor.recognize_google(audio,language="en-in")
		except sr.UnknownValueError:
			error_noget="Anand: Sorry, I Didn't Get That"
			print(error_noget)
			speak(error_noget)
	respond(voice_data)
	print("You: "+voice_data)
def respond(voice_data):
	voice_data=voice_data.lower()
	print(voice_data)
	if "What's your name?" in voice_data:
		speak("My Name Is Anand")
		print("My Name Is Anand")
	if "Where are you from?" in voice_data:
		speak("I am from burdwan, west bengal, india, asia")
		print("I am from burdwan, west bengal, india, asia")

	if "What's the time?" in voice_data:
		now=datetime.now()
		current_time=now.strftime("%H Hours : %M Minutes And %S Seconds")
		speak("Accroding To Your Local Zone, The Current Time Is: "+current_time)
		print("Accroding To Your Local Zone, The Current Time Is: "+current_time)
r_audio()
root.mainloop()
#speech_recognisor= sr.Recognizer() sr.Microphone(device_index=1) with sr.Microphone() as source: speech_recognisor.adjust_for_ambient_noise(source) audio= speech_recognisor.listen(source) voice_data='' try: voice_data= speech_recognisor.recognize_google(audio, language='en-in')
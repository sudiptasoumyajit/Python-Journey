from tkinter import *
import random
root=Tk()
root.title("Encapsulation")
root.geometry("500x400")
root.config(bg="lightgrey")
label_name=Label(root,font=("Work Sans",40),bg=white)
label_name.place(relx=0.5,rely=0.3,anchor=CENTER)
class game:
	def __init__(self):
		self.__score=0
	def updateGame(self):
		self.text=["BLACK","PINK","BLUE","YELLOW","GREEN","GREY","ORANGE","PINK"]
	self.random_number_for_text=random.randint(0,6)
	self.color=["black","pink","blue","yellow","green","grey","orange","pink"]
	self.random_number_for_color=random.randint(0,6)
	label_name["text"]=self.text[self.random_number_for_text]
	label_name["fg"]=self.text[self.random_number_for_color]
obj=game()
btn=Button(root,text="START",command=obj.updateGame,bg="darkblue",fg="white",relief=FLAT,padx=10,pady=1)
btn.place(relx=0.65,rely=0.65,anchor=CENTER)
root.mainloop()
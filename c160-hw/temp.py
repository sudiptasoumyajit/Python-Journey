from tkinter import *
from PIL import ImageTk, Image
app=Tk()
#set dimensions
app.geometry("650x650")
app.title("OpenPad Web IDE")
app.minsize=(650,650)
app.maxsize(650,650)
#load images
ico_open=ImageTk.PhotoImage(Image.open("icon-open.png"))
ico_close=ImageTk.PhotoImage(Image.open("icon-close.png"))
ico_save=ImageTk.PhotoImage(Image.open("icon-save.png"))
#info module
about_name=Label(app,text="Your File Name: ")
about_name.place(relx=0.38,rely=0.03,anchor=CENTER)
about_file=Entry(app)
about_file.place(relx=0.56,rely=0.03,anchor=CENTER)
#text area
workspace=Text(app,height=35,width=650)
workspace.place(relx=0.5,rely=0.55,anchor=CENTER)
#action
def funOpen():
    #code
    print("Open")
act_open=Button(app,image=ico_open,text="Open Your Recent File")
act_open.place(relx=0.05,rely=0.03,anchor=CENTER)
def funClose():
    #code   
    print("Close")
act_close=Button(app,image=ico_close,text="Close Your Recent File")
act_open.place(relx=0.05,rely=0.03,anchor=CENTER)
def funSave():
    #code
    print("Save")
act_save=Button(app,image=ico_open,text="Save Your Recent File")
act_save.place(relx=0.05,rely=0.03,anchor=CENTER)
app.mainloop()

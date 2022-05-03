from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
app=Tk()
#set dimensions
app.geometry("650x650")
app.title("OpenPad")
app.minsize=(650,650)
app.maxsize(650,650)
#load images
ico_open=ImageTk.PhotoImage(Image.open("icon-open.png"))
ico_close=ImageTk.PhotoImage(Image.open("icon-close.jpg"))
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
dataFileName=""
def funOpen():
    global dataFileName
    workspace.delete(1.0,END)
    about_file.delete(0,END)
    ask_filename=filedialog.askopenfilename(
            title="Any Files",
            filetypes=(("Text Files","*.txt"))
        )
    print(ask_filename)
    dataFileName=os.path.basename(ask_filename)
    split_file=dataFileName.split('.')[0]
    about_file.insert(END,split_file)
    root.title("OpenPad [ Opened: ",split_file,"]")
    ask_filename=open(dataFileName,'r')
    textwrite=ask_filename.read()
    workspace.insert(END,textwrite)
    ask_filename.close()
    print("Open")
act_open=Button(app,image=ico_open,text="Open Your Recent File")
act_open.place(relx=0.05,rely=0.03,anchor=CENTER)
def funClose():
    root.destroy()  
    print("Close")
act_close=Button(app,image=ico_close,text="Close Your Recent File")
act_open.place(relx=0.10,rely=0.03,anchor=CENTER)
def funSave():
    fileInput=about_file.get()
    fileOp=open(fileInput+".txt","w")
    data=workspace.get("1.0",END)
    print("Include:" + data)
    fileOp.write(data)
    about_file.delete("0",END)
    workspace.delete("1.0",END)
    messagebox.showinfo("Error","Success")
    print("Save")
act_save=Button(app,image=ico_save,text="Save Your Recent File")
act_save.place(relx=0.15,rely=0.03,anchor=CENTER)
app.mainloop()
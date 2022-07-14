from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
root=Tk()

root.geometry("1000x400")
root.config(bg="white")
root.title("Google Translate")

language=list(LANGUAGES.values())

title_label=Label(root,text="GOOGLE Translate",font=("Work Sans","20","bold"),bg="white")
title_label.place(relx=0.5,rely=0.1,anchor=CENTER)

input_label=Label(root,text="Write Here...",font=("Work Sans","13","bold"),bg="white")
input_label.place(relx=0.02,rely=0.2,anchor=CENTER)

src_lang=ttk.Combobox(root,values=language,width=22,state="readonly")
src_lang.place(relx=0.13,rely=0.2,anchor=CENTER)
src_lang.set("english")

output_label=Label(root,text="Output Here...",font=("Work Sans","13","bold"),bg="white")
output_label.place(relx=0.81,rely=0.2,anchor=CENTER)

dest_lang=ttk.Combobox(root,values=language,width=22,state="readonly")
dest_lang.place(relx=0.98,rely=0.2,anchor=CENTER)
dest_lang.set("hindi")

Input_text=Text(root,font("Work Sans"),height="11",wrap=WORD,padx=5,pady=5,width=60,bg="lightgrey",bd="0")
Input_text.place(relx=0.02,rely=0.5,anchor=W)

Output_text=Text(root,font("Work Sans"),height="11",wrap=WORD,padx=5,pady=5,width=60,bg="lightgrey",bd="0")
Output_text.place(relx=0.98,rely=0.5,anchor=E)

def Tanslate():
    translator=Translator()
    try:
        translated=translator.translate(text=Input_text.get(1.0,END),src=src_lang.get(),dest=dest_lang.get())
        Output_text.delete(1.0,END)
        Output_text.insert(END,translated.text)
    except:
        print("TRY AGAIN")

trans_btn=Button(root,text="Translate",bg="blue2",fg="white",pady=5,command=Translate)
trans_btn.place(relx=0.5,rely=0.85,anchor=CENTER)

root.mainloop()
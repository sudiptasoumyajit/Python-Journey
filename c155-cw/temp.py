from tkinter import *
root=Tk()
root.title("Dictonary")
root.geometry("600x400")

label_of_mutable=Label(root)
label_of_immutable=Label(root)
label_of_tkinter=Label(root)

dictonary={
        'Mutable':'Values Can Be Changed Just Like A List',
        'Immutable':'Values that cannot be changed just like a tuple',
        'Tkinter':'A GUI Libary of Python'
    }

def mutable():
    label_of_mutable["text"]=dictonary['Mutable']
def immutable():
    label_of_immutable["text"]=dictonary['Immutable']
def tkinter():
    label_of_tkinter["text"]=dictonary['Tkinter']

button_mutable=Button(root,text="Mutable",command=mutable)
button_immutable=Button(root,text="Immutable",command=immutable)
button_tkinter=Button(root,text="Tkinter",command=tkinter)

button_mutable.place(relx=0.5,rely=0.1,anchor=CENTER)
button_immutable.place(relx=0.5,rely=0.2,anchor=CENTER)
button_tkinter.place(relx=0.5,rely=0.3,anchor=CENTER)

label_of_mutable.place(relx=0.5,rely=0.6,anchor=CENTER)
label_of_immutable.place(relx=0.5,rely=0.7,anchor=CENTER)
label_of_tkinter.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()
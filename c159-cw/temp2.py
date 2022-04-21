from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("lol")
root.geometry("90x90")
list_name=[
    "Elsa",
    "Micky",
    "Anna",
    "Donald Duck"
    ]
dictonary={
    "name":"frozen",
    "age":"18+"
    }
try:
    print(dictonary["abcd"])
    print(list_name[5])
except IndexError:
    messagebox.showinfo("Hi","lol")
except KeyError:
    messagebox.showinfo("Bye","lol")
root.mainloop()
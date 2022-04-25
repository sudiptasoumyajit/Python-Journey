from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Country")
root.geometry("90x90")
list_name=[
    "India",
    "Bangladesh",
    "Nepal",
    "Japan"
    ]
dictonary={
    "Country":"India",
    "Freedom":"1998",
    "Country":"Bangladesh",
    "Freedom":"1999"
    }
try:
    print(dictonary["abcd"])
    print(list_name[5])
except IndexError:
    messagebox.showinfo("Hi","lol")
except KeyError:
    messagebox.showinfo("Bye","lol")
print(dictonary["Country"])
root.mainloop()
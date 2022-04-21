from tkinter import *
win=Tk()
win.title("Error Sample")
try:
    root.geometry("600")
except:
    print("Python TKinter Code Error @Line 4: The window design should be with X_Size into Y_size. Single Cannot Make It.")
win.mainloop()
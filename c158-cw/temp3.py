from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Error Sample")
root.geometry("600x400")
Input=Entry(root)
Input.pack()
def add():
    num=5
    InputGet=Input.get()
    try:
        print(num+InputGet)
    except(TypeError):
        messagebox.showinfo("Python Console & Tkinter Writting Error @Line11","There is an calulating function error as it cannot store the var in the code and cant genarate it !!")
btn=Button(root,text="Click To Add",command=add)
btn.pack()
root.mainloop()
from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Free Robux Giveaway Genarator")
root.geometry("400x400")
rbxLbl=Label(root,text="Enter Your Robux Amount")
rbxAmount=Entry(root)
rbxLbl.pack()
rbxAmount.pack()
def troll():
    try:
        num=int(rbxAmount.get())
        messagebox.showinfo("You Hacked !!","Your Amount 1000 $ Is Been Taken From Your Bank Account")
    except ValueError:
        messagebox.showinfo("Warning !!","You Are Actually Giving Your Password Of Roblox")
hackBtn=Button(root,text="Get Robux",command=troll)
hackBtn.pack()
root.mainloop()
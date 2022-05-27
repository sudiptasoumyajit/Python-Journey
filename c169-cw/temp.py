from tkinter import *
from tkinter import messagebox

root=Tk()

root.title("PyClas")
root.geometry("900x600")

class CreateElements:
    
    def __int__(self):
        print("This is an CreateElement Class")
    
    def createNewElement(self):
        
        label=Label(root,text="A New Label Is Created Using Class", fg="blue")
        label.pack()
        
        btn=Button(root,text="Click Me",command=self.message)
        btn.pack(padx=20,pady=20)
        
    def message(self):
        messagebox.showinfo("Show Info","You Have Clicked the Button Created Using Class")

obj_of_CreateElement=CreateElements()

btn=Button(root,text="Click To Create Label And Button Element",command=obj_of_CreateElement.createNewElement)
btn.pack(padx=20,pady=10)

root.mainloop()
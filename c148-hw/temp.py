from tkinter import *
import random

root = Tk()
root.title("1D Lists")
root.geometry("400x400")


#start writing here
items_list=["sandwich","mat","bottle","books","dress","chair","food","basket","id"]

label=Label(root)
label2=Label(root)

label["text"]="Listed Items: "+str(items_list)

def content():
    result=random.sample(range(0,5),1)
    label2["text"]="Items To Be Picked First: "+str(result)+" "
    
btn=Button(root,text="Arrange",command=content)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
label.place(relx=0.5,rely=0.5,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()
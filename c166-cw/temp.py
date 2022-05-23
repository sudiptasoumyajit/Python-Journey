print("Like & Subscribe Now !!")

from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Blocky Paint")
root.geometry("600x600")

color_label=Label(root,text="Write A Color: ")
color_label.place(relx=0.6,rey=0.9,anchor=CENTER)

input_box=Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=590,height=510,bg="grey97",highlightbackground="lightgrey")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("turtle.png"))
my_image=canvas.create_image(25,25,image=img)

direction=""

oldx=50
oldy=50

newx=50
newy=50

def draw(direction,oldx,oldy,newx,newy):
    fill_color=input_box.get()

root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()
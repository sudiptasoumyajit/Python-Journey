print("Like & Subscribe Now !!")

from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Blocky Paint")
root.geometry("600x600")

width_label=Label(root,text="Write Width Of Line:")
width_label.place(relx=0.1,rely=0.9,anchor=CENTER)

color_label=Label(root,text="Write A Color: ")
color_label.place(relx=0.6,rely=0.9,anchor=CENTER)

input_box=Entry(root)
input_box.insert(0,"black")
input_box.place(relx=0.8,rely=0.9,anchor=CENTER)

input_box_width=Entry(root)
input_box_width.insert(0,"2")
input_box_width.place(relx=0.35,rely=0.9,anchor=CENTER)

canvas=Canvas(root,width=590,height=510,bg="grey97",highlightbackground="lightgrey")
canvas.pack()

img=ImageTk.PhotoImage(Image.open("turtle.png"))
my_image=canvas.create_image(25,25,image=img)

direction=""

oldx=50
oldy=50

newx=50
newy=50

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx+5
    direction="right"
    draw(direction,oldx,oldy,newx,newy)
    
def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newx=newx-5
    direction="left"
    draw(direction,oldx,oldy,newx,newy)

def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy-5
    direction="up"
    draw(direction,oldx,oldy,newx,newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx=newx
    oldy=newy
    newy=newy+5
    direction="down"
    draw(direction,oldx,oldy,newx,newy)
    
def draw(direction,oldx,oldy,newx,newy):
    fill_color=input_box.get()
    fill_width=input_box_width.get()
    if(direction=='right'):
        right_line=canvas.create_line(oldx,oldy,newx,newy,width=fill_width,fill=fill_color)
    if(direction=='left'):
        left_line=canvas.create_line(oldx,oldy,newx,newy,width=fill_width,fill=fill_color)
    if(direction=='up'):
        up_line=canvas.create_line(oldx,oldy,newx,newy,width=fill_width,fill=fill_color)
    if(direction=='down'):
        down_line=canvas.create_line(oldx,oldy,newx,newy,width=fill_width,fill=fill_color)

root.bind("<Right>",right_dir)
root.bind("<Left>",left_dir)
root.bind("<Up>",up_dir)
root.bind("<Down>",down_dir)

root.mainloop()
import random
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Dice Classic Gamez")
root.geometry("600x400")
root.configure(background="darkblue")
img=ImageTk.PhotoImage(Image.open("dice.jpg"))
player1=Label(root,text="Player 1 (You)",bg="darkgreen",fg="white")
player2=Label(root,text="Player 2 (Your Freind)",bg="darkgreen",fg="white")
player1_score=Label(root,text="Score",bg="darkgreen",fg="white")
player2_score=Label(root,text="Score",bg="darkgreen",fg="white")
lbl_random_dice=Label(root,text="-:-",bg="darkorange",fg="white")
player1.place(relx=0.1,rely=0.4,anchor=CENTER)
player2.place(relx=0.9,rely=0.4,anchor=CENTER)
player1_score.place(relx=0.1,rely=0.6,anchor=CENTER)
player2_score.place(relx=0.9,rely=0.6,anchor=CENTER)
lbl_random_dice.place(relx=0.5,rely=0.5,anchor=CENTER)
player1_score=0
def player1():
    global player1_score
    random_no=random.randint(1,6)
    lbl_random_dice["text"]="Player 1 Rolls Dice"+str(random_no)
    player1_score=player1_score+random_no
    player1_score["text"]=str(player1_score)
player2_score=0
def player2():
    global player2_score
    random_no2=random.randint(1,6)
    lbl_random_dice["text"]="Player 2 Rolls Dice"+str(random_no2)
    player2_score=player2_score+random_no2
    player2_score["text"]=str(player2_score)
player1_btn=Button(root,image=img,command=player1)
player2_btn=Button(root,image=img,command=player2)
player1_btn.place(relx=0.1,rely=0.6,anchor=CENTER)
player2_btn.place(relx=0.9,rely=0.7,anchor=CENTER)
root.mainloop()
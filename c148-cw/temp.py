from tkinter import *
import random

root = Tk()
root.title("1D Lists")
root.geometry("400x400")


#start writing here
random_number_list=Label(root)
random_number_sorted_list=Label(root)

def randomlist():
    randomlist=random.sample(range(20,60),10)
    random_number_list["text"]="Random Numbers: "+str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"]="Sorted Random Numbers Acending: "+str(randomlist)

btn=Button(root, text="Genarate Random Number",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()
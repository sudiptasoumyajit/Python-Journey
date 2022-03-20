from tkinter import *
import random
root=Tk()
root.title("Lucky Friend Wheel")
root.geometry("400x400")
list1=["Jhon","Rahul","Anita","Merry","Pummy"]
print(list1)
def random_number():
    random_no=random.randint(0, 4)
    print(random_no)
    random_lucky_friend=list1[random_no]
    print("Your Lucky Friend Is:"+random_lucky_friend)
btn1=Button(root)
btn1=Button(root,text="Get A Friend For Free",command=random_number)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()
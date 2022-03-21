from tkinter import *
import random
root=Tk()
root.title("Lucky Friend Wheel")
root.geometry("500x500")
enter_name=Entry(root)
enter_name.place(relx=0.5,rely=0.2,anchor=CENTER)
friend_list=Label(root)
random_number_label=Label(root)
lucky_friend=Label(root)
list1=[]
def addfriend():
    friend_name=enter_name.get()
    list1.append(friend_name)
    friend_list["text"]="List: "+str(list1)
def random_number():
    length=len(list1)
    random_no=random.randint(0,length-1)
    random_number_label["text"]=str(random_no)
    genarated_random_number=list1[random_no]
    lucky_friend["text"]="Your Truth Best Friend Is: "+str(genarated_random_number)
btn=Button(root,text="Add your friends in the list",command=addfriend)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
friend_list.place(relx=0.5,rely=0.4,anchor=CENTER)
btn1=Button(root,text="Get the friend",command=random_number)
btn1.place(relx=0.5,rely=0.6,anchor=CENTER)
random_number_label.place(relx=0.5,rely=0.7,anchor=CENTER)
lucky_friend.place(relx=0.5,rely=0.8,anchor=CENTER)

root.mainloop()
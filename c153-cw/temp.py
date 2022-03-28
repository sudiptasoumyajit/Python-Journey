from tkinter import *
import random
root=Tk()
root.title("3D_Arrays")
root.geometry("400x400")

label=Label(root)
array_3d=[[["1","2","3","4","5","6","7","8","9","0"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["!","@","#","$","%","^","&","*","(",")","[","]",":",";"]]]
print(array_3d[0][2][3])

def new_password():
    random_no_1=random.randint(0,5)
    random_no_2=random.randint(0,1)
    random_no_3=random.randint(0,7)
    
    letter1=str(array_3d[0][0][random_no_1])
    letter2=(array_3d[0][1][random_no_2])
    letter3=(array_3d[0][2][random_no_3])
    
    label["text"]=letter1+""+letter2+""+letter3

btn=Button(root, text="RANDOM PASSCODE:", command=new_password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root=Tk()
root.title("Encapsulation")
root.geometry("800x600")
root.config(bg="orangered")




label_heading=Label(root,text="NACHO TACOS",bg="orangered",fg="white",font=("OCR A Extended",18,"bold"))
label_heading.place(relx=0.05,rely=0.1,anchor=W)
juice=ImageTk.PhotoImage(Image.open("logo.png"))
juice_image=Label(root,image=juice,bg="orangered")
juice_image.place(relx=0.2,rely=0.4,anchor=CENTER)
apple=ImageTk.PhotoImage(Image.open("apple_img.png"))
mango=ImageTk.PhotoImage(Image.open("mango_img.png"))
orange=ImageTk.PhotoImage(Image.open("orange.png"))
furit_image=Label(root,background="orangered")
furit_image.place(relx=0.75,rely=0.8,anchor=CENTER)
label_name=Label(root,text="Select A Fruit",bg="orangered",fg="white",font=("OCR A Extended",15,"bold"))
label_name.place(relx=0.96,rely=0.2,anchor=E)
furit_list=["Apple","Mango","Orange"]
furit_dropdown=ttk.Combobox(root,state="readonly",values=furit_list,justify="right")
furit_dropdown.place(relx=0.95,rely=0.25,anchor=E)
label_quantity=Label(root,text="Enter Quanity",bg="orangered",fg="white",font=("OCR A Extended",15))
label_quantity.place(relx=0.96,rely=0.35,anchor=E)
input_quantity=Entry(root,fg="white",bg="darkblue")
input_quantity.place(relx=0.95,rely=0.4,anchor=E)
label_show_quantity=Label(root,bg="orangered",fg="white",font=("OCR A Extended",15))
label_show_quantity.place(relx=0.96,rely=0.8,anchor=E)




class Juice:
    def __init__(self,fruit_name,quantity):
        self.fruit=fruit_name
        self.quantity=int(quantity)
        self.__cost=250
    def __calculateCost(self):
        total_cost=self.quantity*self.__cost
        label_show_amount['text']="You Have To Pay "+str(total_cost)+" $"
        print("YOU HAVE TO PAY:"+str(total_cost)+" Lakh")
        if(self.fruit=="Apple"):
            calorie=self.quantity*52
            furit_image['image']=apple
        elif(self.fruit=="Mango"):
            calorie=self.quantity*60
            furit_image['image']=mango
        elif(self.fruit=="Orange"):
            calorie=self.quantity*72
            furit_image['image']=orange
        label_show_quantity['text']="x "+str(self.quantity)+" = "+str(calorie)+" calories"
    def getCost(self):
        self.__calculateCost()
def orderJuice():
    fruit=furit_dropdown.get()
    quantity=input_quantity.get()
    obj1=Juice(fruit,quantity)
    obj1.getCost()
btn=Button(root,text="TOTAL",command=orderJuice,bg="darkblue",fg="white",font=("OCR A Extended",15,"bold"))
btn.place(relx=0.95,rely=0.5,anchor=E)
root.mainloop()
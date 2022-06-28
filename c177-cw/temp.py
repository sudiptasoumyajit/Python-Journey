from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root=Tk()
root.title("Encapsulation")
root.geometry("800x600")
class Juice:
    def __init__(self,fruit_name,quantity):
        self.fruit=fruit_name
        self.quantity=int(quantity)
        self.__cost=250
    def __calculateCost(self):
        total_cost=self.quantity*self.__cost
        print("YOU HAVE TO PAY:"+str(total_cost)+" Lakh")
        if(self.fruit=="Apple"):
            calorie=self.quantity*52
        elif(self.fruit=="Mango"):
            calorie=self.quantity*60
        elif(self.fruit=="Orange"):
            calorie=self.quantity*72
        print("x "+str(self.quantity)+" = "+str(calorie)+" calories")
    def getCost(self):
        self.__calculateCost()
def orderJuice():
    fruit="Orange"
    quantity=1000
    obj1=Juice(fruit,quantity)
    obj1.getCost()
btn=Button(root,text="TOTAL",command=orderJuice)
btn.place(relx=0.95,rely=0.5,anchor=E)
root.mainloop()
list=["Burger","Ice Cream"]
class parent():
    def __init__(self):
        print("JOB MENU")
    def menu(type):
        if type=="burger":
            print("You Can Add Following Toppings \n 1. Tomato \n 2. Cabbage \n 3. Cucumber")
            print("You Can Select The Food Type \n 1. Veg \n 2. Non-Veg")
        elif type=="icecream":
            print("You Can Select Any Type \n 1. Cone \n 2. Stick \n 3. Cup")
            print("You Can Select Any Flavour \n 1. Chocolate \n 2. Vanilla \n 3. Strawberry \n 4. Cherry")
        else:
            print("Enter Any type From The List \n"+list)
    def final_amount(type,name):
        if type=="burger" and name=="tomato":
            print("Your Bill \n Burger With Tomato As Add: 100 Rs")
        elif type=="burger" and name=="cabbage":
            print("Your Bill \n Burger With Cabbage As Add: 400 Rs")
        elif type=="burger" and name=="cucumber":
            print("Your Bill \n Burger With Cucumber As Add: 50 Rs")
        elif type=="icecream" and name=="chocolate":
            print("Your Bill \n Ice Cream With Chocolate Flavour: 50 Rs")
        elif type=="icecream" and name=="vanilla":
            print("Your Bill \n Ice Cream With Vanilla Flavour: 20 Rs")
        elif type=="icecream" and name=="strawberry":
            print("Your Bill \n Ice Cream With Strawberry Flavour: 200 Rs")
        elif type=="icecream" and name=="cheery":
            print("Your Bill \n Ice Cream With Cheery Flavour: 10 Rs")
        else:
            print("Select A name Please")
class child1(parent):
    def __init__(self,type):
        self.new_type=type
    def get_menu(self):
        parent.menu(self.new_type)
class child2(parent):
    def __init__(self,type,name):
        self.new_type=type
        self.add=name
    def added(self):
        parent.final_amount(self.new_type,self.add)
pick1=child1("burger")
pick1.get_menu()
pick2=child2("burger","tomato")
pick2.added()
pick3=child1("icecream")
pick3.get_menu()
pick4=child2("icecream","chocolate")
pick4.added()
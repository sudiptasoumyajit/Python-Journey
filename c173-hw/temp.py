from tkinter import *
root=Tk()
root.title("Connecting Jobs")
root.geometry("600x600")
#CODEs
label1=Label(root,text="NaN")
label1.pack()
button1=Button(root,text="Show Hospital Alloted",command="hireHospital")
button1.pack()
label2=Label(root,text="NaN")
label2.pack()
button2=Button(root,text="Show IT Company Alloted",command="hireIT")
button2.pack()
label3=Label(root,text="NaN")
label3.pack()
button3=Button(root,text="Show Chemical Factory Alloted",command="hireChemical")
button3.pack()
class parent:
    def __init__(self):
        print("Jobs")
    def offer(type):
        if type=="Hospital":
            label1["text"]="Select Your Company: Appolo, Ceta, MRI"
        elif type=="IT Engeneer":
            label2["text"]="Select Your Company: ICode, Apple, Microsoft"
        elif type=="Chemical":
            label3["text"]="Select Your Company: IFFCO, Abbot, CiNi"
        else:
            print("Select")
    def offertype(type,item):
        if(type=="Hospital" and name=="AppoloDoc"):
            label1["text"]="\n Applo Hiers You As Doctor"
        elif(type=="Hospital" and name=="AppoloSur"):
            label1["text"]="\n Applo Hiers You As Surgeon"
        elif(type=="Hospital" and name=="AppoloNur"):
            label1["text"]="\n Applo Hiers You As Nurse"
        elif(type=="Hospital" and name=="CetaDoc"):
            label1["text"]="\n Ceta Hiers You As Doctor"
        elif(type=="Hospital" and name=="CetaSur"):
            label1["text"]="\n Ceta Hiers You As Surgeon"
        elif(type=="Hospital" and name=="CetaNur"):
            label1["text"]="\n Ceta Hiers You As Nurse"
        elif(type=="Hospital" and name=="MRIDoc"):
            label1["text"]="\n MRI .Inc Hiers You As Doctor"
        elif(type=="Hospital" and name=="MRISur"):
            label1["text"]="\n MRI .Inc Hiers You As Surgeon"
        elif(type=="Hospital" and name=="MRINur"):
            label1["text"]="\n MRI .Inc Hiers You As Nurse"
        elif(type=="IT Engeneer" and name=="ICodeDev"):
            label2["text"]="\n ICode Has Hired You As Developer"
        elif(type=="IT Engeneer" and name=="ICodeBug"):
            label2["text"]="\n ICode Has Hired You As Bug Fixer"
        elif(type=="IT Engeneer" and name=="MicrosoftDev"):
            label2["text"]="\n Microsoft Has Hired You As Developer"
        elif(type=="IT Engeneer" and name=="MicrosoftBug"):
            label2["text"]="\n Microsoft Has Hired You As Bug Fixer"
        elif(type=="IT Engeneer" and name=="AppleDev"):
            label2["text"]="\n Apple Has Hired You As Developer"
        elif(type=="IT Engeneer" and name=="AppleBug"):
            label2["text"]="\n Apple Has Hired You As Bug Fixer"
        elif(type=="Chemical" and name=="IFFCOWork"):
            label2["text"]="\n IIFFCO Has Hired You As Workman"
        elif(type=="Chemical" and name=="AbbotWork"):
            label2["text"]="\n Abbot Has Hired You As Workman"
        elif(type=="Chemical" and name=="CiNiWork"):
            label2["text"]="\n CiNi Has Hired You As Workman"
        else:
            print("Select")
class jobType(parent):
    def __init__(self,type):
        self.new_type=type
    def get_menu(self):
        parent.menu(self.new_type)
class jobCategory(parent):
    def __init__(self,type,item):
        self.new_type=type
        self.add=name
    def added(self):
        parent.result(self.new_type,self.add)
def  hireHospital():
    name1=jobType("Hospital")
    name1.result()
    name2=jobCategory("Hospital","MRINur")
    name2.result()
label1["label"]=hireHospital()
def  hireIT():
    name1=jobType("IT Engeneer")
    name1.result()
    name2=jobCategory("IT Engeneer","AppleBug")
    name2.result()
label2["label"]=hireIT()
def  hireChemical():
    name1=jobType("Chemical")
    name1.result()
    name2=jobCategory("Chemical","CiNiWork")
    name2.result()
label3["label"]=hireChemical()
lbl1=Label(root,text=hireHospital)
lbl1.pack()
lbl2=Label(root,text=hireIT)
lbl2.pack
lbl3=Label(root,text=hireChemical)
lbl3.pack()
root.mainloop()
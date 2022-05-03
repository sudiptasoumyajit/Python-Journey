from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("COVID Check")
root.geometry("600x350")

question1_radioButton=StringVar(value="0")
Question1=Label(root,text="Do You Have Fever, Vomit, Cought / Dry Cough And Difficult In Breathing ?")
Question1.pack()
question1_r1=Radiobutton(root,text="Yes",variable=question1_radioButton,value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root,text="Little",variable=question1_radioButton,value="little")
question1_r2.pack()
question1_r3=Radiobutton(root,text="No",variable=question1_radioButton,value="no")
question1_r3.pack()

question2_radioButton=StringVar(value="0")
Question2=Label(root,text="Do You Have Bleeding In Cough, Not Proper Vision / Hearing Sense?")
Question2.pack()
question2_r1=Radiobutton(root,text="Yes",variable=question2_radioButton,value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root,text="Little",variable=question2_radioButton,value="little")
question2_r2.pack()
question2_r3=Radiobutton(root,text="No",variable=question2_radioButton,value="no")
question2_r3.pack()

question3_radioButton=StringVar(value="0")
Question3=Label(root,text="Do You Felling Dizzy, Headchae, Dehydration, Pain, Extreme Coldness")
Question3.pack()
question3_r1=Radiobutton(root,text="Yes",variable=question3_radioButton,value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root,text="Little",variable=question3_radioButton,value="little")
question3_r2.pack()
question3_r3=Radiobutton(root,text="No",variable=question3_radioButton,value="no")
question3_r3.pack()

def fever_score():
    score=0
    if question1_radioButton.get()=="yes":
        score=score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score=score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score=score+20
        print(score)
    if score <= 20:
        messagebox.showinfo("Alert","You must quarrentime yourself and should consult a doctor for medicine.!!!!")
    elif score > 20 and score <= 40:
        messagebox.showinfo("Warning","Stay Safe, Stay Home :)")
    else:
        messagebox.showinfo("Danger","You Must Immedieatly Advice A Doctor And Must Be In The Admit Hospital!!!!!!!")

btn=Button(root,text="Show Results God",command=fever_score)
btn.pack()

root.mainloop()
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root=Tk()
root.title("PlanetWiki")
root.geometry("900x600")
root.configure(background="black")

planets=["Mercury","Venus","Earth"]
selectedval=StringVar()

dropdown=ttk.Combobox(root,value=planets,textvariable=selectedval)
dropdown.place(relx=0.5,rely=0.1,anchor=CENTER)

Mercury=ImageTk.PhotoImage(Image.open("mercury.jpg"))
Venus=ImageTk.PhotoImage(Image.open("venus.jpg"))
Earth=ImageTk.PhotoImage(Image.open("earth.jpg"))

label_planet=Label(root,text="Planet: ",bg="black",fg="white",font=("Work Sans",20,"bold"))
label_planet.place(relx=0.2,rely=0.1,anchor=CENTER)

label_planet_name=Label(root,text="__Unknown Name__",fg="white",bg="black",font=("Work Sans",20,"bold"))
label_planet_name.place(relx=0.5,rely=0.26,anchor=CENTER)

label_planet_image=Label(root,bg="darkblue",highlightthickness=4,borderwidth=2,relief=SOLID)
label_planet_image.place(relx=0.5,rely=0.5,anchor=CENTER)

label_planet_gravity_radius=Label(root,text="__Unknown Radius__",fg="white",bg="black",font=("Work Sans",20,"bold"))
label_planet_gravity_radius.place(relx=0.5,rely=0.8,anchor=CENTER)

label_planet_info=Label(root,text="__Unknown Info__",fg="white",bg="black",font=("Work Sans",20,"bold"),wraplength=500)
label_planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)

def PlanetInfo():
    print("BRO !!! ITS Just A Prank")
    planet=selectedval.get()
    if planet=="Mercury":
        label_planet_name['text']="Mercury"
        label_planet_image['image']=Mercury
        label_planet_gravity_radius['text']="Gravity: 3.7 m/s2 \n Radius: 2,439.7 KM"
        label_planet_info['text']="The smallest and closest planet to the Sun in the Solar System."
    elif planet=="Venus":
        label_planet_name['text']="Venus"
        label_planet_image['image']=Venus
        label_planet_gravity_radius['text']="Gravity: 8.87 m/s2 \n Radius: 6,501 KM"
        label_planet_info['text']="The second planet from the Sun and sixth in the solar system in size and mass."
    elif planet=="Earth":
        label_planet_name['text']="Earth"
        label_planet_image['image']=Earth
        label_planet_gravity_radius['text']="Gravity: 9.807 m/s2 \n Radius: 6,371 KM"
        label_planet_info['text']="The third planet from the Sun and the only astronomical object known to harbor life."

btn=Button(root,text="Search >",fg="white",bg="black",font=("Work Sans",20,"bold"),command=PlanetInfo)
btn.place(relx=0.5,rely=0.18,anchor=CENTER)

root.mainloop()
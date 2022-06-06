from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time 

root=Tk()
root.title("USA And India Clock")
root.geometry("600x450")

clock_image=ImageTk.PhotoImage(Image.open("clock.jpg"))

#---------------------------------------------------------------------INDIA

india_label=Label(root,text="IST India Standerd Time: Kolkata")
india_label.place(relx=0.2,rely=0.05,anchor=CENTER)

india_clock=Label(root)
india_clock["image"]=clock_image
india_clock.place(relx=0.2,rely=0.35,anchor=CENTER)

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="TIME: "+current_time
        india_time.after(200,self.times)

india_time=Label(root,text="Detecing")
india_time.place(relx=0.2,rely=0.65,anchor=CENTER)

obj_india=India()

india_btn=Button(root,text="Refresh If Take Long Time",command=obj_india.times)
india_btn.place(relx=0.2,rely=0.8,anchor=CENTER)

#---------------------------------------------------------------------USA

usa_label=Label(root,text="USA Central Time")
usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)

usa_clock=Label(root)
usa_clock["image"]=clock_image
usa_clock.place(relx=0.7,rely=0.35,anchor=CENTER)

class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="TIME: "+current_time
        usa_time.after(200,self.times)

obj_usa=USA()

usa_btn=Button(root,text="Refresh If Take Long Time",command=obj_usa.times)
usa_btn.place(relx=0.7,rely=0.8,anchor=CENTER)

usa_time=Label(root,text="Detecing")
usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)

root.mainloop()
from tkinter import *
from PIL import ImageTk,Image
from datetime import datetime
import pytz
import time 

root=Tk()
root.title("USA And India Clock")
root.geometry("600x450")
#---------------------------------------------------------------------INDIA

india_label=Label(root,text="IST India Standerd Time: Kolkata")
india_label.pack()

class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="TIME: "+current_time
        india_time.after(200,self.times)

india_time=Label(root,text="Detecing")
india_time.pack()

obj_india=India()

india_btn=Button(root,text="Refresh If Take Long Time",command=obj_india.times)
india_btn.pack()

#---------------------------------------------------------------------USA

usa_label=Label(root,text="USA Central Time")
usa_label.pack()

class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="TIME: "+current_time
        usa_time.after(200,self.times)

obj_usa=USA()

usa_btn=Button(root,text="Refresh If Take Long Time",command=obj_usa.times)
usa_btn..pack()

usa_time=Label(root,text="Detecing")
usa_time..pack()

#---------------------------------------------------------------------AUSTRALIA

australia_label=Label(root,text="USA Central Time")
australia_label.pack()

class australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        australia_time["text"]="TIME: "+current_time
        australia_time.after(200,self.times)

obj_australia=australia()

australia_btn=Button(root,text="Refresh If Take Long Time",command=obj_australia.times)
australia_btn..pack()

australia_time=Label(root,text="Detecing")
australia_time..pack()

root.mainloop()

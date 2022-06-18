from tkinter import *
import psutil as p
import matplotlib .pyplot as plt
root=Tk()
root.geometry("600x500")
app_name_list=[]
app_name_percentage_list=[]
count=0
def code():
    global count
    global app_name_list
    global app_name_percentage_list
    for process in p.process_iter():
        count=count+1
        if count<=10:
            name=process.name()
            cpu_usage=p.cpu_percent()
            lbl['text']="name:",name,"--cpu-usage:",cpu_usage,"\n"
            print("name:",name,"--cpu-usage:",cpu_usage,"\n")
            app_name_list.append(name)
            app_name_percentage_list.append(cpu_usage)
lbl=Label(root,text="")
btn=Button(root,text="Show Usage",command=code)
lbl.pack()
btn.pack()
root.mainloop()
plt.figure(figsize=(15,7))
plt.xlabel("Task Manager")
plt.ylabel("RAM / Stroage Usage")
plt.bar(app_name_list,app_name_percentage_list,width=0.3,color=("blue","blue","blue","blue","blue","blue","blue","blue","blue","blue"))
plt.show()
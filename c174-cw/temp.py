import matplotlib .pyplot as plt
import psutil as p
app_name_list=[]
app_name_percentage_list=[]
count=0
for process in p.process_iter():
    count=count+1
    if count<=5:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("name:",name,"--cpu-usage:",cpu_usage)
        app_name_list.append(name)
        app_name_percentage_list.append(cpu_usage)
plt.figure(figsize=(15,7))
plt.xlabel("Task Manager")
plt.ylabel("RAM / Stroage Usage")
plt.bar(app_name_list,app_name_percentage_list,width=0.3,color=("blue","blue","blue","blue","blue"))
plt.show()
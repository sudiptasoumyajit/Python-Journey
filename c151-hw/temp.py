from tkinter import *
root=Tk()
root.title("Sales")
root.geometry("500x500")
month=("Jan","Feb","Mar","Apr","May","Jun","July","Aug","Sept",'Oct',"Nov","Dec")
profits=(20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)
max_profit=max(profits)
max_profit_index=profits.index(max_profit)
print(max_profit_index)
max_profit_month=month[max_profit_index]
print("The Max. Profit Of "+str(max_profit)+" Was Recorded In Month Of "+str(max_profit_month)+".")
min_profit=min(profits)
min_profit_index=profits.index(min_profit)
print(min_profit_index)
min_profit_month=month[min_profit_index]
print("The Min. Profit Of "+str(min_profit)+" Was Recorded In Month Of "+str(min_profit_month)+".")
lbl_list=Label(root)
lbl_max=Label(root)
lbl_min=Label(root)
def show_result():
    lbl_list["text"]=max_profit_index
    lbl_max["text"]=max_profit_month
    lbl_min["text"]=min_profit_month
btn_show=Button(root,text="Click To Show Me",command=show_result)
lbl_list.place(relx=0.5,rely=0.5,anchor=CENTER)
lbl_min.place(relx=0.5,rely=0.6,anchor=CENTER)
lbl_max.place(relx=0.5,rely=0.7,anchor=CENTER)
btn_show.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()
from tkinter import *
root=Tk()
root.title("Multidimensonal Array")
root.geometry("500x500")

label=Label(root)

array_1d=["jhon","marry","thomas"]
print(array_1d[0])

array_2d=[["jhon","a"],["marry","b"],["thomas","c"]]
print(array_2d[0][1])

array_3d=[[["jhon","a","scinctist"],["marry","b","mathematician"],["thomas","c","gamer"]]]
print(array_3d[0][0][2])

def report():
    label["text"]=array_3d[0][1][0]+" gets grade "+array_3d[0][1][1]+" and is doining "+array_3d[0][1][2]

btn=Button(root,text="Results",command=report)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()
from tkinter import *

root = Tk()
root.geometry("500x250")

label_file_name = Label(root, text="Name")
label_file_name.place(relx=0.3,rely=0.1,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.1, anchor= CENTER)

my_text= Text(root,height=5,width=40)
my_text.place(relx=0.5,rely=0.4,anchor= CENTER)


# Define clearInputFeild() function
def clearInputFeild():
    input_file_name.delete(0,END)

# Define clearTextArea() function
def clearTextArea():
    my_text.delete(1.0,END)

# Define addData() function
def addData():
    input_file_name.insert(END,"Hello World")


open_button=Button(root,text="Clear Input field", command=clearInputFeild)
open_button.place(relx=0.25,rely=0.7,anchor=CENTER)
save_button=Button(root, text="Clear Textarea", command=clearTextArea)
save_button.place(relx=0.455,rely=0.7,anchor= CENTER)
exit_button=Button(root, text="Add data to input feild", command=addData)
exit_button.place(relx=0.7,rely=0.7,anchor= CENTER)

root.mainloop()


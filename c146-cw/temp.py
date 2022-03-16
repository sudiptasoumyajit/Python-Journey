from tkinter import *
root = Tk()
root.title("Fibonacci | Sample")
root.geometry("400x400")
label_series = Label(root, text="Fibonacci Series: ")
label_flower = Label(root)
label_spiral = Label(root)
def Fibonacci():
    num = 10
    first_num = 0
    second_num = 1
    sum = 0
    counter = 1
    while(counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter+1
        first_num = second_num
        second_num = sum
        sum = first_num + second_num
        label_flower["text"] = "Flower Is Fully Blommed"
        label_spiral["text"] = "Spiral In Right Direction Are " +str(first_num)+ "\n Spiral In Left Direction Are " + str(second_num)+ "\n Total Spirals Are " + str(sum)
btn = Button(root, text="Show The Text", command = Fibonacci)
btn.pack()
label_series.pack()
label_spiral.pack()
label_flower.pack()
root.mainloop()
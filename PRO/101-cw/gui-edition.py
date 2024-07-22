from tkinter import *
import time
import threading

# Function to run the countdown timer
def countdown_timer(seconds):
    while seconds > 0:
        minutes = int(seconds / 60)
        secs = int(seconds % 60)
        timer = f'{minutes:02d} : {secs:02d}'
        countLbl.config(text=timer)
        root.update()
        time.sleep(1)
        seconds -= 1
    
    countLbl.config(text='Times up!!')

# Function to start the timer in a new thread
def start_timer():
    try:
        seconds = int(entry.get())
        # Start countdown timer in a separate thread
        threading.Thread(target=countdown_timer, args=(seconds,)).start()
    except ValueError:
        countLbl.config(text='Invalid input!')

# Initialize the GUI window
root = Tk()
root.title('Countdown')
root.geometry('400x400')
root.configure(background='darkblue')

# Label to display the countdown timer
countLbl = Label(root, anchor='center', text='00 : 00', foreground='lightblue', background='darkblue', font=['Poppins', 80, 'bold'])
countLbl.pack(pady=20)

# Entry widget to input the number of seconds
entry = Entry(root, font=['Poppins', 20, 'bold'], justify='center')
entry.pack(pady=10)

# Button to start the countdown timer
startBtn = Button(root, text='Start Timer', command=start_timer, font=['Poppins', 20, 'bold'], fg='darkblue', bg='lightblue', relief='flat')
startBtn.pack(pady=20)

# Run the GUI loop
root.mainloop()

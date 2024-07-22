import time

seconds = input('Enter the time in number of seconds:   ')

def countdown_timer(seconds):

    while seconds > 0:                      #Changes: Added the while loop to countdown
        minutes = int(seconds / 60)
        secs = int(seconds % 60)

        timer = f'{minutes} : {secs}'
        print(timer, end='\r')              #Changes: Added To Remove The List
        time.sleep(1)

        seconds -= 1
    
    print('Times up!!')

countdown_timer(int(seconds))
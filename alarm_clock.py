# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
from playsound import playsound
import time


CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed=0
    
    print(CLEAR)
    
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed +=1
        
        time_left= seconds - time_elapsed
        minutes_left = time_left//60
        seconds_left= time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in :{minutes_left:02d}:{seconds_left:02d}")
        
    playsound("Alarm.mp3")
 
min=int(input("How many min to wait : "))
sec=int(input("How many sec to wait : "))
total_time=min*60 + sec     
alarm(total_time)
        
        
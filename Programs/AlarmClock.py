import winsound as WS
import time 
import os

def Hour():
    while True:
        Hour = int(input("Hour : "))
        if(Hour < 1 or Hour > 24):
            print("Invalid Hour")
            continue
        return(Hour)

def Min():
    while True:
        Min = int(input("Min : "))
        if(Min < 0 or Min > 60):
            print("Invalid Min")
            continue
        return(Min)
    
def AlarmTime():
    AlarmHour = Hour()
    AlarmMin = Min()
    
    while True:
        os.system("cls")
        CurrentHour = int(time.strftime("%H"))
        CurrentMin = int(time.strftime("%M"))
        S = int(time.strftime("%S"))

        print(f"Alarm = {AlarmHour}:{AlarmMin}\n")
        print(f"Time = {CurrentHour}:{CurrentMin}:{S}")
        
        if((AlarmHour == CurrentHour) and (AlarmMin == CurrentMin)):
            for i in range(10):
                WS.MessageBeep()
                time.sleep(1)
            break
        time.sleep(0.5)
        
if __name__ == "__main__":
    AlarmTime()
    

import time
from playsound import playsound
from datetime import datetime

#set the alarm here
alarmtime = "14:25"

while True:
    lcltime = datetime.now().strftime('%H:%M')

    if lcltime == alarmtime:
        #set the music here
        playsound("sound.mp3")
        break
    else:
        print ("Not yet")
        time.sleep(10)
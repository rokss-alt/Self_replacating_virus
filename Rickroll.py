
from datetime import datetime
import time
import webbrowser
import subprocess
import random
import os

Time_stop = "09:30:00"

while True:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    if current_time == Time_stop:
        while True:
        sites = random.choice(['youtube.com/watch?v=dQw4w9WgXcQ'])
        visit = "http://{}".format(sites)
        webbrowser.open(visit)
        seconds = random.randrange(5, 10)
        time.sleep(seconds)
        break
    elif current_time >= Time_stop:
        break
    
input()

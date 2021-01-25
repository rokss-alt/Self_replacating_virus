
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
        os.system('cmd /k" python Rick_roll.py')
    elif current_time >= Time_stop:
        break
    
input()


from datetime import datetime
import time
import webbrowser
import subprocess
import random
import os

Time_stop = input("When to stop:")

while True:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    if current_time == Time_stop:
        while True:
            print("HHHHHHHHHHHHHHHHEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLOOOOOOOOOOOOO")
            break
    elif current_time >= Time_stop:
        break
    
input()

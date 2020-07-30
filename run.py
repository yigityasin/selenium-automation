from subprocess import Popen

processes = []
f = open("input.txt", "r")
lines = f.readlines()
for line in lines:
    cmd = "python3 scraper.py '"+line.strip()+"'"
    processes.append(Popen(cmd, shell=True))

for i in range(len(lines)):
    processes[i].wait()

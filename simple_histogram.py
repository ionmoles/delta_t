import numpy as np
import matplotlib.pyplot as plt
f = file('delta_t.csv','r')

delta_t = []
read = False
for line in f:
    if line[0]==',':
        break
    if read:
        t,a,b,c,d = line.split(',')
        if int(t) < 1800000/3: #10 minutes
            delta_t.append(int(t)/60000)
    if line[0]=='E':
        read = True

plt.hist(delta_t)
plt.xlabel("Time in minutes between loading question page and opening solution")
plt.ylabel("Number of events")
plt.savefig("delta_t.png")   

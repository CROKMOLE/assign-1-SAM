import math

import matplotlib.pyplot as plt
import random

ther_mean = 0.5
ther_def = 1/12


ug = []
for i in range(500):
    ug.append(random.random())

print(ug)

meant = sum(ug) / 500
ud = []
for x in ug:
    ud.append(meant - x)    
print(f"exponential: {meant}   theoretical: {ther_mean}")



plt.hist(ug)
plt.show()
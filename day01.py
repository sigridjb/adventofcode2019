import pandas as pd
import numpy as np

d = pd.read_csv("input",header=None)
d["fuel1"] = np.floor(d/3)-2
print("Day 1 - part 1: "+str(int(d.fuel1.sum())))

def getfuel(val):
    fuelneeded = 0
    while (np.floor(val/3)-2)>0:
        fuelneeded += np.floor(val/3)-2
        val = np.floor(val/3)-2
    return(fuelneeded)

d["fuel2"] = d[0].apply(lambda x: getfuel(x))
print("Day 1 - part 2: "+str(int(d.fuel2.sum())))
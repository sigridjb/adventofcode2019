import pandas as pd
import numpy as np

d = pd.read_csv("input",header=None)
p1 = d.loc[0].values
p2 = d.loc[1].values

def getWirePath(turns):
    horiz = [0]
    verti = [0]

    for turn in turns:
        d = turn[0]
        l = int(turn[1:])
        h = horiz[-1]
        v = verti[-1]
        if d=="R":
            horiz = horiz+list(range(h+1,h+1+l))
            verti = verti+[v]*l
        elif d=="L":
            horiz = horiz+list(range(h-1,h-1-l,-1))
            verti = verti+[v]*l
        elif d=="U":
            horiz = horiz+[h]*l
            verti = verti+list(range(v+1,v+1+l))
        else:
            horiz = horiz+[h]*l
            verti = verti+list(range(v-1,v-1-l,-1))
    return(np.array(horiz[1:])*1e6+np.array(verti[1:]))

#part 1
wpath1 = getWirePath(p1)
wpath2 = getWirePath(p2)
common = np.intersect1d(wpath1, wpath2)
horiz = np.round(common/1e6)
verti = common-horiz*1e6
print("Day 3 - part 1: " + str(int(min(abs(horiz)+abs(verti)))))

#part 2
minsteps = 1e5
for i in range(len(common)):
    minsteps = min(np.where(wpath1==common[i])[0][0] + np.where(wpath2==common[i])[0][0] + 2, minsteps)
print("Day 3 - part 2: " + str(minsteps))
import pandas as pd

#part 1
d = pd.read_csv("input",header=None).values[0]
d[1] = 12
d[2] = 2
i = 0
while not d[i]==99:
    d[d[i+3]] = d[d[i+1]] + d[d[i+2]] if d[i]==1 else d[d[i+1]] * d[d[i+2]]
    i+=4
print("Day 2 - part 1: "+str(d[0]))

#part 2
orig = pd.read_csv("input",header=None).values[0]
outval = 19690720
for noun in range(100):
    for verb in range(100):
        if verb>=noun:
            d = orig.copy()
            d[1] = noun
            d[2] = verb
            i=0
            while not d[i]==99:
                d[d[i+3]] = d[d[i+1]] + d[d[i+2]] if d[i]==1 else d[d[i+1]] * d[d[i+2]]
                i+=4
            if d[0]==outval:
                print("Day 2 - part 2: "+str(100 * noun + verb))
                break
    if d[0]==outval:
        break
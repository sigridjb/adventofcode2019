import pandas as pd
import numpy as np

inp = np.array(list(range(245318,765747+1)))
digits = pd.DataFrame(columns=range(6))
for i in range(6):
    digits[5-i] = inp%10
    inp //= 10

#part 1
digits["decreases"] = 0
digits["adjacentEquals"] = 0
for i in range(1,6):
    digits["decreases"]+=((digits[i]-digits[i-1])<0).astype(int)
    digits["adjacentEquals"]+=((digits[i]-digits[i-1])==0).astype(int)

digits = digits[digits["decreases"]==0]
digits = digits[digits["adjacentEquals"]>0]

print("Day 4 - part 1: " + str(digits.shape[0]))

#part 2
last5  = digits[[1,2,3,4,5]]
first5 = digits[[0,1,2,3,4]]
last5.columns = first5.columns
diffs = (last5-first5)
digits["trues"] = True
diffs["single0exists"] = False
for i in range(5):
    is0 = (diffs[i]==0).astype(int)
    no0left  = (digits.trues if i==0 else diffs[i-1]>0).astype(int)
    no0right = (digits.trues if i==4 else diffs[i+1]>0).astype(int)
    haveSingle0 = (is0 + no0left + no0right)==3
    diffs["single0exists"]+= haveSingle0.astype(int)

print("Day 4 - part 2: " + str(diffs[diffs.single0exists>0].shape[0]))

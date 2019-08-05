import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv('Data2.csv'))
#seperate the concept
concepts = np.array(data.iloc[:,:-1])
print(concepts)
# seperate the target
target = np.array(data.iloc[:,-1])
print(target)
# copy first instance to specfic hypothesis
spec_h=concepts[0]
print(spec_h)
#intialise general hypothesis
gen_h = [["?" for i in range(len(spec_h))] for i in range(len(spec_h))]
print(gen_h)
   #check if positive training example
for i, h in enumerate(concepts):
    if target[i] == "P":
        for x in range(len(spec_h)):
            if h[x]!= spec_h[x]:
                spec_h[x] ='?'
                gen_h[x][x] ='?'
            #print(spec_h)
    #print(spec_h)
    if target[i] == "N":
        for x in range(len(spec_h)):
            if h[x]!= spec_h[x]:
                gen_h[x][x] = spec_h[x]
            else:
                gen_h[x][x] = '?'
    print(" Steps No",i+1)
    print("Specific Boundary")
    print(spec_h)
    print("Generic Boundary")
    print(gen_h)


indexes = [i for i, val in enumerate(gen_h) if val == ['?', '?', '?', '?', '?', '?']]
for i in indexes:
    gen_h.remove(['?', '?', '?', '?', '?', '?'])
print("Final Solution")
print(spec_h)
print(gen_h)

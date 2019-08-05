#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[104]:


df = pd.DataFrame(pd.read_csv('Data2.csv'))
df


# In[105]:


attr = list(df.columns)
class_label = str(attr[len(attr)-1])
class_index = len(attr)-1


# In[106]:


#Specific and General Hypothesis to be initialised

S0 = [ '%' for i in range(len(attr)-1) ]
temp0 = [ '?' for i in range(len(attr)-1) ]
G0 = []
G0.append(temp0)

#specify lists to hold updated versions of G and S
G = []
S = []
G.append(G0)
S.append(S0)
print(G)


# In[107]:


#function to check for consistency of S and G hypotheses when S gets updated, it is used to eliminate candidates in latest General hypothesis that is inconsistent with training set instance

def consistent():
    last_G = G[-1]
    #print(last_G)
    last_S = S[-1]
    #print(last_S)
    i = 0
    if len(last_G) > 1:
        for g_hyp in last_G:
            print("YOOOO G_HYP")
            print(g_hyp)
            for i in range(len(g_hyp)):
                if g_hyp[i]!='?' and g_hyp[i] != last_S[i]:
                    G[-1].remove(g_hyp)



# In[ ]:


for index, row in df.iterrows():
    print(index,S[index])
    print(index,G[index])
    row = list(row)
    if row[class_index] == 'P':
        #if its first training example, comparing with % attr and updating S
        if S[len(S)-1][0] == '%':
            S.append(row[:-1])
            G.append(G[-1])
            #print(G)

        else:
            for i in range(len(row)-1):
                if S[-1][i] != row[i]:
                    row[i] = '?'
            S.append(row[:-1])
            G.append(G[-1])
            #print(G)
            #check for consistency
            consistent()

    elif row[class_index] == 'N':
        print("For negative instance entered")
        i = 0
        tmp1 = []
        tmp2 = temp0
        for i in range(len(row)-1):
            #tmp2 = temp0
            if row[i] != S[-1][i] and S[-1][i] != '?':
                tmp2[i] = S[-1][i]
                tmp1.append(tmp2)
                tmp2 = temp0
                break
                #print(tmp1)
            elif S[-1][i] == '?':
                #print(tmp1)
                print("CAME HERE ALSO")
                tmp2 = temp0
                break
        #tmp1.append(tmp2)
        S.append(S[-1])
        G.append(tmp1)
        #print("For negative instance")
        #print(G)



# In[ ]:

'''
#print out S and G hypothesis boundaries at each step of algo

print("BOUNDARIES OF Specfic and General Hypothesis at each step :")
for i in range(0,len(S)):
    print("S"+str(i)+":")
    print(S[i])
    print("G"+str(i)+":")
    print(G[i])

'''
# In[ ]:

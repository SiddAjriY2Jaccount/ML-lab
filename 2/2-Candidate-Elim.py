#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.DataFrame(pd.read_csv('Data2.csv'))
#df

attr = list(df.columns)
class_label = str(attr[len(attr)-1])
class_index = len(attr)-1

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

#function to check for consistency of S and G hypotheses when S gets updated, it is used to eliminate candidates in latest General hypothesis that is inconsistent with training set instance

def consistent():
    global S
    global G
    last_G = G[-1]
    #print(last_G)
    last_S = S[-1]
    #print(last_S)
    i = 0
    print(last_G)
    if len(last_G) > 1:
        print(last_G)
        for g_hyp in last_G:
            #print(g_hyp)
            for i in range(len(g_hyp)):
                if g_hyp[i]!='?' and g_hyp[i] != last_S[i]:
                    #print("*************** yo check **************")
                    #print(g_hyp)
                    #print(" inside G[-1] ")
                    #print(G[-1])
                    count = 0
                    for index_1, inner_list in enumerate(G[-1]):
                        for c in range(len(inner_list)):
                            if inner_list[c] == g_hyp[c]:
                                count+=1
                        if count == len(attr)-1:
                            G[-1].pop(index_1)
                        else:
                            count = 0
                    #print(G)

print("\nBOUNDARIES OF Specfic and General Hypothesis at each step :\n")
for index, row in df.iterrows():
    print('S',index,S[index])
    print('G',index,G[index])
    row = list(row)
    if row[class_index] == 'P':
        #if its first training example, comparing with % attr and updating S
        if S[len(S)-1][0] == '%':
            S.append(row[:-1])
            G.append(G[-1])

        else:
            for i in range(len(row)-1):
                if S[-1][i] != row[i]:
                    row[i] = '?'
            S.append(row[:-1])
            G.append(G[-1])
            #check for consistency with generic boundary
            consistent()

    elif row[class_index] == 'N':
        row = row[:len(row)-1]
        print("For negative instance entered")
        i = 0
        tmp1 = []
        for i in range(len(row)):
            tmp2 = [ '?' for i in range(len(attr)-1) ]
            #print("----------0000000000000000---------------")
            #print(tmp2)
            #print("--------------------------")
            #print(row)
            #print("--------------------------")
            #print(S[-1][i])
            if row[i] != S[-1][i] and S[-1][i] != '?':
                tmp2[i] = S[-1][i]
                print(tmp2)
                tmp1.append(tmp2)
                print(tmp1)
                continue
            elif S[-1][i] == '?':
                #print("CAME HERE ALSO")
                continue
        S.append(S[-1])
        G.append(tmp1)
    
print('S',index+1,':',S[index])
print('G',index+1,':',G[index])
#printing final boundaries
print("\n\nFINAL Specific and Generic Boundaries\n\n")
print('S boundary : ',S[index])
print('G boundary : ',G[index])

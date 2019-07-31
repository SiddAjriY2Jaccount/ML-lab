import pandas as pd

#initial hypothesis should be null sets
init_hypothesis = ['%','%','%','%','%','%','%']
df = pd.read_csv('Dataset-lab-1.csv')
attr = list(df.columns)

#to obtain class_attribute
class_attr = str(attr[len(attr)-1])

index_class = len(attr)-1

#get first row in dataset
#first_instance = list(df.iloc[0,:]) -> gets first row
first_instance = []

print("Steps of Hypotheses:")
print(init_hypothesis)

for index, row in df.iterrows():
    row = list(row)
    if row[index_class]=='yes':
        if len(first_instance)==0: #checking if first_instance initialised
            first_instance = row
            hypothesis = first_instance
            #initially, first instance taken as hypothesis
            print(hypothesis[0:len(hypothesis)-1])
            max_spec_hypothesis = hypothesis[0:len(hypothesis)-1]

        else:
            for i in range(len(hypothesis)):
                if hypothesis[i]!=row[i]:
                    hypothesis[i]='?'
            print(hypothesis[0:len(hypothesis)-1])
            max_spec_hypothesis = hypothesis[0:len(hypothesis)-1]

print("")
print("Maximally specific hypothesis:")
print(max_spec_hypothesis)

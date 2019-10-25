import pandas as pd
import sys
import math

df = pd.DataFrame(pd.read_csv('Data3.csv'))

attr = list(df.columns)
class_label = str(attr[len(attr)-1])
class_index = len(attr)-1

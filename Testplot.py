import numpy as np
import matplotlib.pyplot as plt

import csv
data=[]
with open(r"C:\Users\John\Documents\Kristi\test.csv",'rb') as fIn:
    reader=csv.reader(fIn)
    for line in reader:
        data.append(line)
        
data.remove(data[0])
# DATA SANITIZATION
# For each sublist in list
    #for each element in sublist
        # if first element, convert to datetime64
        # else convert element to float

# NUMPY ARRAYS
# List ot lists to numpy array

# PLOT DATA
# Plot desired data


print data

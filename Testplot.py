import numpy as np
import matplotlib.pyplot as plt

import csv

with open(r"C:\Users\John\Documents\Kristi\test.csv",'rb') as fIn:
    reader=csv.reader(fIn)
    for line in fIn:
        print line

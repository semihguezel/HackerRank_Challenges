import math
import os
import random
import re
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    
    timeCharged = float(input().strip())
    
    columns = ['charge_time', 'battery_lasted']
    dataset = pd.read_csv('trainingdata.txt', header=0, names=columns)

    # According to the chart, we must remove items with a 
    # duration of time greater than eight.
    dataset = dataset[dataset.iloc[:,1] < 8]


    # Separe variables dependet and independent
    X = dataset.drop(columns='battery_lasted', axis=1)
    y = dataset.loc[:,'battery_lasted']

    # Create the classifier model
    model = LinearRegression()
    model.fit(X, y)

    # Set new value to predict
    
    result = model.predict([[timeCharged]])
    if result[0] > 8:
        print (8.0)
    else:
        print (round(result[0],2))

#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#Question 1
print("Question 1")
p=pd.Series([1,2,3,4,5,6,7,8,9,10])
q=pd.Series([10,9,8,7,6,5,4,3,2,1])
#since the series are the same size, start with difference
difference=q-p
squarediff=(difference)**2
sumsquarediff=squarediff.sum()
q_1=sumsquarediff*(1/2)
print(q_1)

#Question 2
print("Question 2")
df=pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
q_2=df[['c','b','a','d','e']]
print(q_2)

#Question 3
print("Question 3")
df=pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
q_3=df.iloc[:, [2,1,0,3,4]]
print(q_3)

#Question 4
print("Question 4")
df=pd.DataFrame(np.random.random(4)**10, columns=['random'])
#print(df)
q_4=np.round(df, 4)
print(q_4)

#Question 5
print("Question 5")
#import euclidean
from scipy.spatial.distance import euclidean
df = pd.DataFrame(np.random.randint(1, 100, 40).reshape(10, -1),
                  columns=list('pqrs'),
                  index=list('abcdefghij'))
#review what the dataframe looks like
#print(df)
#create empty columns
df['closestidx'] = None
df['closestdist'] = None

#select only numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

# calculate euclidean distance between a row of interest and all other rows
#for each index in the dataframe
for idx in df.index:
    #create an empty dictionary
    distances={}
#for each other row besides the row of interest
    for x in df.index:
#if not the row of interest
        if idx !=x:
#calculate the distance between the row of interest and another row, store in new variable, using only numeric values
            distances[x]=euclidean(df.loc[idx, numeric_cols].to_numpy(), df.loc[x, numeric_cols].to_numpy())
#find the closest distance and assign this distance and it's index to the row for the new columns
    closest_idx = min(distances, key=distances.get)
    df.loc[idx, 'closestidx'] = closest_idx
    df.loc[idx, 'closestdist'] = distances[closest_idx]

print(df[['closestidx', 'closestdist']])

#Question 6
#create a correlation matrix is my interpretation of the problem since there was no question
print("Question 6")
data = {'A': [45, 37, 0, 42, 50],
        'B': [38, 31, 1, 26, 90],
        'C': [10, 15, -10, 17, 100],
        'D': [60, 99, 15, 23, 56],
        'E': [76, 98, -0.03, 78, 90]
        }
df=pd.DataFrame(data)
matrix=df.corr()
print(matrix)
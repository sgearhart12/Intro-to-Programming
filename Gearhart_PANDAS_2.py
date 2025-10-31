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
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

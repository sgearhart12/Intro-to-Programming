import numpy as np
print("Problem 1")
print(np.__version__)

print("Problem 2")
array=np.array([0,1,2,3,4,5,6,7,8,9])
print(array)

print("Problem 3")
import numpy as np
#identifying the url
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#create an array of this data
irisdata=np.genfromtxt(url,delimiter=",",dtype=None)
#print the first 5 rows
print(irisdata[0:5])

print("Problem 4")
#this is a 2D array
#first let new variable equal the value we are looking for in column 4. In numpy, column for will be  f3
petalwidthgreater1=np.where(irisdata['f3']>1)
#return a tuple containing all indices where this condition is met in the fourth column
#print(petalwidthgreater1)
#print the first instance, the first indice in the tuple
print(petalwidthgreater1[0][0])

print("Problem 5")
#create a list of 20 random numbers between 1 and 50
np.random.seed(100)
a=np.random.uniform(1,50, 20)
#looking at the original data
#print(a)
#confirming that this is really a 1D array
#print(a.ndim)
#completing in two steps
updatedarray=np.where(a>30,30,a)
finalarray=np.where(updatedarray<10,10,updatedarray)
#checking work
print(finalarray)
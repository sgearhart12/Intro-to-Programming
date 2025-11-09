#import pandas
import pandas as pd

#code for import provided by dataset
from ucimlrepo import fetch_ucirepo 
  
#fetch dataset 
diabetes=fetch_ucirepo(id=296) 

#combine into a dataframe that we can use with PANDAS
df=diabetes.data.original

#this dataset is so large that I will instead use a sample
df_sample=df.sample(1000)

#Start by reviewing the data
print(df_sample.info)
print(df_sample.head)
print(df_sample.columns)

#Pivot
print("Pivot")
#Our data already appears to be in a wide format, so we will start with the pivot function.
df_pivot=df_sample.pivot(index='patient_nbr', columns='encounter_id', values='A1Cresult')
#print the first few rows
print(df_pivot.head())

#Melt
print("Melt")
#Now we can convert this previous table back to our column format using melt. 

#First, reset the index so 'patient_nbr' becomes a regular column again
df_reset=df_pivot.reset_index()

#Now melt the table. ID_vars is the columns to keep fixed, var_name is a new column for previous column headers and value_name is a new column for these values.
df_melt=pd.melt(df_reset, 
                  id_vars='patient_nbr',      
                  var_name='encounter_id',    
                  value_name='A1Cresult')  
    
#print the first few rows
print(df_melt.head())

#Aggregation and Groupby
print("Aggregation and Groupby")
#let's find the average num_lab_procedures for each patient using the original dataframe (not melted or pivoted)
#we will use groupby and aggregation to acccomplish this
avglab=df.groupby('patient_nbr')['num_lab_procedures'].mean()
print(avglab.head())
#now we can go beyond just the meme to understand this data by patient
avglabsumstats=df.groupby('patient_nbr')['num_lab_procedures'].agg(['mean','min','max'])
print(avglabsumstats.head())

#Iterate
print("Iterate")
#let's say we want to iterate over our patient data to create a new column that identifies patients as older adults (aged over 65), adults (18-64), and youth (under 18)
#first, let's define a function that will assign patients to each group based on their age

#this initially failed, so I had to check the datatype for age
print(df['age'].dtype)
print(df['age'].unique())

#age is set as ranges rather than an int as I expected. Corrected function below

def agefunction(age):
    if age=='[0-10)' or age=='[10-20)':
        return "Youth"
    if age=='[20-30)':
        return "Young Adult"
    elif age=='[30-40)' or age=='[40-50)' or age=='[50-60)':
        return "Adult"
    else:
        return "Older adult"

#now let's apply to the dataframe and create a new column associated with this category using iteration
df['Age Category'] = df['age'].apply(agefunction)
print(df.head())
#see results!



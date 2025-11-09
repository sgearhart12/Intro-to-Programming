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

#Problem 2
print("Problem 2: Pivot")
#Our data already appears to be in a wide format, so we will start with the pivot function.
df_pivot=df_sample.pivot(index='patient_nbr', columns='encounter_id', values='diag_1')
print(df_pivot)

#Problem 1
print("Problem 1: Melt")
#Now we can convert this previous table back to our column format using melt. 

#First, reset the index so 'patient_nbr' becomes a regular column again
df_reset=df_pivot.reset_index()

# Now melt the table back to long format
df_melt=pd.melt(df_reset, 
                  id_vars='patient_nbr',       # columns to keep fixed
                  var_name='encounter_id',     # new column for previous column headers
                  value_name='diag_1')         # new column for values

print(df_melt.head())  # print first few rows

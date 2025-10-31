#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

#importing our data
flights_data=pd.read_csv(r"C:\Users\sgear\OneDrive\Desktop\DBMI\Fall 2025\Intro to Programming BMI 6018-001\flights.csv")
flights_data.head(10)
weather_data_pd=pd.read_csv(r"C:\Users\sgear\OneDrive\Desktop\DBMI\Fall 2025\Intro to Programming BMI 6018-001\weather.csv")
weather_data_np=weather_data_pd.to_numpy()

#Question 1 - how many flights were there from JFK to SLC?
print("Question 1")
#inspecting the data
#print(flights_data.columns)
q_1=((flights_data['origin']=='JFK') & (flights_data['dest']=='SLC')).sum()
#confirming that q_1 is an int
#print(type(q_1))
print(q_1)

#Question 2 - how many airlines fly to SLC?
print("Question 2")
q_2=flights_data.loc[flights_data['dest']=='SLC', 'carrier'].nunique()
print(q_2)
#checking my work
#carriers=flights_data.loc[flights_data['dest']=='SLC','carrier'].unique()
#print(carriers)
#confirming that two carriers, DL and B6 service SLC

#Question 3 - what is the average arrival delay for flights to RDU?
print("Question 3")
q_3=flights_data.loc[flights_data['dest']=='RDU', 'arr_delay'].mean()
print(q_3)

#Question 4 - what proportion of flights to SEA come from the two NYC airports (LGA and JFK)?
print("Question 4")
#to calculate a percentage lets create a numerator and denominator
#numerator flights from NY to SEA broken out into two steps for each airport
numerator1=((flights_data['dest']=='SEA') & (flights_data['origin']=='LGA')).sum()
#print(numerator1)
#noticing that numerator1 is 0, but this aligns with the data
numerator2=((flights_data['dest']=='SEA') & (flights_data['origin']=='JFK')).sum()
#print(numerator2)
numerator=numerator1+numerator2
#denominator flights to SEA
denominator=(flights_data['dest']=='SEA').sum()
#print(denominator)
q_4=(numerator/denominator)*100
print(q_4)

#Question 5 - which date has the largest average departure delay?
print("Question 5")
#create a column to hold the date format which will be used in the next question as well
flights_data['datecombined']=flights_data['year'].astype(str) + '/' + flights_data['month'].astype(str) + '/' +flights_data['day'].astype(str)
longest_departure_delay=flights_data.sort_values(by='dep_delay', ascending=False).iloc[0]
q_5=longest_departure_delay['datecombined']
print(q_5)

print("Question 6")
longest_arrival_delay=flights_data.sort_values(by='arr_delay', ascending=False).iloc[0]
q_6=longest_arrival_delay['datecombined']
print(q_6)

print("Question 7")
#we will need to create a variable for speed
flights_data['speed']=(flights_data['distance'])/(flights_data['air_time'])
fastest_flight=flights_data[(['origin']=='JFK') or (flights_data['origin']=='LGA')].sort_values(by='speed', ascending=False).iloc[0]
print(fastest_flight['tailnum'])

print("Question 8")
print(weather_data_np.dtype)
#set nan values to 0 in the pandas dataframe
containsnumeric=weather_data_pd.select_dtypes(include=np.number).columns
weather_data_pd[containsnumeric]=weather_data_pd[containsnumeric].fillna(0)
#check work
nans=weather_data_pd[containsnumeric].isna().any().any()
print(nans)
#no nans remain

print("Question 9")
q_9=np.sum(weather_data_np[:,3]==2)
print(q_9)

print("Question 10")
#ignoring nan in calculation
q_10=np.nanmean(weather_data_np[:,8])
print(q_10)

print("Question 11")
q_11=np.nanstd(weather_data_np[:,8])
print(q_11)





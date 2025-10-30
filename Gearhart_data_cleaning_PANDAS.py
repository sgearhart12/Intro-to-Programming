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
q_2=flights_data.loc[flights_data['dest']=='SLC', 'carrier'].nunique()
print(q_2)
#checking my work
#carriers=flights_data.loc[flights_data['dest']=='SLC','carrier'].unique()
#print(carriers)
#confirming that two carriers, DL and B6 service SLC

#Question 3 - what is the average arrival delay for flights to RDU?
q_3=flights_data.loc[flights_data['dest']=='RDU', 'arr_delay'].mean()
print(q_3)

#Question 4 - what proportion of flights to SEA come from the two NYC airports (LGA and JFK)?
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
            




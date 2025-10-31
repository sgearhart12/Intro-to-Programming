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
#calculate departure delay for each combination of month, day.
def dep_date(month):
    monthdata=flights_data[flights_data['month']==month]
    largest_delay=monthdata.sort_values(by='dep_delay', ascending=False).iloc[0]
    return (largest_delay['day'], largest_delay['dep_delay'])
#this will return the date associated with the largest departure delay in the month

#now print the value for each month
january=(dep_date(1))
print("January")
print(january)
february=(dep_date(2))
print("February")
print(february)
march=(dep_date(3))
print("March")
print(march)
april=(dep_date(4))
print("April")
print(april)
may=(dep_date(5))
print("May")
print(may)
june=(dep_date(6))
print("June")
print(june)
july=(dep_date(7))
print("July")
print(july)
august=(dep_date(8))
print("August")
print(august)
september=(dep_date(9))
print("September")
print(september)
october=(dep_date(10))
print("October")
print(october)
november=(dep_date(11))
print("November")
print(november)
december=(dep_date(12))
print("December")
print(december)

#now let's put these tuples into a new array to work with
monthtuples=[january, february, march, april, may, june, july, august, september, october, november, december]
month_names=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
newarray=pd.DataFrame(monthtuples, columns=['day', 'delay'])
newarray['month']=month_names

#finally, let's return the highest delay value from all of them
final_delay=newarray.sort_values(by='delay', ascending=False).iloc[0]
print(final_delay)

#now we need to put the solution in the right format since we can see the right day is January 9
month=1
year=2013
day=9

q_5=f'{year}/{month}/{day}'
print(q_5)

#For next question try using pd slice and then applying to previous question...


            




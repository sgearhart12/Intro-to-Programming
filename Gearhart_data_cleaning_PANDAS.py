#importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
print(os.path.exists(r"C:\Users\sgear\OneDrive\Desktop\DBMI\Fall 2025\Intro to Programming BMI 6018-001\flights.csv"))


#importing our data
flights_data=pd.read_csv(r"C:\Users\sgear\OneDrive\Desktop\DBMI\Fall 2025\Intro to Programming BMI 6018-001\flights.csv")
flights_data.head(10)
weather_data_pd=pd.read_csv(r"C:\Users\sgear\OneDrive\Desktop\DBMI\Fall 2025\Intro to Programming BMI 6018-001\weather.csv")
weather_data_np=weather_data_pd.to_numpy()

#Question 1 - how many flights were there from JFK to SLC? Int q_1
print("Question 1")



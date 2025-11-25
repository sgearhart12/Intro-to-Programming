# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''

#understanding the data
print(covid_df.head())
print(covid_df.columns)
print(covid_df.columns[:15])

#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''
#let's show Utah in May 2020
#Select only the May 2020 columns from UT
#first, select only Utah counties
utah_df=covid_df[covid_df['Province_State']=='Utah']
may_cols=[col for col in utah_df.columns if col.startswith('5/') and col.endswith('/20')]
df_may=utah_df[['Admin2'] + may_cols] 
#Convert from wide to long format for ease of time series data
df_long=df_may.melt(id_vars='Admin2', var_name='date', value_name='cases')
#Convert date strings to datetime for ease of use
df_long['date']=pd.to_datetime(df_long['date'], format='%m/%d/%y')

#Create a new column called 'color' for highlighting
highlight_county='Salt Lake'
df_long['color']=df_long['Admin2'].apply(lambda x: 'red' if x==highlight_county else 'blue')

plt.figure(figsize=(12, 6))
plt.scatter(df_long['date'], df_long['cases'], c=df_long['color'], alpha=0.7)

plt.title('Utah COVID Cases by County - May 2020')
plt.xlabel('Date')
plt.ylabel('Cases')
plt.xticks(rotation=45)
plt.tight_layout()

#ceate a legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Salt Lake County',
           markerfacecolor='red', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Other Counties',
           markerfacecolor='blue', markersize=10)
]
plt.legend(handles=legend_elements, loc='upper left')
plt.show()

#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''
#we need to sum all cases to date in UT and FL counties, then identify the two with the most cases.
#create a function to determine which columns are dates containing case values
def is_date(col_name):
    try:
        pd.to_datetime(col_name, format='%m/%d/%y')
        return True
    except Exception:
        return False
#get the columns whose names are dates in M/D/YY format
date_cols=[c for c in covid_df.columns if is_date(c)]
#create a new column to store this sum
covid_df['sum_cases']=covid_df[date_cols].sum(axis=1)
print(covid_df[['Admin2', 'sum_cases']].head())
#now we need to find the counties with the highest numbers in UT and FL
#assign most cases in FL and UT to new variables

#FL dataframe first
FL_df=covid_df[covid_df['Province_State']=='Florida']
#highest cases in Florida
highest_FL=FL_df['sum_cases'].max()
highest_FL=int(highest_FL)
#index location
max_index_FL=FL_df['sum_cases'].idxmax()
highest_FL_county=FL_df.loc[max_index_FL, 'Admin2']
print("FL highest cases:", highest_FL)
print("County:", highest_FL_county)

#UT dataframe next
UT_df=covid_df[covid_df['Province_State']=='Utah']
#highest cases in Florida
highest_UT=UT_df['sum_cases'].max()
highest_UT=int(highest_UT)
#index location
max_index_UT=UT_df['sum_cases'].idxmax()
highest_UT_county=UT_df.loc[max_index_UT, 'Admin2']
print("UT highest cases:", highest_UT)
print("County:", highest_UT_county)

#now we will create a bar chart with these cases and counties
counties=[highest_UT_county, highest_FL_county]
case_count=[highest_UT, highest_FL]

plt.bar(counties, case_count)

plt.title('Total COVID Cases in Salt Lake and Miami-Dade 2020-2023')
plt.xlabel('County')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
#we will use Salt Lake county
#create a new dataframe for salt lake county only
saltlake_df=covid_df[covid_df['Admin2']=='Salt Lake']
#idenify date columns with case counts to create a running total
def is_date(col):
    try:
        pd.to_datetime(col, format='%m/%d/%y')
        return True
    except:
        return False
#create new list of columns that are dates
date_cols=[c for c in covid_df.columns if is_date(c)]
#now, sum the salt lake county row
cumulative=saltlake_df[date_cols].iloc[0]
#create a variable that captures the change in the sum between each column
daily_new=cumulative.diff().fillna(cumulative.iloc[0]) 

dates=pd.to_datetime(date_cols, format='%m/%d/%y')

fig, ax1=plt.subplots(figsize=(12, 6))
#choose colors
color_cumulative='blue'
color_daily='purple'

#Plot cumulative cases
ax1.set_xlabel('Date')
ax1.set_ylabel('Cumulative Cases', color=color_cumulative)
ax1.plot(dates, cumulative, color=color_cumulative, label='Cumulative Cases')
ax1.tick_params(axis='y', labelcolor=color_cumulative)

#Create second y-axis for daily new cases
ax2 = ax1.twinx()
ax2.set_ylabel('Daily New Cases', color=color_daily)
ax2.bar(dates, daily_new, color=color_daily, alpha=0.5, label='Daily New Cases')
ax2.tick_params(axis='y', labelcolor=color_daily)
plt.title(f'COVID Cases in {highlight_county}')
fig.autofmt_xdate()  # nicely formats the dates on x-axis
fig.tight_layout()

plt.show()



#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''
#we already summed cases by county previously in 'sum cases' column in the covid_df
#create a dataframe for UT
UT_df= covid_df[covid_df["Province_State"]=='Utah'].copy()

#we have one row per county with total cases
counties=UT_df["Admin2"]
values=UT_df["sum_cases"]

fig, ax=plt.subplots()

bottom=0
for county, val in zip(counties, values):
    ax.bar(
        "Utah",   
        val,          
        bottom=bottom,
        label=county
    )
    bottom += val

ax.set_ylabel("Total COVID cases")
ax.set_title("County contributions to total COVID cases in utah")
ax.legend(
    title="County",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()
plt.show()


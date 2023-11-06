
"""
   Joseph Baruch
   CS 212: Project 1
   Due: 11/08/2023
   Description: 
       This program retrieves stock prices from a stock price API. 
       Then, this data is presented in a Matplotlib graph for visual
       analysis. 
"""
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
    ------ HTTP Request to Alpha Vantage Stock Price API -----
"""
# ---- HTTP Request to API  for data ----
url = 'https://www.alphavantage.co/query?'
key = '&apikey=39G28MAGU76LGPYW'
function = 'function=TIME_SERIES_MONTHLY'
symbol = '&symbol=IBM' # Specifies the stock for IBM Company
totalURL = url + function + symbol + key # Preparing string query URL 
data = requests.get( totalURL ).json() # HTTP GET request 

"""
    ----- Pandas DataFrame -----
"""
 # converting to dataframe and entering correct sub-category
data_in_df = pd.DataFrame(data["Monthly Time Series"])
IBM_data = data_in_df.transpose() # switching X and Y for proper format

"""
    ----- Data Manipulation using numpy and other -----
"""
# fetch stock high and low values and convert to array
high_val = IBM_data["2. high"].to_numpy() 
low_val = IBM_data["3. low"].to_numpy()

# Convert the array of strings into an array of floats for matplotlib
def convert_strings_to_floats(input_array):
    output_array = []
    for element in input_array:
        converted_float = float(element) 
        output_array.append(converted_float)
    return output_array

# Call above function for high and low values
high = convert_strings_to_floats(high_val)
low = convert_strings_to_floats(low_val)

"""
    ------ MatPlotLib --------
""" 
plt.style.use('_mpl-gallery')

# plot
fig, ax = plt.subplots()

# Two seperate plots (high and low values)
ax.plot(pd.to_datetime(IBM_data.index.values), high, linewidth=1.0, color="red", label="high")
ax.plot(pd.to_datetime(IBM_data.index.values), low, linewidth=1.0, color="green", label="low")

# Labeling
plt.title("IBM High and Low Price (2000-2024)")
plt.xlabel("Time (year)")
plt.ylabel("Cost ( US Dollars )")
plt.legend(loc="upper left")

# Rotating x-axis labels for better viewing
plt.xticks(rotation=45, ha='right')

plt.show()     




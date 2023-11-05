
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

# ---- HTTP Request to API  for data ----
url = 'https://www.alphavantage.co/query?'
key2 = '&apikey=W8UBPRCPRPG0F5PJ'
 # key = '&apikey=39G28MAGU76LGPYW'
function = 'function=TIME_SERIES_MONTHLY'
symbol = '&symbol=IBM' # Specifies the stock for IBM Company
# IBM 
totalURL = url + function + symbol + key2 # Preparing string query URL 
data = requests.get( totalURL ).json() #

data_in_df = pd.DataFrame(data["Monthly Time Series"]) # converting to dataframe

IBM_data = data_in_df.transpose() # switching X and Y for proper format

IBM_data['index'] = range(1, len(IBM_data) + 1) # creating new column for index's

open_val = IBM_data["2. high"].to_numpy() # Convert to array
#open_val = np.flip(open_val) # flip values in the array so they are old -> new

# Convert the array of strings into an array of floats for better plotting in matplotlib
def convert_strings_to_floats(input_array):
    output_array = []
    for element in input_array:
        converted_float = float(element) 
        output_array.append(converted_float)
    return output_array

# Convert plotted values into floats for easier and cleaner plotting
values_as_float = convert_strings_to_floats(open_val)
indeces = convert_strings_to_floats(IBM_data['index'])

# Plot the open values for IBM using matplotlib 
plt.style.use('_mpl-gallery')

# plot

fig, ax = plt.subplots()
ax.plot(pd.to_datetime(IBM_data.index.values), values_as_float, linewidth=1.0)

plt.title("IBM Open Price (2000-2024)")
plt.xlabel("Time (year)")
plt.ylabel("Cost ( US Dollars )")

plt.xticks(rotation=45, ha='right')

plt.show()     




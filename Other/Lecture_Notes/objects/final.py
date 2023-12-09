import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?'
key = '&apikey=39G28MAGU76LGPYW'
function = 'function=TIME_SERIES_MONTHLY'
symbol = '&symbol=IBM'

totalURL = url + function + symbol + key
x = requests.get( totalURL ).json()

print(x.keys())
# print(x['Monthly Time Series'])

values = pd.DataFrame(x["Monthly Time Series"])

new = values.transpose()

new.head()
new['index'] = range(1, len(new) + 1)

dates = list(new.index.values)
dates.reverse()

new.head()

values = new["1. open"].to_numpy()
def convert_strings_to_floats(input_array):
    output_array = []
    for element in input_array:
        converted_float = float(element)
        output_array.append(converted_float)
    return output_array
input_array = ['1.1', '1.5', '2.7', '8.9']
output_array = convert_strings_to_floats(values)

type(new["index"][1])



import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
y = output_array
x = new["index"]

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=1.0)

ax.set(xlim=(0, 287), xticks=np.arange(1, 287),
       ylim=(min(output_array), max(output_array)), yticks=np.arange(min(output_array), max(output_array)))


plt.show()
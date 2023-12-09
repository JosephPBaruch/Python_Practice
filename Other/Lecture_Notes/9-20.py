precip_list = []
with open("test.csv") as src:
    for row in src:
       if "Idaho (PST)" in row:
           continue
       parsed = row.split(',')
       #print(parsed)
       #if '\n' in parsed:
           #print(parsed)
       #if '\n' in parsed:
           #parsed.remove('\n')
       #if parsed:
           #if 'PREC.I-1 (in)' not in parsed[3]:
               #precip_list.append(parsed[3])
           #print(parsed)
           
import pandas as pd
test_data = pd.read_csv('test.csv', header=2)
#print(test_data.head())
test_data.columns
#test_data

import matplotlib.pyplot as plt
plt.plot(test_data['Date'].tolist(), test_data['PREC.I-1 (in) '].tolist())
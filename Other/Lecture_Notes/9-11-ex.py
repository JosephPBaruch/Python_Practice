# Example Problem for 9/11/2023

# create a dict that has monthly cost of stuff

# use list(), .keys() and .values() to create two lists. Name whatever

costs = {}

costs = dict( Housing = 1200,
             Transportation = 500,
             Groceries = 300,
             Entertainment = 150,
             Utilities = 200 )

key_list = list(costs.keys())

value_list = list(costs.values())

al
if 'Housing' not in key_list:
    costs['Housing'] = 1200
else:
    print("There is already a Housing Cost")
    
print(costs)

#print(key_list)

#print(value_list)

#find total cost
    # sum function
    
percent_list = []

for val in value_list:
    percent_list.append(val/sum(value_list) * 100)
    #percent_list.append(percent)

# [((val/sum(value_list))*100) for val in percent_list]
    
#print(percent_list)

labels = key_list
sizes = percent_list
fid, ax = plt.subplots()
ax.pie(sizes, labels=labels)
# Dictionaries Continued (dict(), .keys(), .values(), list())
# Joseph Baruch
# 9/11/2023

# Go over list methods to practice and start learning them 
    # Write them down
    
# Go over dictionaries methods to practice and start learning them 
    # Write them down

# Dicionaries ({})

import matplotlib.pyplot as plt

my_dict = {'key': 1}

my_dict['key'] # use the other kind because it will give error if key doesnt exist

my_dict.get('key') # This is better because it wont give an error

# using the dict function

 # print(my_dict)
my_list = [1,2,3]

my_dict2 = dict( name = 'joseph', person = 'me', value = 1, ) #lis = my_list
    # do not provide string as nane
    # remember: Dictionaries can use different data types
    
# to add key-value paris: my_dictionary[key] = value

if not my_dict2.get('name'): # using get incase of an error
    my_dict2['name'] = 'me' # Note that if we use dict, it will override the entire list
else:
    print("there is already a name")

#print(my_dict2)

# you can print keys with ,keys()
# make a list of these keys

key_list = list(my_dict2.keys())

print(key_list)

if 'lis' not in key_list:
    my_dict2['lis'] = 'Test'
else:
    print("there is a already this key and value")


print(my_dict2)
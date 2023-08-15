# Calculator
#print("Have Python add two numbers together!")
#value_one = float(input("Value 1: ")) # float conversion can be here or ...
#value_two = float(input("Value 2: "))
#sum = value_one + value_two # float conversion could also be here ex. float(value_one)
#print( "Sum: " + str(sum) )

# String Manipulation (remember: upper(), lower(), find(something), replace(something, with something))
#name = "joseph"
#upper_name = name.upper()
#print(upper_name)
#print(name)

# Convert lbs to kg or kg to lbs
#print("Have Python convert your weight to lbs or kgs!")
#input_weight = float(input("Enter your weight: "))
#type = input("(L)bs or (K)gs?: ")
#if type == "L" or type == "l":
#    out_weight = input_weight * 0.453592 # convert lbs to kgs
#    type = "kgs"
#if type == "K" or type == "k":
#    out_weight = input_weight * 2.20462 # convert kgs to lbs
#    type = "lbs"
#print("You weight " + str(out_weight) + " " + type ) 


# Random Numbers
#import random
#number = random.randint(0,100)
#print(number)

# Car Simulation

# Need to start, stop, and quit the game
# Need to have a help option
# Message if car starts, stops or the game quits
#car = "off"
#while True:
 #   instruction = input("> ").lower()
 #   if instruction == "help":
 #       print( 
 #       """
 #       start: start the car engine
 #       stop: stop the car engine
  #      quit: stop the simulation
  #      """)
  #  elif instruction == "start" and car == "off":
  #      print("The car is now on!")
  #      car = "on"
  #  elif instruction == "start" and car == "on":
  #      print("The car is already on...")
  #  elif instruction == "stop" and car == "on":
  #      print("The car is now off!")
   #     car = "off"
   # elif instruction == "stop" and car == "off":
   #     print("The car is already off...")
   # elif instruction == "quit":
  #      break
   # else:
  #      print("I dont understand. Try again")
        
# Take Away: When running in the terminal, it is important to quit the program before "running" it again. Changes wont happen.
    
# 2D Lists
#matrix = [
#   [ "one", "two", "three"],
 #   [ 1, 2, 3],
 #   [ 1, "two", 3]
#]
#print(matrix[1][1])

# Remove the duplicates of a list

list = [ 4, 5, 4, 5, 6, 8, 9, 1, 2, 3, 4, 4, 8, 10, 3, 5 ]
#list.sort()
list2 = list.copy()

# print(list2)

for items in list2:
    print(items.index())

# There might be another way to do this with only one list where you dont need to sort the list first but I dont know how. 
# The best way to do this is just adding into another array 


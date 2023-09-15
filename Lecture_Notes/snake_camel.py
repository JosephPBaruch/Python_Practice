def un_camel(my_str):
    snake_case = "" # accumulator 
    first_char = my_str[0].lower() # lower moves it to lower case
    snake_case += first_char
    for char in my_str[1:]: # if you dont specify the end location it goes to very end
        if char.isupper(): # isupper returns a bool
            snake_case += '_'
        snake_case += char.lower()
    return snake_case
        
print(un_camel("camelCase"))

print(un_camel("camelCase") == "camel_case")
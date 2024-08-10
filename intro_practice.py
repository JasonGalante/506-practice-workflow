import pandas as pd
import numpy as np
import math

#create a number variable, a string variable, and a list
number = 5
string = "Jason"
list = [1, 2, 3] 

#create adictionary that contains 3 key: value pairs which includes 1 list, and 1 nested dictionary
Dictionary1 = {
        "Key_1": "value1",
        "Key_list": ["1", "2", "3"],
        "Key_Dictionary": {
            "d1": "value_d1",
            "d2": "value_d2",
            "d3": "value_d3"
        }
    }

#create a function with 2 arguments and a calculation with an if/else statement
def my_function(age, height_in_inches):
    print(f'you are {age} years old and you are {round(height_in_inches/12,2)} feet tall ')

    if height_in_inches/12 > 6:
        print('you are very tall and ', end='' )
    else:
        if (height_in_inches/12) < 5:
            print('you are shorter than average and ', end=''),
        else:
            print('you are average height and ', end=''),
    if age > 65:
        print('you must be getting ready to retire ')
    else:
        if age < 18:
            print('you must be looking forward to graduating ')
        else:
            print('you are in the prime of your life ')

    

my_function(49,  67)    
my_function(12,  82) 
my_function(70,  55)

def age_of_a_person(age1):
    a_persons_age = age1
    return f'the persons age is: {a_persons_age}'

age_of_a_person(50)



def weight_of_a_person(weight1):
    a_persons_weight = weight1
    return f'the persons age is: {a_persons_weight}'

weight_of_a_person(180)


#this is a test to practice on push
#I have no idea why this isnt working
#second test to push



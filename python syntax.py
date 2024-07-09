if 5 > 2:
    print("Five is greater than two!")




if True:
    print("All is well!") 
 print("Wait, why am I here?") #Oops! This line is wrongly indented



# Multiline-statements in Python

a = '''Python's
multi-line
Groove!'''

b = "Hello, Coding Templers!\ How are you today?"

print(a)
print(b)


# Variables

cookies = 10
print(cookies) # 10

# -with no variables

print("Hello, Alex!")

# with variables

user_name = input("What's your name?")

print("Hello, " + user_name + "!")


# Snake case for variables

cup_of_coffee = "Expresso"
cup_of_tea = "Green Tea"

#Camel Case for functions

def orderCoffee():
    return "One coffee coming right up!"

def orderTea():
    return "A cup of tea for your thoughts!"


# Pascal Case for Classes

class CoffeeMug:
    def __init__(self, size="medium"):
        self.size = size



# UPPERCASE for Constants

TABLES = 10


# UPPER_SNAKE_CASE for constants with multiple words

MAX_SEATING_CAPACITY = 40


# ________________________________________

favorite_ice_cream = "chocolate"
print(favorite_ice_cream)



x, y, z = "apple", "banana", "cherry"
print(x, y, z)



beach = "Sunny Shore"
print(beach)


waves_today = 5
tide_height = 3.4

print(waves_today)
print(tide_height)


is_sunny = True
is_raining = False

print(is_sunny)
print(is_raining)



(int) (float) (bool) (str)

amount = 100
print(type(amount))



user_print = input("Enter a number:")
print(type(user_print))



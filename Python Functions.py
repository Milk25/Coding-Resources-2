# Special Characters

# Newline(\n)
# Tab(\t)

print("Hello, \nWorld!")
# Hello,
# World!


print("Hello\tWorld!")
# Hello World!


print("This is a backslash: \\")
# This is a backslash: \


print('She said, 'Hello!'')
print('She said, \'Hello!\'')

# She said, 'hello!'

print("He replied, |"Hi there!|"")
      # He replied, "Hi there!"




# String Concatenation

print("apple", "banana", "cherry", sep="-")
apple-banana-cherry

print("This is just the beginning...", end="")
print("and here's the continuation.")
This is just the beginning... and here's the continuation

print("apple", "banana", "cherry", sep="-", end="...yum!")
apple-banana-cherry....yum




# String Formatting
# Placeholders: str.format() or %s

F-strings: print(f"Ella loves {hobby}.")

name = "Ella"
print("Her name is %s." %name)

# Her name is Ella



age = 25
print("she is {} years old.".format(age))
# She is 25 years old.



hobby = "writing"
print(f"Ella loves {hobby}.")
# Ella loves writing


pi = 3.1415...793
print(f"The value of PI to 3 decimal places is {pi:3f}.")
# The value of PI to 3 decimals places is 3.142



# input()


answer = input("Do you like Python?(yes/no)")
if answer == "yes":
    print("That's great to hear!")
else:
    print("Oh, why not?")






number_string = "123"
number = int(number_string)
print(number + 1) # 124


decimal_string = "3.14"
pi = float(decimal_string)
print(pi + 2) # 5.1400...1




age = 25
age_string = str(age)
print("I am " + age_string + "years old.")

# I am 25 years old.



is_empty = bool("") ("pineapple") # True
print(is_empty) # False



#___________________________________
type()
len()
isinstance()



mystery_variable = "Sherlock"
clue_list = ["candlestick", "footprint", "hankerchief"]
alleged_title = "I am a duke"

print("Type of mystery_variable:", type(mystery_variable))
# Type of mystery_variable: <class 'str'>

print("Number of clues found:", len(clue_list))

# Number of clues found: 3

print("Is the title genuine?", isinstance(alleged_title, str))

# Is the title genuine? True


# Python's Number Sorcery

abs()
round()
sum()
min()
max()
pow()
divmod()

# Math module

sqrt()
ceil()
floor()
exp()
log()
sin()
cos()
tan()
radians()
degrees()
#___________________________________

import math
scores = [1, 5, 10, 8, 4, 2]
# Casting the spells

print(abs(-2023),round(3.14159, 2),sum([1, 2, 3, 4, 5]))

print(min(scores), max(scores), pow(2, 3), divmod(10, 3))

# 2023 3.14 15 

# 1 10 8 (3, 1)

print(math.sqrt(16), math.ceil(2.1), math.floor(2.9))
# 4.0 3 2


print(math.exp(1), math.log(10))
# 2.718...045  2.3025...046


angle = 10
print(math.sin(angle), mathj.cos(angle), math.tan(angle))
# -0.544...698  -0.835...524

print(math.radians(180), math.degrees(math.pi))

# 3.1415...793   180.0








#_________________________________-
# Exercise 1: 

'''
In the digital age, usernames are crucial for identity on various platforms.
Your task is to write a program that checks if
a username is neither too short not too long,
adhering to specific length criteria.

**Instructions**:

1. Prompt the user to entera username.
2. Check if the username is between 5 and 15 character long.
3. If the username meets the criteria, print a confirmation message.
4. If it does not meet the criteria, print a message indicating the username length requirements.
5. Provide the user with the option to try a different username or exit the program.

'''


while True:
username = input("Enter your desired username:")

if 5 <= len(username) <= 15:
    print("Username is valid!")
else:
    print("Username must be between 5 and 15 characters!")

continue_input = input("Do you want to try another username?(yes/no)").lower()
if continue_input != 'yes':
    break


#_________________________________________
'''
# Exercise 2: The Precise Price Tagger

In retail applications, both online and in-store, 
displaying prices in a clear and precise manner is 
essential for customer satisfaction.
Your task is to write a program that takes 
a price as input and rounds it to two decimal 
places, making it more user_friendly.

**Instructions**:

1. Prompt the user to enter a price.
2. Use the 'round()' function to round the price to two decimal places.
3. Display the rounded price in a format that is easy for customers to understand.
4. Provide the user with the option to enter a new price or exit the program.

'''

while True:
    price_input = float(input("Enter the price: "))
    rounded_price = round(price_input, 2)
    print(f"Rounded Price: $(rounded_price)")

    new_price = input("Would you like to enter in a new price?(yes/no)").lower()
    if new_price != 'yes':
        break



#______________________________________________


'''
**Problem Statement**:

You are creating a feature for a travel app that allows users to view the temperature in both Celsius
and Fahrenheit, so they can easily understand the weather forecast
no matter where they travel.


**Instructions**:

1. Create a list of temperatures in Celsius that you want to convert.
2. Loop through the list, and for each temperature in Celsius, convert it to Fahrenheit.end=
3. Print out both the Celsius and fahrenheit temperature using f-strings for formatted output.

'''

celsius_temperatures = [10, 20, 25, 30, 35]

for celsius in celsius_temperatures:
    fahrenheit = (celsius + 9/5) + 32
    print(f"{celsius} C is equivalent to {fahrenheit} F")



#_____________________________________



'''
Goldilocks wants to find the warmest and coolest rooms in her house based on the current temparature readings.
She has a list of temperatures for each room
and needs a quick way to determine which
rooms are the warmest and coolest.

**Instructions**:

1. Create a list of temperatures and rooms for each room in the house.end=
2. Determine the warmest and coolest temperatures using the 'max()' and 'min()' functions.
3. Identify the rooms with these temperatures and print out the results using string formatting.

'''

room_temperatures = [22, 29, 19, 21]

room_names = ['living room', 'kitchen', 'bedroom', 'bathroom']

warmest_temp = max(room_temperatures)
coolest_temp = min(room_temperatures)

warmest_room_index = room_temperatures.index(warmest_temp)
coolest_room_index = room_temperatures.index(coolest_temp) 

print(warmest_room_index, coolest_room_index)
print(room_names[warmest_room_index])

warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]

print(f"The {warmest_room} is the warmest with {warmest_temp}C")
print(f"The {coolest_room} is the coolest with {coolest_temp}C")

print(warmest_temp, coolest_temp)

# 24 19











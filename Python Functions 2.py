'''
Exercise 5: The E-Commerce Cart Summary

In an e-commerce application, its important 
to provide customers with a clear and concise 
summary of their shopping cart before they proceed
to checkout.
Your task is to write a Python script that uses
string concatenation to create a summary of the
items in a shopping cart, including product names,
prices, and stock availability.

**Instructions**:

1. Define variables for a few products, their
prices, and their stock avalability.
2. Use string concatenation to build a summary
of the cart.
3. Include product names, prices, and stock status
(In stock or Out of stock) in the summary.
4. Display the cart summary to the user.
 
'''

# Products

product_1 = "Wireless Mouse"
product_2 = "Gaming Keyboard"
product_3 = "USB-C Adapter"

# Prices

price_1 = "$25"
price_2 = "$50"
price_3 = "$10"

# Avalability

in_stock_1 = True
in_stock_2 = False
in_stock_3 = True

cart_summary = "Your cart Items:\n"
cart_summary += "-" + product_1 + ": " + price_1 + ("(In stock)" if in_stock_1 else "Out of Stock")
+ "\n"

cart_summary += "-" + product_2 + ": " + price_2 + ("(In stock)" if in_stock_2 else "Out of Stock")
+ "\n"

print(cart_summary)

# Wireless Mouse: $25(In stock)
# Gaming Keyboard: $50(Out of stock)
# USB-C Adapter: $10(In stock)


#______________________________________________________________________

"""
**Problem Statement**:
You are creating an interactive story where the
reader can choose their own adventure.
At each stage of the story, the reader is presented
with a choice that determines the direction of
the narrative.
Your task is to write a Python script that guides
the reader through the first decision point of
the story.

**Instructions**:

1. Present the reader with a brief introduction to the story and a choice to make.
2. Capture the reader's choice using the 'input()' function.
3. Depending on the choice, display the outcome
of their decision.
4. Use a list to store possible choices and outcomes.

"""

print("You wake up in a mysterious forest. Two paths lie before you.")

choices = ['left', 'right']
outcomes = ["You encounted a friendly elf who offers you a map.", "You stumble upon a sleeping dragon"]

print(f"Do you go left or right? (Type 'left or 'right')")
decision = input().lower()

if decision not in choices:
    print("Confused, you decide to wait for a clearer sign of which path to take.")
elif decision == 'left':
    outcome_index = choices.index('left')
    print(outcomes[outcome_index])
else:
    outcome_index = choices.index('right')
    print(outcomes[outcome_index])


#left




'''
Exercise 7: The Customized List Printer
You are tasked with creating a program that prints
out a shopping list.
However, the user wants the list to be printed
in a specific format, with customs separators
between items and custom ending to signify the end
of the list.

**Instructions**:

1. Create a list of shopping items.
2. Ask the user for their preferred separator
(e.g., comma, slash, dash).
3. Ask the user for their preferred ending phrase 
(e.g., "End of list", "That's all!").
4. Use a loop to print each item with the user's
preferred separator and end the list with their
chosen ending phrase.

'''

shopping_list = ['apples', 'bananas', 'carrots', 'bread',
'milk']

separator = input("Please enter your preferred item separator (e.g., ',', '/', '-'):")
ending = input("Please enter your preferred ending phrase (e.g., 'End of List', 'That's all'):")

print("Your shopping list: ", end="\\n\n")

for item in shopping_list:
    if item == shopping_list[-1]:
        print(item)




#__________________________________________________

'''
Exercise 8: The Dynamic Type Quiz Game
You are tacked with developing a given game that
challenges players to answer questions that require
answers in different data types. The game
should prompt the user for an answer, convert
the answer to the required type, and verify its
corrections.

**Instructions**:

1. Create separate lists for questions, correct
answer, and the required answer types.
2. Use a loop to iterate over the questions and 
present them to the user one by one.
3. For each question, prompt the user for their 
answer and convert it to the required type
using the corresponding type conversion function.
4. Compare the user's converted answer to the
correct answer and provide immediate feedback.
5. Keep a count of the number of correct
answers and display the user's score at the end
of the game.

'''
score = 0
questions = [
    "What is 10 plus 4?",
    "Enter a decimal number between 1 and 2",
    "What is the string representation of the number 20?",
    "Is Python a programming language? (True/False)"
]

correct_answers = [14, 1.5, "20", True]
answer_types = [int, float, str, bool]

for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if answer_types[i] == bool:
            converted_answer = user_answer.lower() in ['true', 't', 'l', 'yes', 'y']
        else:
            converted_answer = answer_types[i](user_answer)
        if converted_answer == correct_answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong answer.")
    except ValueError:
        print("Invalid input type.")
print(f"Your final score is {score}/{len(questions)}.")


#What is 10 plus 4? 14 12(wrong answer)
#Correct

#Enter a decimal number between 1 and 21.5
#Correct  10(wrong answer)

#What is the string representation of the number 20? "20" wrong answer, 20(Correct)

#Is Python a programming language? (True/False) True(Correct)  Yes(Correct)

#Your final score is 3/4.  Your final score is 2/4.





#_____________________________________________________

'''
Exercise 9: The Type Inspection Challenge.

You are creating a program that categories elements
in a list based on their data type.
The program should iterate over a mixed-type
list, identify the data type of each element,
and sort the elements into separate lists
according to their type.

**Instructions**:

1. Create a mixed-type list with various data types
(e.g., integers, floats, strings, booleans).
2. Initialize separate lists to hold elements
of each data type.
3. Use a loop to iterate over the mixed-type
list.
4. For each element, use `isinstance()` or 
`type()` to determine the elements type.
5. Append the element




'''
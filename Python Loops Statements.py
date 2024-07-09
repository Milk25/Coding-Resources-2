flavors = ["vanilla", "chocolate", "blueberry", "mango", "salted caramel"]

for flavor in flavors:
    print("Mmm... I just sampled" + flavor + "!")



# range()
for i in range(3):
    print("Trying out flavor number " + str(i + 1) + ": " + flavors[i])



flavors = ["chocolate"....,"pistachio"]



toppings = ["sprinkle", "chocolate syrup", "whipped cream", "cherry"]
for flavor in flavors:
    for topping in toppings:
        print("Let's try a scoop of " + flavor + "with some " + topping + " on top!")



# break
ice_cream_flavors = ["chocolate"...., "pistachio"]

for flavor in ice_cream_flavors:
    if flavor == 'mint chocolate chip':
        print("My favorite! No need to taste further.")
        break
    print("Trying" + flavor + " flavor.")




# Given Lists
booth_types = ["Food", "Games", "Music", "Crafts"]

schedule_times = ["10:00AM", "1:00PM", "3:00PM", "5:00PM"]

items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

# Iterating over the booth types with a for loop
for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule_times[i]
    item = items_needed[i]
    print(f"(booth) Booth - Schedule: (time), Items Needed: (item)")



# You have 30 students - 5 rows
# Each row can seat an equal number of students
# Use a for loop with the range function to assign and print a seat number for each student
# Seat numbers should start at 1 and increase sequentially

total_students = 30
rows = 5

students_per_row = total_students // rows
for row in range(1, rows + 1):
    for seat in range(1, students_per_row + 1):
        seat_number = (row - 1) * students_per_row + seat
        print(f"Row (row) - Seat(seat): Student (seat_number)")




# _____________________________________

# List of item prices
# Use a for loop to iterate through the list of prices
# Calculate the total cost by adding up the prices of all the items
# Print the total cost at the end

item_prices = [2.99, 5.49, 3.25, 13.99, 4.75]
total_cost = 0

for price in item_prices:
    total_cost += price
print(f"The total cost of the shopping cart is: ${total_cost: .2f}")




#___________________________________________

# Ask the user for the size of the multiplication table they wish to generate
# Use nested for loops to calculate the product of each pair of numbers
# Display the multiplication table in a formatted manner

table_size = int(input("Enter the size of the multiplication table:"))
for row in range(1, table_size + 1):
    for col in range(1, table_size + 1):
        product = row * col
        print(f"{product} \t", end="")
    print()




#___________________________________________________________________

# List representing caves, 'True'indicates the cave with the treasure

caves = [False, False, True, False, False]

# Iterate over the caves

for index, cave in enumerate(caves):
    # Check if the cave has the treasure
    if cave:
        print(f"Treasure found in cave {index + 1}!")
        break # Stop searching once the treasure is found





#_____________________________________________________

# List representing email addresses, 'None' indicates an invalid email

emails = ["user1@example.com", None, "user@example.com", "user3@example.com", None]

# List to hold valid emails

valid_emails = []

# iterate over the list of emails

for email in emails:
    # Skip the iterate of the email in invalid
    if email is None:
        continue
    # Add the valid email to the list valid_emails.append(email)
# Print the list of valid emails
print("Valid emails:", valid_emails)


#_______________________________________

# While loop
# while condition_is_true:
    # Your delicious code here



marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")





marshmallows = 0
while marshmallows < 5:
    print("Planning to add a marshmallow! Currently, there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1





# initialize a variable

temperature = 100
# Set up a while loop with a condition that is never true

while temperature < 0:
    # This block of code will not execute because the initial temperature is 100, which is not less than 0
    temperature -= 1
    print("The temperature is now:", temperature) # Since the loop body never executes, this print statement will run immediately
print("The temperature was never below 0 to begin with.")








while True:
    user_input = input("Say 'stop' to end the refill:")
    if user_input.lower() == 'stop':
        break
    else:
        print("Here's more coffee!")





while steps > 0:
    print("Descending the stairs. " + str(steps) + " steps remaining.")
    steps -= 1 # Take a step down
print("We've reached the ground floor!")





# Exercise 1. The Countdown Timer

timer = 10
# Start the countdown

while timer > 0:
    print(timer)
    timer -= 1 # Decrement the timer by one

# Print the final message
print("Time is up!")



# Exercise 2. The Patient Queue

# Initialize the number of patients in the queue

patients = 5

# Process the queue

while patients > 0:
    print(f"Patient number {patients} please come in.")
    patients -= 1 # call the next patient
# All patients have been called
print("There are no more patients in the queue.")




# Exercise 3. The Baterry Charger with Efficiency Check.

# Initialize the battery level

battery = 0
increment = 10 # Initial charging increment
# Start charging the battery

while battery < 100:
    # Charge the battery
    battery += increment
    print(f"Battery is now at {battery}%")

# Check the efficiency and adjust the charging rate

if battery == 50:
    print("Efficiency check: Increasing charge rate.")
    increment = 15
elif battery == 80:
    print("Efficiency check: Reducing charge rate to prevent overcharging.")
    increment = 5
# Battery is fully charged
print("The Battery is now fully charged.")



# Exercise 4. The Smart Coffee Machine

# Initialize the coffee reservoir level 

coffee_reservoir = 10
# List of coffee types

coffee_types = ["Espresso", "Cappucino", "Latte", "Americano", "Mocha"]

# Start dispensing coffee
while coffee_reservoir > 0:
    # Check if there are still coffee types available
    if coffee_types:
        # Dispense the first type of coffee
        current_coffee = coffee_types.pop(0)
        print(f"Dispensing {current_coffee}.")
    # Decrement the coffee amount
    coffee_reservoir -= 1
    print(f"Coffee types left: {coffee_types}")
else:
    print("No more coffee types available.")
    break
# Coffee reservoir is empty
    print("The coffee reservoir is now empty.")



#___________________________________


# random()

#import random

# Let's roll the dice 10 times

for _ in range(10):
    dice_roll = random.randint(1, 6)
    print("You rolled a " + str(dice_roll) + "!")




#____________________________

# Shuffling

#import random

playlist = ['song1', 'song2', 'song3', 'song4', 'song5']

random.shuffle(playlist)

# Let's see the shuffled playlist

for song in playlist:
    print(song)




# Randomized Loop

#import random

snacks = ['apple', 'banana', 'carrot stick', 'doughnut', 'chocolate bar']

picked_snack = ''

while picked_snack != 'chocolate bar':
    picked_snack = random.choice(snacks)
    print("You gota " + picked_snack + ".")
    if picked_snack != 'chocolate bar':
        print("Let's pick again!")
    else:
        print("Yay! Chocolate bar wins!")







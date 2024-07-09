potions = ["Healing", "Invisibility", "Strength"] 
print(potions)


empty_liist = []




print(potions[0]) # This will output Healing




favorite_potion = potions[1] # This willl get you "Invisibliy"

print(favorite_potion)




last_potion = potions[-1] # This will fetch you "Strength"

print(last_potion)



colors = ["red", "ble", "green", "yellow"]
print(colors)




ecletic_list = [42, "unicorn", 3.14, ["apple", "banana", "cherry"]]
print(ecletic_list)


ecletic_list.append("starry-night")
print(ecletic_list)

ecletic_list.remove(42)
print(ecletic_list)




# Duplicate items

flowers = ["rose", "lily", "rose", "daisy", "lily"]
print(flowers)


rose_count = flowers.count("rose") # This reveals the number 2

print(rose_count)



flowers.remove("lily") # Only the first "lily" vanishes, leaving one behind

print(flowers)



# Dynamic Additions

hobbies = ["reading", "painting", "cycling"]

print(hobbies)

hobbies.append("singing")
print(hobbies) # New entry to the end


hobbies.insert(1, "dancing") # This adds "dancing" at the second position

print(hobbies)


# Modifying Existing Values

hobbies[0] = "writing" # "reading transform into "writing"

print(hobbies)



# Taking items out

hobbies.remove = ("cycling")
print(hobbies)


# pop - removes the last item or a specific item by its position.


last_hobby = hobbies.pop() # Removes the last hobby

print(last_hobby)

second_hobby = hobbies.pop(1) # Removes "dancing"
print(second_hobby)


# Exploring & Finding

count_reading = hobbies.count("writing") 
print(count_reading)


position_painting = hobbies.index("painting") 
print(position_painting)


# Clearing the List
hobbies.clear()
print(hobbies)


# Built in Methods

# sort() - sort your items

fruits = ["banana", "apple", "cherry"]
fruits.sort() # This arranges the fruits in alphabetical order.

print(fruits)

count = len(ecletic_list)
print(count)


# Reverse() - Reverse the order of your items.

numbers = [1, 2, 3, 4, 5]
numbers.reverse() # This turns the list around.


print(numbers)




# Python List Methods

append() # Adds an element at the end of the list

clear() # Removes all the elements from the list

copy() # Returns a copy of the list

count() # Returns the number of elements with specified value

extend() # Add the elements of a list (or any iterable), to the end of the current list

index() # Returns the index of the first element with the specified value

insert() # Adds an element at the specified position

pop() # Removes the element at the specified position

remove() # Removes the item with the specified value

reverse() # Reverses the order of the list

sort() # Sorts the list.


# Identity Operators

- is
- is not


guest_1 = [1, 2, 3]
guest_2 = guest_1
guest_3 = [1, 2, 3]

print(guest_1 is guest_2) # Outputs: True
print(guest_1 is guest_3) # Outputs: False


# is not
party_crasher = [4, 5, 6]
guest_4 = [4, 5, 6]

print(party_crasher is not guest_4) # Outputs: True

# in
guest_list = ["Alice", "Bob", "Charlie"]
print("Alice" in guest_list) # Outputs: True
print("Dana" in guest_list) # Outputs: False

# not in
print("Dana" not in guest_list) # Outputs: True


# len()
hobbies = ["reading", "painting", "cycling"]
print(hobbies)

total_hobbies = len(hobbies) # This would be 3

print(total_hobbies)




# -1
last_index = len(hobbies)-1 # This would be 2
last_hobby = hobbies[last_index] # This fetches "cycling"

print(last_hobby)



position = 1
mystery_hobby = hobbies[position] # This unveils "painting"

print(mystery_hobby)


# //
middle_index = len(hobbies) # 2
middle_hobby = hobbies[middle_index]
print(middle_hobby)


# Merged or merging
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "brocooli", "peas"]

food = fruits + vegetables # Forms ["apple", "banana". "cherry", "Carrot", "brocooli", "peas"]
print(food)


fruits_clone = fruits.copy() # Creates a new list identical to fruits
print(fruits_clone)



# Joining Lists and Strings
fruits.extend(vegetables) # Fruits now holds ["apple", "Banana", "cherry", "Carrot", "brocooli", "peas"]
print(fruits)


story_elements = ["Once", "upon", "a", "time"]
story = " ".join(story_elements) # Forms "Once upon a time"
print(story)


# Slicing
hobbies = ["reading", "painting", "cycling", "singing", "dancing"]
print(hobbies)


segment = hobbies[1:3] # This extracts ["painting", "cycling"]
print(segment)


beginning_to_third = hobbies[:3] # This unveils ["reading", "painting", "cycling"]
print(beginning_to_third)



third_to_end = hobbies[2:] # This reveals ["cycling", "singing", "dancing"]
print(third_to_end)



# index - 1
enchanted_forest = ["elf", "fairy", "troll", "sprite"]

# The list has 4 creatures, but the indices range from 0 to 3.

print(enchanted_forest[4]) # This will conjure an IndexError!




































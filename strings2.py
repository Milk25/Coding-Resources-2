'''
Strings: The unaiterable Scoreboard Video
'''
original_score = "Python"

original_score[1] = 'i'   #Type Error

new_score = original_score[0] + 'i' + original_score[2:]

print(original_score) # Python
print(new_score) # Python



'''
Indexing and Accessing Characters: The Playbook Stategy Video

'''

team = "Coders"

first_letter = team[0]
third_letter = team[2]

print(first_letter) # C
print(third_letter) # d

last_letter = team[-1] # s
second_last_letter = team[-2] # r

print(last_letter) # s
print(second_last_letter) # r




'''
Iterating: The Repetitive Drill Video

'''

track = "Marathon"

for char in track:
    print(char, end=" ") # Marathon

# M a r a t h o n



'''
Iterating: Slicing: The Precision Play Video

'''

field = "Touchdown"

play_one = field[0:5] # Touch
play_two = field[5:] # down
play_three = field[2::2] # uhon
play_three = field[2::-1] # (backwards)



'''
Combining Drills: Iterating with Slicing Video

'''

game_plan = "Execute play number 9"

for word in game_plan[8:]:
    print(word, end=" ") # play number 9



'''
String Concatenation: The Passing Game Video

'''

quarterback = "Tom"
receiver = "Jerry"

play = " runs a route to catch the pass from "

complete_play = quarterback + play + receiver
print(complete_play) # Tom runs a route to catch the pass from Jerry



#_____________________________________

players = ["Python", "is", "great", "for", "string", "manipulation"]

team_statement = ""
for word in players:
    print(team_statement)
    team_statement += word + " "

print(team_statement.strip())

# Python is great for string manipulation

"""
Python
Python is
Python is great
Python is great for
Python is great for string
Python is great for string manipulation
"""

#__________________________________________________

quarterback = "Player"
jersey_number = 10
message = " scored a "
points = 6
summary = "points!"

highlight_reel = quarterback + " " + str(jersey_number) + message + str(points + summary)
print(highlight_reel) # Player 10 scored a 6 points!



'''
String Formatting: The Choreographed Celebration Video

'''
celebration = "{} scores a touchdown and does the {} dance!"










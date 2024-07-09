# Syntax:

# while some_boolean_condition:
#     # do something
# else:
#     # do something different




x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1


# The current value of x is 0
# The current value of x is 1
# The current value of x is 2
# The current value of x is 3
# The current value of x is 4




x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not les than 5')


# The current value of x is 0
# The current value of x is 1
# The current value of x is 2
# The current value of x is 3
# The current value of x is 4

# x is not less than 5




# x = [1, 2, 3]

# for item in x:
#     #comment

# # SyntaxError



x = [1, 2, 3]
for iem in x:
    # comment
    pass
print('end of my script')

# end of my script



mystring = 'Sammy'

for letter in mystring:
    print(letter)

# S a m m y



for letter in mystring:
    if letter == 'a':
        continue
    print(letter)


# S m m y




for letter in mystring:
    if letter == 'a':
        break
    print(letter)

# S


 

x = 0
while x < 5:
    print(x)
    x += 1


# 0 1 2 3 4



while x < 5:
    if x == 2:
        break
    print(x)
    x += 1


# 0 1



# if
# elif 
# else

if True:
    print('Its TRUE!')

# Its TRUE

hungry = True

if hungry:
    print('FEED ME!')

# FEED ME!


hungry = False
if hungry:
    print('FEED ME')

# no condition


hungry = False
if hungry:
    print("FEED ME!")
else:
    print("I'm not hungry")


# I'm not hungry


hungry = True
if hungry:
    print("FEED ME")
else:
    print("Im not hungry")

# FEED ME!



loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars are cool!")
else:
    print("I do not know much.")


# I do not know much.

loc = 'Bank'
if loc == 'Auto Shop':
    print("Cars are cool!")
elif loc == 'Bank':
    print("Money is cool!")
else:
    print("I do not know much.")

# Money is cool!



name = 'Sammy'

if name == 'Frankie':
    print("Hello Frankie!")
elif name == 'Sammy':
    print("Hello Sammy")
else:
    print("What is your name?")

# Hello Sammy



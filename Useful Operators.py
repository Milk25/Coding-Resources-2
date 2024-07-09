mylist = [1, 2, 3]
for num in range(10):
    print(num)

# 0 1 2 3 4 5 6 7 8 9


for num in range(3, 10):
    print(num)


# 3 4 5 6 7 8 9



for num in range(0, 10, 2):
    print(num)

# 0 2 4 6 8

# (0, 11, 2)  0 2 4 6 8 10




list(range(0, 11, 2))

# [0, 2, 4, 6, 8, 10]




index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

# At index 0 the letter is a
# At index 1 the letter is b
# At index 2 the letter is c
# At index 3 the letter is d
# At index 4 the letter is e





index_count = 0
word = 'abcde'

for letter in word:
    print(word[index_count])
    index_count += 1


# a b c d e 




word = 'abcde'
for item in enumerate(word):
    print(item)



# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')



word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

# 0 a
# 1 b
# 2 c
# 3 d
# 4 e




mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
zip(mylist1, mylist2)
# <zip at 0<2d4b64e5be8>



for item in zip(mylist1, mylist2):
    print(item)


# (1, 'a')
# (2, 'b')
# (3, 'c')



mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)


# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)



list(zip(mylist1, mylist2))

# [(1, 'a'), (2, 'b'), (3, 'c')]




for a, b, c in zip(mylist1, mylist2, mylist3):
    print(b)

# a b c



'x' in [1, 2, 3]
# False

'x' in ['x', 'y', 'z']
# True

'a' in 'a world'
# True

2 in [1, 2, 3]
# True

'mykey' in {'mykey': 345}
# True



d = {'mykey': 345}
345 in d.values()

# True


345 in d.keys()
# False



mylist = [10, 20, 30, 40, 100]
min(mylist)
# 10

max(mylist)
# 100



from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

shuffle(mylist)
# [3, 9, 7, 8, 10, 5, 1, 2, 6, 4]

shuffle(mylist)
# [4, 9, 2, 1, 10, 6, 5, 3, 7, 8]


random_list = shuffle(mylist)
random_list
# nothing

type(random_list)
# NoneType



from random import randint
randint(0, 100)

# 79

randint(0, 100)

# 99



mynum = randint(0, 10)
mynum
# 3




input('Enter a number here: ')
# Enter a number here: 50
# 50

result = input('What is your name?')
# What is your name? Jose

result
# 'Jose'



result = input('Favorite Number: ')
# Favorite Number: 30

result
# '30'

type(result)
# str



float(result)
# 30.0

int(result)
# 30


result = int(input('Favorite Number: '))
# Favorite Number: 20

type(result)
# int
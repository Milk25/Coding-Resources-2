# iterate over an object
# like list, string, key in dictionary


my_iterable = [1, 2, 3]

for item_name in my_iterable:
    print(item_name)


# 1 2 3

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in mylist:
    print(num)

# 1 2 3 4 5 6 7 8 9 10


for jelly in mylist:
    print('hello')


# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello
# hello



for num in mylist:
    if num % 2 == 0:
        print(num)

# 2 4 6 8 10


for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd number: {num}")

# Odd number: 1
# 2

# Odd number: 3
# 4

# Odd number: 5
# 6

# Odd number: 7
# 8

# Odd number: 9
# 10



list_sum = 0
for num in mylist:
    list_sum = list_sum + num

print(list_sum)

# 55


list_sum = 0
for num in mylist:
    list_sum = list_sum + num

    print(list_sum)

# 1 2 6 10 15 21 28 39 45 55


mystring = 'Hello World!'
for letter in mystring:
    print(letter)

# H e l l o  W o r l d


for letter in 'Hello World':
    print(letter)

# H e l l o  W o r l d




for ghghg in 'Hello World':
    print(ghghg)

# H e l l o  W o r l d




for _ in 'Hello World':
    print('Cool!')

# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!
# Cool!



tup = (1, 2, 3)

for item in tup:
    print(item)

# 1 2 3



mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
len(mylist)

# 4



for item in mylist:
    print(item)

# (1, 2)
# (3, 4)
# (5, 6)
# (7, 8)




for (a, b) in mylist:
    print(a)
    print(b)

# 12345678


for (a, b) in mylist:
    print(c)

# 1 3 5 7 Tuple Unpacking




for a, b in mylist:
    print(a)
    print(b)

# a  1 3 5 7
# b  2 4 6 8



mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]

for item in mylist:
    print(item)

# (1, 2, 3)  (5, 6, 7)  (8, 9, 10)



for a, b, c in mylist:
    print(b)

# 2 6 9




d = {'k1': 1, 'k2': 2, 'k3': 3}

for item in d:
    print(item)

# k1 k2 k3





for item in d.items():
    print(item)

('k1', 1)  ('k2', 2) ('k3', 3)




for key, value in d.items():
    print(value)

# 1 2 3

for value in d.values():
    print(value)

# 1 2 3








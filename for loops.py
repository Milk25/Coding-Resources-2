s = "Geeks"
for i in s:
    print(i)

s = 'geeks'
for i in s:
    print(i)

s = "Geeks"
for letter in s:
    print(letter)



for i in range(1, 12, 1):
    print(i)

for i in range(1, 10):
    print(i)


for i in range(0, 10, 2):
    print(i)




items = ["bookbag", "pen", "laptop"]

for count, ele in enumerate(items):
    print(count, ele)

items = ['bookbag', 'pens', 'laptop']
for count, ele in enumerate(items):
    print(count, ele)
i



items = ["Pen", "reel", "lighter"]

for item, ele in enumerate(items):
    print(item, ele)


for i in range(0, 10, 1):
    for j in range(1, 7, 2):
        print(i, j)


for i in range(2, 12, 3):
    for j in range(1, 12, 2):
        print(i, j)

for i in range(1, 12, 3):
    for j in range(1, 4):
        print(i, j)


l = ["geeks", "for", "geeks"]

for i in l:
    print(i)

l = ["geeks", "for", "geeks"]
for i in l:
    print(i)



l = ["geeks", "for", "geeks"]
for i in l:
    print(i)






numbers = [x for x in range(1)]
print(numbers)




print("Geeks for Geeks!")

d = dict()

d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("Print numbers: " (i, d[i]))



t = ((1, 2), (3, 4), (5, 6))
for a, b in t:
    print(a, b)





fruits = ["apple", "banana", "cherry"]
colors = ["green", "yellow", "red"]
for fruit, color in zip(fruits, colors):
    print(fruit, "is", color)


for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print("Current letter: ", letter)

for letter in 'geeksforgeeks':
    if letter == 't' or letter == 'r':
        continue
    print("Current Letter: ", letter)



for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print("Current Letter :", letter)




for letter in 'geeksforgeeks':

    if letter == 'e' or letter == 's':
        break

print('Current Letter :', letter)






for i in range(1, 4):
    print(i)
else:
    print("No break\n")


for i in range(1, 4):
    print(i)
else:
    print("No break\n")


for i in range(0, 10):
    print(i)
else:
    print("getting better\n")



clothes = ["shirt", "sock", "pants", "sock", "towel"]
paired_socks = []
for item in clothes:
    if item == "sock":
        continue
    else:
        print(f"Washing {item}")
paired_socks.append("socks")
print("Washing {paired_socks}")


clothes.append("smartphone")
clothes.pop([-1])

clothes.remove([0])


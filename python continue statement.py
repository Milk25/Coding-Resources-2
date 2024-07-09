for var in "Geeksforgeeks":
    if var == "e":
        continue
    print(var)

# G k s f o r g k s


for i in range(1, 11):
    if i == 6:
        continue
    else:
        print(i, end=" ")


# 1 2 3 4 5 7 8 9 10



nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in nested_list:
    for j in i:
        if j == 3:
            continue
        print(j)

# 1 2 4 5 6 7 8 9


i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1


# 0 1 2 3 4 6 7 8 9




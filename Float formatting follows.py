# "{value:width.precision f}"
result = 100 / 777
result = 0.1287001287001287
print("The result was {}".format(result))
# The result was 0.12870012877001287



print("The result was {r}".format(r=result))
# The result was 0.12870012877001287


print("The result was {r:1.3f}".format(r=result))

# The result was 0.129

print("The result was {r:1.5f}".format(r=result))

# The result was 0.12870


result = 104.12345

print("The result was {r:1.2f}".format(r=result))
# The result was 104.12





name = "Jose"
print('Hello, his name is {}'.format(name))

# Hello, his name is Jose


print(f'Hello, his name is {name}')
# Hello, his name is Jose


name = "Sam"
age = 3

print(f'{name} is {age} years old.')
# Sam is 3 years ols.


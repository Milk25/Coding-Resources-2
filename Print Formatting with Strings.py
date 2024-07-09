my_name = "Jose"
print("Hello " + my_name)



2 : ways

.format() # Method
f-strings (formatted string literals)


print('This is a string {}'.format('INSERTED'))
# This is a string INSERTED


print('The {} {} {}'.format('fox', 'brown', 'quick'))
# The fox brown quick

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
# The quick brown fox

print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))
# The fox fox fox


print('The {q} {0} {f}'.format(f='fox', b='brown', q='quick'))
# The quick brown fox

print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))
# The fox fox fox



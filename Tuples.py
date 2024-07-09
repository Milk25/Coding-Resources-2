# immutability
# canot be reassigned



t = (1, 2, 3)

my_list = [1, 2, 3]

type(t)
# tuple

type(my_list)
# list

len(t)
# 3


t = ('one', 2)
t[0]
# one

t[-1] # 2


t = ('a', 'a', 'b')
t.count('a')
# 2
t.index('a')
# 0

t.index('b')
# 2

my_list[0] = 'NEW'
my_list # ['NEW', 2, 3]

t[0] = 'NEW' # TypeError


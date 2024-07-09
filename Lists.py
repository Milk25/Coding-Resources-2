# support indexing and slicing

my_list = [1, 2, 3]
my_list = ['STRING', 100, 23.3]

len(my_list) # 3


my_list = ['one', 'two', 'three']
my_list[0] # 'one'

my_list[1:]
# ['two', 'three']


another_list = ['four', 'five']

my_list + another_list

# ['one', 'two', 'three', 'four', 'five']

new_list = my_list + another_list

# ['one', 'two', 'three', 'four', 'five']


new_list[0] = 'ONE ALLCAPS'
new_list # ['ONE ALLCAPS', 'two', 'three', 'four', 'five']



new_list.append('six')

# ['ONE ALLCAPS', 'two', 'three', 'four', 'five', 'six']

new_list.append('seven')

# ['ONE ALLCAPS', 'two', 'three', 'four', 'five', 'six', 'seven']


new_list.pop()

# ['ONE ALLCAPS', 'two', 'three', 'four', 'five', 'six']

popped_item = new_list.pop()
popped_item # 'six'

new_list # ['ONE ALLCAPS', 'two', 'three', 'four', 'five',]



new_list.pop(0)

# ['two', 'three', 'four', 'five',]




new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

new_list.sort()

['a', 'b', 'c', 'e', 'x']



my_sorted_list = new_list.sort()
type(my_sorted_list)
# NoneType


new_list.sort()
my_sorted_list = new_list
# ['a', 'b', 'c', 'e', 'x']

num_list
# [4, 1, 8, 3]
num_list.sort()
# [1, 3, 4, 8]


num_list.reverse()
# [8, 4, 3, 1]





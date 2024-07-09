# unordered and can not be sorted
# key-value pairing


my_dict = {'key1': 'value1', 'key2': 'value2'}

my_dict['key1']
# 'value1'


prices_lookup = {'apple': 2.99, 'oranges': 1.99, 'milk': 5.80}

prices_lookup['apple']
# 2.99



d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insidekey: 100'}}

d['k2']
# [0, 1, 2]

d['k3']
# {'inside': 100}

d['k3']['insidekey']
# 100

d['k2'][2]
# 2


d = {'key1': ['a', 'b', 'c']}
my_list = d['key1']

my_list 
# ['a', 'b', 'c']



letter = my_list[2]

letter # 'c'

letter.upper() # 'C'



d['key1'][2].upper()
# 'C'



d = {'k1': 100, 'k2': 200}
d # {'k1': 100, 'k2': 200}

d['k3'] = 300

d # {'k1': 100, 'k2': 200, 'k3': 300}



d['k1'] = 'New Value'

d # {'k1': 'New Value', 'k2': 200, 'k3': 300}


d.keys()


dict_keys(['k1', 'k2', 'k3'])
d.values()
dict_values([100, 200, 300])


d.items()
dict_items([('k1', 100), ('k2', 200), ('k3', 300)])





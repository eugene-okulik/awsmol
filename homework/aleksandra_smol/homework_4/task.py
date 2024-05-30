my_dict = {
    'tuple': (1, 5, 3, 8, 9),
    'list': ['a', 'b', 'c', 'd', 'e'],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {5, "pu", 2.5, 6, 12}
}

print(my_dict['tuple'][-1])

my_dict['list'].append('f')
del my_dict['list'][1]

my_dict['dict'][('i am a tuple',)] = 'not turtle'
del my_dict['dict']['b']

my_dict['set'].add(42)
my_dict['set'].remove(2.5)

print(my_dict)

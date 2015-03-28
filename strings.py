dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasagna'},
    {'name': 'Walter',
     'food': 'pancackes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

my_string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(a_dict, a_string):
    return_list = []
    for key in a_dict:
        return_list.append(a_string.format(**key))
    
    return return_list
        
my_list = string_factory(dicts, my_string)
print(my_list)
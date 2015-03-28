my_dict = {'apples': 1, 'bananas': 2, 'coconuts': 3}
my_list = ['apples', 'coconuts', 'grapes', 'strawberries']

def members(a_dict, list_keys):
    count = 0
    for item in list_keys:
        try:
            a_dict[item]
            count = count + 1
        except:
            continue

    return count
    
print(members(my_dict, my_list))

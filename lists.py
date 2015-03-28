the_list = ["a", 2, 3, 1, False, [1, 2, 3]]

the_list.insert(0, the_list.pop(3))

del the_list[1]
del the_list[3]
del the_list[3]

the_list.extend(range(4,21)

for item in the_list:
    print(item)
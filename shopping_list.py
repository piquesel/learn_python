shopping_list = []

print("What should we pick up at the store?")
print("Enter 'DONE' to stop adding items.")

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    shopping_list.append(new_item)
    print("Added: list has {} items".format(len(shopping_list)))
    continue

print("Here is your list:")
for item in shopping_list:
    print(item)
    
print(' '.join(shopping_list))

full_name = "Bruno Rouchouse"
name_list = full_name.split(' ')
greeting_list = "Hi, I'm Treehouse".split()
greeting_list[2] = full_name.split()[0]
greeting = greeting_list.join()
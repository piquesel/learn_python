def word_count(a_string):
    a_dict = {}
    new_string = a_string.lower()
    list_words = new_string.split()
    for word in list_words:
        print(word)
        if word in a_dict:
            a_dict[word] += 1
        else:
            a_dict[word] = 1
    return a_dict
    
my_string = "I am what I am"
my_dict = word_count(my_string)
print(my_dict)
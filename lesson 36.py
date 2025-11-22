# Iterables = An object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop


my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


# ============ Tuple ================

my_tuple = (1, 2, 3, 4, 5)

for item in my_tuple:
    print(item)


# ============ Set ================

my_set = {"apple", "orange", "banana", "coconut"}

for item in my_set:
    print(item)


# ============ String ================

my_name = "Bro Code"

for item in my_name:
    print(item)


# ============ Dictionary ================

my_dictionary = {'A': 1, 'B': 2, 'C': 3}

for key in my_dictionary:
    print(key)

for value in my_dictionary.values():
    print(value)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
# collection = single "variable" used to store multiple values
#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# ============ List ================
# fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# print(fruits.count("banana"))

# print(fruits[0:3])
# print(fruits)

# for fruit in fruits:
    #print(fruit)



# ============ Set ================

# fruits = {"apple", "orange", "banana", "coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()

# print(fruits)

# for fruit in fruits:
    #print(fruit)



# ============ Tuple ================

# fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)

# for fruit in fruits:
    #print(fruit)
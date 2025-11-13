# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# age = age + 1


# print(f"Hello {name}")
# print(f"You are {age} years old")



# ============ EXERCISE 1 ================

# adjective1 = input("Enter an adjective: ")
# noun = input("Enter an noun: ")
# adjective2 = input("Enter an adjective: ")
# verb = input("Enter an verb: ")
# adjective3 = input("Enter an adjective: ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw {noun}")
# print(f"{noun} are {adjective2} and {verb}ing.")
# print(f"I was {adjective3}.")


# ============ EXERCISE 2 ================

# length = float(input("Enter the length of a rectangle:"))
# width = float(input("Enter the width of a rectangle:"))
# height = float(input("Enter the height of a rectangle:"))

# volume = length * width * height

# print(f"The volume is: {volume}cm^3")


# ============ EXERCISE 3 ================

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like to buy?: "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${round(total, 2)}")
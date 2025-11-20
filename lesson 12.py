# String Methods


# name = input("Enter your name: ")

# result = len(name)
# result = name.find(" ")
# result = name.rfind("s")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()

# print(result)
# print(name)


# phone_number = input("Enter your phone #: ")

# result = phone_number.count("-")
# phone_number = phone_number.replace("-", "")

# print(result)
# print(phone_number)

# ============ EXERCISE 1 ================

# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
   print("Your name can't be more than 12 characters")
elif not username.find(" ") == -1:
   print("Your username can't contain spaces")
elif not username.isalpha():
   print("Your username can't contain digits")
else:
   print(f"Welcome {username}!")
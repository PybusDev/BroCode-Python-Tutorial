# if _name_ == __main__: (this script can be imported OR run standalone)
#                         Functions and classes in this module can be reused 
#                         without the main block of code executing

# ex. library = Import library for functionality
#               When running library directly, display a help page

# if _name_ == '__main__':
#     main()

# This file should run only standalone

from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

print("We are on Script2 now")
favorite_food("sushi")
favorite_drink("coffee")
print('Goodbye!')
# keyword arguments = arguments prefixed with the names of parameters
#                     order of the arguments doesn’t matter
#                     helps with readability
#                     1. positional, 2. default, 3. KEYWORD, 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")


# ============ EXERCISE 2 ================
for number in range(1, 11):
    print(number, end=" ")

print("1", "2", "3", "4", "5", sep="-")


# ============ EXERCISE 3 ================
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)
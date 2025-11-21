# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. ARBITRARY


# ================ *ARGS EXAMPLE 1 ================
def add(*nums):
   total = 0
   for num in nums:
       total += num
   return total

print(add(1, 2, 3, 4))


# ================ *ARGS EXAMPLE 2 ================
def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


# ================ **KWARGS ================
def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")


# ============ EXERCISE 1 ================
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")
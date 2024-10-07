# day = "wednesday"
# age = 22
# discount = 2
# adult = 12
# children = 8
# if age < 18 and day == "wednesday":
#     print(children - discount)
# elif age >= 18 and day == "wednesday":
#     print(adult - discount)
# elif age < 18:
#     print(children)
# elif age >= 18:
#     print(adult)

age = 26
day = "Wednesday"

price = 12 if age >= 18 else 8

if day == "Wednesday":
    # price = price - 2
    price -= 2

print("Ticket price for you is $",price)
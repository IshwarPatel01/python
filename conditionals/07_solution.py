order_size = "small"
extra_shots = False

if extra_shots:
    coffee = order_size + " coffee with extra shots"
else:
    coffee = order_size + " coffee"

print(coffee)
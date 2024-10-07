password = "hell!"

if 10 < len(password):
    pass_Strength = "Strong"
elif 6 <= len(password):
    pass_Strength = "Medium"
else:
    pass_Strength = "Weak"

print(pass_Strength)
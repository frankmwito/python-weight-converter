# Python weight converter

weight = float(input("Enter your weight:"))
unit = input("kilograms or pounds? (K or L):")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {weight} {unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"Your weight is {weight} {unit}")
else:
    print(f"{unit} was not valid")
    

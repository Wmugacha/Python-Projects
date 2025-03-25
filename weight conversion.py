# Weight Conversion Program

weight = float(input("What is you weight? "))
unit = input("Kilograms or Pounds? (Kg or P): ")

if unit == "Kg":
    weight = weight * 2.205
    units = "Pounds"
    print(f"your weight is {round(weight, 2)} {units}")
elif unit == "P":
    weight = weight / 2.205
    units = "Kgs"
    print(f"your weight is {round(weight, 2)} {units}")
else:
    print(f"{unit} is not a valid weight")
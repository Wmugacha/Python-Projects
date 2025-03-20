# Temparature Conversion Program

temp = float(input("Enter the current temparature: "))
unit = input("Is it in Degree Celcius of Farenheit (C or F: )")

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The current temparature is {temp} Degress Farenheit")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The current temparature is {temp} Degrees Celcius")

else:
    print(f"{unit} is not a valid unit of measurement")
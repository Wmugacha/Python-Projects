#Consession Stand Program
menu = {"Pizza" : 800,
        "Soda" : 100,
        "Popcorn" : 150,
        "Ice Cream": 300,
        "Nachos": 250,
        "Chips" : 200,
        "Fries": 350,
        "Chicken" : 1200}

selection = []
total = 0

print("---------MENU----------")
for food, price in menu.items():
    print(f"{food:10}: {price}")

while True:
    food = input("Please select a food item(Enter Q to quit): ").title()
    if food == "Q":
        break
    elif menu.get(food) is not None:
        selection.append(food)

print("-------YOUR ORDER----------")
for food in selection:
    total += menu.get(food)
    print(food, end=" ")

print("")
print(f"Your total bill is Ksh {total}.")
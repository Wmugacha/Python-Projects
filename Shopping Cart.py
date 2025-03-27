#Shopping Cart Program

Foods = []
Prices = []
total = 0

while True:
    food = input("please enter a food item(Enter Q to Quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input("Please input the price of the food item: "))
        Foods.append(food)
        Prices.append(price)

print("--------YOUR SHOPPING CART---------")

for food in Foods:
    print(food, end=" ")

for price in Prices:
    total += price

print()
print(f"Your Total is {total}")
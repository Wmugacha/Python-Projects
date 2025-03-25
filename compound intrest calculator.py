# Compound Intrest Calculator

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Please input the principal amount: "))
    if principal < 0:
        print("Please enter a valid principal amount")
    else:
        break

while True:
    rate = float(input("Please input the interest rate: "))
    if rate < 0:
        print("Please Enter a valid rate")
    else:
        break

while True:
    time = int(input("Please input the time: "))
    if time < 0:
        print("Please enter a valid time period(Year(s))")
    else:
        break

total = principal * pow((1 + rate / 100), time) # Compounded Yearly
quarterly = principal * pow((1 + rate / (100 * 4)), 4 * time) #Compounded quarterly
monthly = principal * pow((1 + rate / (100 * 12)), 12 * time) #Compounded Monthly

print(f"Balance after {time} years is {total:.2f} Ksh.")
print(f"Balance compounded quarterly after {time} years is {quarterly:.2f} Ksh.")
print(f"Balance compounded monthly after {time} years is {monthly:.2f} Ksh.")
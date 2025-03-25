# Compound Intrest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Please input the principle amount: "))
    if principle < 0:
        print("Please enter a valid principle amount")
    else:
        break

while True:
    rate = float(input("Please input the interest rate: "))
    if rate < 0:
        print("Please Enter a valid rate")
    else:
        break

while time <=0:
    time = int(input("Please input the time: "))
    if time < 0:
        print("Please enter a valid time period(Year(s))")
    else:
        break

total = principle * pow((1 + rate / 100), time) # Compounded Yearly

print(f"Balance after {time} years is {total:.2f} Ksh.")
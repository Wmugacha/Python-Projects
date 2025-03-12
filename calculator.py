#Calculator program

operator = input("Please enter an operator *, +, /, -: ")

num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))

elif operator == "-":
    result = num1 - num2
    print(round(result, 3))

elif operator == "*":
    result = num1 * num2
    print(round(result, 3))

elif operator == "/":
    result = num1/num2
    print(round(result, 3))

else:
    print (f"{operator} is not a valid operator")
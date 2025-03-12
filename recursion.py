def greet():
    print("Hello")
    #greet()

greet()

def fibonacci(idx):
    seq = [0,1]
    for i in range(idx - 1): #running the loop idx times will generate an extra number
        seq.append(seq[-1] + seq[-2])
    return seq[-1]

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx - 1) + Fibonacci(idx -2)

print(Fibonacci(8))
print(fibonacci(8))
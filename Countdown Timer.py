#Countdown Timer Program
import time

my_time = int(input("Enter time in seconds: "))

for x in range (my_time, 0, -1):
    seconds = x % 60
    minutes = int(x % 3600) // 60
    hours = int(x // 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("TIME'S UP!!!")
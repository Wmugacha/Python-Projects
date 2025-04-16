# Python Banking Program

def show_balance(balance):
    print(f"Your balance is {balance:.2f} Ksh")

def deposit():
    amount = float(input("How much would you like to deposit?: "))

    if amount < 0:
        print("Invalid Amount!!!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("How much would you like to withdraw?: "))

    if amount <= 0:
        print("Invalid Amount")
        return 0
    elif amount > balance:
        print("insufficient funds!!")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("What do you want to do?: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Please enter a valid choice")

    print("Thank you, Have a nice day")

if __name__ == "__main__":
    main()
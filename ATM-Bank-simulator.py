print("=== ATM Simulation ===")

balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Balance: R", balance)

    elif choice == "2":
        amount = float(input("Deposit Amount: R"))
        balance += amount
        print("Deposit Successful!")

    elif choice == "3":
        amount = float(input("Withdraw Amount: R"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Funds.")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid Option."
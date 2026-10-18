
balance = 1000
print("---Welcome to python ATM---")
Pin = 9763

attempt = 0

while attempt < 3:
    pin = int(input("Enter your pin:"))
    if pin == Pin:
        print("-- Your options are --")
        print("check balance.")
        print("2. Deposit.")
        print("3. withdraw.")
        print("4. Change Pin.")
        print("5. Exit")
        choose = input("enter your choice:")
        break
    else:
        attempt += 1
        print(f"Invalid pin. Attempt left: {3-attempt}")

if attempt == 3:
    print("Too many in correct attempt, Account locked.")
    exit()

if choose == "1":
    print(f"your current balance is: {balance}.")
elif choose == "2":
    amount = float(input("Emter the amount you want to deposit:"))
    balance = balance + amount
    print("deposited succesfully!")
    print(f"your current balance is {balance}.")
elif choose == "3":
    amount = float(input("enter the amount you want to withdraw:"))
    if amount > balance:
        print("sorry, insufficient amount.")
    else:
        balance = balance - amount
        print("withdrawal succesful!")
        print(f"your current balance is {balance}.")
elif choose == "4":
    pin = int(input("enter your current pin:"))
    if pin == Pin:
        new_pin = int(input("Enter your new pin."))
        Pin = new_pin
        print("pin changing succesful!")
    elif pin != Pin:
        print("Invalid pin.")
elif choose == "5":
    print("Thank you for using python ATM.")
    
while True:
    balance = 1.0
    try:
        num = float(input("Enter amount: "))
        break
    except ValueError:
        print("Invalid amount, try again:")

balance += num
print(f'Balance: {balance} $')

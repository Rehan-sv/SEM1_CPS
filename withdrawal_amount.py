
balance = int(input("Enter your account balance: "))
withdrawal_amount = int(input("Enter withdrawal amount (0 to stop): "))
while withdrawal_amount != 0:

    if withdrawal_amount <= balance:
        balance -= withdrawal_amount
        print("Withdrawal successful, Remaining Balance:", balance)
    else:
        print("Insufficient Balance")

    withdrawal_amount = int(input("Enter withdrawal amount (0 to stop): "))

# Step 5: Print final balance
print("Final Balance:", balance)

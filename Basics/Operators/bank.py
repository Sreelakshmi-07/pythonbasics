fixed_amount = 30000
withdrawn = int(input("Amount to withdraw: "))
if withdrawn < fixed_amount:
    print("Available balance ", fixed_amount-withdrawn)
else:
    print("Insufficient balance")
account_type=input("Is the account Standard or premium:")
amount=float(input("Enter amount:"))
if account_type=="Standard" :
    if amount>500:
        print("Transaction exceeds the limit for Standard account")
    else:
        print("Transaction approved")
elif account_type=="Premium":
    if amount>1000:
        print("Transaction exceeds the limit for Standard account")
    else:
        print("Transaction approved")
else:
    print("Invalid account")
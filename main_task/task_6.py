#Write a program that lets the user input a password.
#Give them only 4 attempts to check the passwords entered against “admin@123”.
#If the password is correct access is granted.
#After you show them a message , the account is blocked."""
password=int(input("Enter password"))
Correct_password="admin@123"
count=0
if password==Correct_password:
    print("Access granted")
    if count==4:
        break
        print("The account is blocked")
else:
    print("Access not granted")
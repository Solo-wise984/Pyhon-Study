#Write a program that takes the email and password as input from a user and checks 
# if they are equal to “admin@mail.com” and password is “Admin@123” ,
# if so then print  “Login is Successful” and if not print “Invalid username or password”.
# ONLY accept 3 tries after which it notifies you that you have been blocked.

correct_email="admin@email.com"
correct_password="Admin@123"
email=input('Email address').strip().capitalize()
password=input('Password').strip()
count=0
if email in correct_email==true:
    if password in correct_password==true:
        print("Login is Successful")
    else:
        count+=1
        print(f"Invalid username or password. Attempts remaining: {3-count}")
        if count==3:
            print("You have been blocked. Please try again later.")
            
else:
    print("Try again later")

if 20>10:
    print('20 is greater')
if 10>40:
    print('10 is greater')  
else:
    print('40 is greater')
    
marks=340
if marks>300 and marks<350:
    print("Pass")
else :
    print("Fail")

num=55
if num%2==0:
    print("even")
else:
    print("odd")
    
marks=int(input("enter your marks"))
if marks >=90 and marks<=100 :
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print ("C")
elif marks>=60 and marks <70:
    print("D")
elif marks>=50 and marks<60:
    print("E")
else :
    print("Failed")
        
Age=int(input("enter ur age"))
if Age>=60:
     print(" You are older")
elif Age>=18 and Age<=59 :
    print("You are an adult")
else:
    print( "You are a minor")




age =int(input('enter you age '))
if age>=18:
    license=input("do you have a license yes/no : ").strip().lower()
    if license=='yes':
        print("Your are eligible")
    else:
        print("Click the button bellow to continue")
else :
    print("you are too young to drive")
    




credit=int(input("enter you income credit"))
if credit>=700:
    income_money=int(input("What is your income a month"))
    if income_money>=50000:
        print("Loan approved")
    else:
        print("Income requirement not met")
else:
    print("Credit score too low")
    


#1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".





#2.Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".
text1="Hello, world"
text2="Hello"
if len (text1) > len (text2):
    print("str1 is longer")
elif len(text2)>len(text1):
    print("str2 is longer")
else:
    print("Both are of eaquals")




#3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
#Prints "Access Granted" if user_id is in valid_ids.
#Prints "Access Denied" if user_id is not in valid_ids.
users_id=int(input("Enter id:"))
valid_ids=[101,102,103]
if users_id in valid_ids== True:
    print("Access Granted")
else:
    print("Acces Denied")

#4.Given a variable value that could be of any type, write a conditional statement that:
#Prints "String Detected" if value is a string.
#Prints "Integer Detected" if value is an integer.
#Prints "Unknown Type" for any other type.
variable=input("enter a text:")
if (type(variable)) == str :
    print("String detected")
elif (type( variable)) == int:
    print("Interger detected")
else:
    print("unknown type")

#5.Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#"Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.
num_x=int(input("Enter a number:"))
num_y=int(input("Enter a number:"))
if num_x%2==0 and num_y%2==0:
    print("They are even")
elif num_x%2==0:
    print("num_x is even")
elif num_y%2==0:
    print("num_y is even")    
else:
    print("There are both odd")



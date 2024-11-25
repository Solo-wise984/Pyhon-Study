num1=10
num2=20
total=num1+num2
print(total)
text="Solomon is a good child"
#print(text::-1)
#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”
name='  Jomes  '
print(name.strip())
#concatinanting
fname="Solomon"
lname="Macharia"
fullname=fname+" "+lname
print(fullname)
print(fullname.upper())
print(fullname.lower())
#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_one = 'The Dog Breed is German Shepherd'
print(sentence_one[8:23])
sentence_two ='Defeats for the Clinton forces, this was her moment of triumph'
print(sentence_two[16:31])
first_name="  Joh.n"  
last_name="   Do,e"
#Clean up and display Full name i.e John Doe
cleaned_fname=first_name.replace('.','')
cleaned_lname=last_name.replace(',','')
fullname=cleaned_fname.strip()+" "+cleaned_lname.strip()
print(fullname)

trainees = ["John", [2, ["James","Mary"]]]
print(trainees[1][0])
print(trainees[1][1][0])
#trainees.insert(56)[1][1][2]
trainees.append(56)
print(trainees)
# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
age=int(input('Enter your age: '))
if age >= 18:
    license=input('Do u have a license Yes/No?')
    if license=='Yes':
        print("Dear client drive safely!")
    else:
        print("Dear client u r eligible for license!")
else:
    print("you are too young to drive!")  
    
#Take three inputs from a user, separately. Print the largest of the numbers.
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
num3=int(input('Enter third number: '))
if num1>num2 and num1>num3:
    print ('The first number is the largest!')
elif num2>num1 and num2>num3:
    print('The second number is the largest')
else:
    print('The third number is the largest!')

#Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temp=float(input('Enter the temperatures of today: '))
if temp>30:
    print('The temperatures are too high!')
elif temp>15 and temp< 30:
    print('Normal temperatures')
else:
    print('Cold temperatures!')
    
    
class Temp:
    def __init__(self,temperatures):
        self.temp=temperatures
    def display(self):
        if self.temp>30:
            return "The temperatures are too high!"
        elif temp>15 and temp< 30:
            return  "Normal temperatures"
        else:
            return "Cold temperatures!"
user_temp=float(input('Enter the temperatures of today: '))
Temperatures=user_temp
#print(Temperatures.display())
    
#Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
x=int(input('Enter a number: '))
if x >=10 and x <=20:
    print('The number is between 10 and 20')
else:
    print('This number is not between 10 and 20')
    
    
#class
class Number:
    def __init__(self,number):
        self.num=number
    def display(self):
        if x >=10 and x <=20:
            return 'The number is between 10 and 20'
        else:
            return 'This number is not between 10 and 20'
user_num=int(input('Enter a number: '))
numw=user_num
#print(numw.display())
        
        
#nd if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
# Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"

correct_passward="secret123"
password=int(input("Enter password"))
if password==correct_passward:
    print("Access granted")
else:
    print("Access denied")

        
 #Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
 
 
#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
#Create a function that calculates the total marks another the average marks ,then a functions that finds the grade according to the table below. 

#Use the value from total to get the average and average to find the grade.

#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40


##loops
#Write a program that displays a numbers 1 to 50 inside a list.
numbers=list(range(1,51))
print(numbers)
#From 1 above display the ones divisible by 7 or 5 inside a list.
X=[]
for i in numbers:
    if i %5==0 or i %7==0:
        x.append(i)
        print(x)
#Find sum and average of values in the range between 10 to 40.
#Put in a list the first 10 odd numbers between 10 to 50. 
#write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
#write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
#ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
#Display the total quantity of the 3 above.



 
        


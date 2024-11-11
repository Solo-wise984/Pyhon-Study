
def total_marks (maths,eng,swa,sci,sos):
    sum=(maths+eng+swa+sci+sos)
    return sum

def average_marks(maths, eng, swa, sci, sos):
    average = ((maths + eng + swa + sci + sos) / 5)
    return average

def grade(average = ((maths + eng + swa + sci + sos) / 5)): # type: ignore
    grade = average
    if grade > 79:
        print("Grade: A")
    elif grade  >= 60 and grade  <= 79:
        print("Grade: B")
    elif grade >= 49 and grade <60:
        print("Grade: C")
    elif grade >= 40 and grade<49:
        print("Grade: D")
    else:
        print("Grade E")

print("Running main function")
maths=int(input("Enter mathematics marks: "))
eng=int(input("Enter english marks: "))
swa=int(input("Enter kiswahili marks: "))
sci=int(input("Enter science marks:  "))
sos=int(input("Enter social marks: "))

print(total_marks(maths,eng,swa,sci,sos))
print(average_marks)
print(average_marks(maths,eng,swa,sci,sos))




#Write a Python program that calculates the Body Mass Index (BMI) of a user. 
# The program should take the user's weight in kilograms and height in meters as inputs.
# Create a function to calculate BMI and another function to determine the BMI category based on the following criteria:

#Underweight: BMI < 18.5
#Normal weight: 18.5 <= BMI < 24.9
#Overweight: 25 <= BMI < 29.9
#Obesity: BMI >= 30


weight=int(input("Enter weight in kilograms: "))
height=float(input("Enter your height in meters: "))
def BMI(weight,height):
    bmi=weight/(height*height)
    return bmi
print(BMI(weight,height))

def BMI_category(weight,height):
    category=weight/(height*height)
    if category < 18.5:
        print("Undeweight")
    elif category >= 18.5 and category <= 24.9:
        print("Normal weight")
    elif category >=25 and category <=29.0:
        print("overweight")
    else  :
        print("Obesity")
print(BMI_category(weight,height))
        
    
    



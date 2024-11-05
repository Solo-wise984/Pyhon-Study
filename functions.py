#function to create a triangle
def triangle_area():
    base=20
    height=40
    area=(base*height)*0.5
    return area
triangle_area()

#function that calculates the area of a rectangle
def rectangle_area():
    length=20
    width=24
    area=length*width
    return area
rectangle_area()

#area of a triangle using parameters and arguments
def area_traingle(a,b):
    area=((a*b)*0.5)
    return area
area_traingle(20,50)
x=area_traingle(10,5)
print(x)

#write a function that going to check if aa number is even or odd number

def check_number(num):
    if num % 2 == 0:
        result= "Even"
    else:
        result= "Odd"
    return result
value=check_number(22)
print(value)

#Write a program that prints the largest of 4 inputs taken in from a user.
# Assume that the user would not enter any two numbers which are the same.
user_input1=int(input("Enter first number: "))
user_input2=int(input("Enter second number: "))
user_input3=int(input("Enter third number: 23" ))
user_input4=int(input("Enter fourth number: "))


if user_input1 >  user_input2 and user_input1 > user_input3 and user_input1 > user_input4:
    largest = user_input1
elif user_input2 > user_input1 and user_input2 > user_input3 and user_input2 > user_input4:
    largest = user_input2
elif user_input3 > user_input1 and user_input3 > user_input2 and user_input3 > user_input4:
    largest = user_input3
else:
    largest = user_input4

print(largest)


if user_input1 >  user_input2 and user_input1 > user_input3 and user_input1 > user_input4:
    print(f"{user_input1} is the largest")
elif user_input2 > user_input1 and user_input2 > user_input3 and user_input2 > user_input4:
    print(f"{user_input2} is the largest")
elif user_input3 > user_input1 and user_input3 > user_input2 and user_input3 > user_input4:
    print(f"{user_input3} is the largest")
else:
    print(f"{user_input4} is the largest")
    
    
def check_largest(user_input1, user_input2, user_input3, user_input4 ):
    if user_input1 >  user_input2 and user_input1 > user_input3 and user_input1 > user_input4:
        largest = user_input1
        print(f"{user_input1} is the largest")
        
        
    largest = max(user_input1, user_input2, user_input3, user_input4)

    

    
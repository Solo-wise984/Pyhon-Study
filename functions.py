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
class Triangle:
    def __init__ (self,length,width):
        self.l=length
        self.w=width
    def area(self):
        result=self.l*self.w
        return f"The area of the triangle {result} is"
triangle=Triangle(22,13)
print(triangle.area())

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
user_input3=int(input("Enter third number: " ))
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

def display_message()   :
    message='you are learning a  new chapter'
    return message
display_message()


def favourite_book():
    title='Alice in Wonderland'
    text="One of my favorites books is "
    return f"{text} {title}"
print(favourite_book())

def make_shirt():
    size=int(input('Enter the size of the T-shirt'))
    text='Your T-shirt size is :'
    return f'{text} {size}'
print(make_shirt())


class Animal:
    def __init__ (self, animal,sound):
        self.animal=animal
        self.sound=sound
    def describe(self):
        return f'{self.animal} makes this {self.sound} sound'
animal=Animal('Cow','Moos')
print(animal.describe())
        
    
class Shapes:
    def area (self):
        return 0
#rectangle
class Rectangle:
    def __init__ (self,width,length):
        self.w=width
        self.l=length
    def calculation(self):
        result=self.w*self.l
        return "The area of the rectangle is :{result}"
#circle
class Circle:
    def __init__ (self,formula,radius):
        self.f=formula
        self.r=radius
    def calculation(self):
        result={self.f}*{self.r}*{self.r}
        return 'The area of the circle is: {result}'
#value of the rectangle
def get_value():
    width=int(input('Enter the width value: '))
    length=int(input('Enter the value of length: '))
    return Rectangle(width,length)
#value of the circle
def get_value():
    formula=float(input("Enter the formula to be used: "))
    radius=int(input('Enter the value of the radius: '))
    return Circle(formula,radius)


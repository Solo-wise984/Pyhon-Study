from turtle import right, width


num=[1,2,3,4]
print(type(num))#class list
num.append(5)





class Car:
    def __init__(self,color,brand,model):
        self.cl=color
        self.br=brand
        self.mdl=model
        
    def describe(self):
        return f"The color of the car is {self.cl} and the brand is {self.br} and the model is {self.mdl}"
#create object    
my_car=Car('green','Mazda','CX5')
print(my_car.describe())


my_car2=Car('yellow','BMW','X series')
print(my_car2.describe())


#Create a class called Student with attributes name and age.
#Add a method introduce that prints: "Hello, my name is [name] and I am [age] years old."
#Create an object of Student and call the introduce method.

class Student:
    def __init__(self,name,age):
        self.nm=name
        self.a=age
    def describe(self):
        return f"Hello, my name is {self.nm} and I am {self.a} years old."
Student1=Student('Solomon Macharia','18')
print(Student1.describe())

#Define a class Calculator with methods add, subtract, multiply,
# and divide that perform the respective operations on two numbers.
#addition
class Calculator:
    def __init__(self,add):
        self.ad=add
    def result(self):
        return f"The sum of 12 and 4 is: {self.ad}"
answer=Calculator(12+4)
print(answer.result())

#subtraction
class Calculator:
    def __init__(self,subtraction):
        self.sub=subtraction
    def result(self):
        return f"The difference of 12 and 4 is: {self.sub}"
answer1=Calculator(12-4)
print(answer1.result())

#multiplication
class Calculator:
    def __init__(self,multiply):
        self.mult=multiply
    def result(self):
        return f"The multiplication of 12 and 4 is: {self.mult}"
answer2=Calculator(12*4)
print(answer2.result())

#division
class Calculator:
    def __init__(self,divide):
        self.div=divide
    def result(self):
        return f"The division of 12 and 4 is: {self.div}"
answer3=Calculator(12/4)
print(answer3.result())

#new method
class Calculator:
    def __init__(self,number1,number2):
        self.num1=number1
        self.num2=number2
    def add(self):
        return f"The sum of 12 and 4 {self.num1}+{self.num2}"
    def subtraction(self):
        return f"The difference of 12 and 4 {self.num1}+{self.num2}"
    def divide(self):
        return f"The division of 12 and 4 {self.num1}+{self.num2}"
    def multiplication(self):
        return f"The multiplication of 12 and 4 {self.num1}+{self.num2}"

        

#Create a class Animal with attributes species and sound.Add a method make_sound that prints: 
# "The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.

class Animal:
    def __init__(self,species,sound):
        self.spe=species
        self.so=sound
    def describe(self):
        return f"The {self.spe} goes {self.so}"
creature=Animal('cow','moos')
print(creature.describe())

#Create a class Book with attributes like title, author, and year.
#Add a method that returns a description of the book.
#Create an object of Book and print out the description.

class Book:
    def __init__(self,title,author,year):
        self.tit=title
        self.aut=author
        self.yr=year
    def description(self):
        return f"The book {self.tit } was written {self.aut} in the year {self.yr}"
set_book=Book('Blossoms of The Savannah','Solomon Macharia','2014')
print(set_book.description())
    

#Define a class BankAccount with attributes owner and balance (set balance to 0 by default).
# Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
#Ensure that the withdraw method does not allow the balance to go negative.

class BankAccount:
    def __init__(self,owner, balance) :
        self.own=owner
        self.bal=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Confirmed {amount} has been deposited .Ur new balance is {self.bal}"
        else:
            "Deposite a higher amount"
    #Withdraw
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return f"{self.own} you have successfully withdrawn {amount} and your new balnce is {self.bal}"
        else:
            return f"{self.own} you have insufficient balance to withdraw"
        
    #balance
    def get_balance(self):
        return f"{self.own} your balance is {self.bal}"        
    
BankAccount('Solomon Macharia')
person1.deposit(5000000)
person.withdraw(5000)
print(perain_get_balance())



#Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# Instantiate a few rectangle objects and print their area and perimeter.
class Rectangle:
    def __init__(self,width,height):
        self.w=width
        self.h=height
    def area(self):
        return f"The area of the rectangle with  is :{self.w}*{self.h} is: "
    def perimeter (self):
        return f"The perimeter of the rectangle is : {self.w}+{self.h}+{self.w}+{self.h}"
diamensions=Rectangle(15,20)
print(diamensions.perimeter())
print(diamensions.area())

#Create a class Employee with attributes name and salary.
# Add a method give_raise that increases the salary by a given percentage.
# Instantiate an employee, give them a raise, and display their new salary.
class Employee:
    def __init__(self,name,salary):
        self.nm=name
        self.sal=salary
    def give_raise (self,percentage):
        new_salary+=self.sal*(percentage/100)
        return f"{self.nm} your  salary is {self.sal} and your new salary is {new_salary}" 
print(new_salary.give_raise()) # type: ignore
        
        
    
    
    
#Create a base class Vehicle with attributes brand and model.
#Create two subclasses Car and Motorcycle that inherit from Vehicle and add unique methods to each subclass (e.g., honk for Car and rev_engine for Motorcycle).
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def describe(self):
        return f"This vehicle is a {self.brand} brand and {self.model} model"
class Car :
    def __init__(self,brand,model):
         self.brand=brand
         self.model=model
    def describe_car(self):
        return f"The car is a {self.brand} and {self.model} honk honk !!"
class Motorcycle:
    def __init__(self,brand,model):
         self.brand=brand
         self.model=model
    def describe_motocycle(self):
        return f"The motocycle is a {self.brand} and {self.model} and it has a rev_engine !!"
vehicle=Vehicle(BMW,Xseries)# type: ignore
print

    
    
    
    

    
    
    
        
        
        
        
  
    
        
    
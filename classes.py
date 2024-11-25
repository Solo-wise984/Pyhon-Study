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
    
#BankAccount('Solomon Macharia')
#person1=deposit(5000000)
#person.withdraw(5000)
#print(perain_get_balance())

banks=BankAccount('Solomon Macharia','1000000')





#Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# Instantiate a few rectangle objects and print their area and perimeter.
class Rectangle:
    def __init__(self,width,height):
        self.w=width
        self.h=height
    def area(self):
        return f"The area of the rectangle with  15 and 20 is {self.w}*{self.h} is: "
    def perimeter (self):
        sum=self.w+self.w+self.h=self.h
       
        return f"The perimeter of the rectangle is {self.sum}: 
print(diamensions.perimeter())
print(diamensions.area())

#Create a class Employee with attributes name and salary.
# Add a method give_raise that increases the salary by a given percentage.
# Instantiate an employee, give them a raise, and display their new salary.
class Employee:
    def __init__(self,name,salary):
        self.nm=name#atribute
        self.sal=salary
    def give_raise (self,percentage):
        self.sal+=self.sal*(percentage/100):
          return f "Your new salary {self.sal}"
        
employee1=Employee("Solomon Macharia",2000000) 
    
print(employee1.give_raise(20))

        
    
    
    
#Create a base class Vehicle with attributes brand and model.
#Create two subclasses Car and Motorcycle that inherit from Vehicle and add unique methods to each subclass (e.g., honk for Car and rev_engine for Motorcycle).
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def describe(self):
        return f"This vehicle is a {self.brand} brand and {self.model} model"
class Car(Vehicle):
    
    def __init__(self,brand,model):
        super().__init__(brand,model)
         
    def hock(self):
        return f"The car is a {self.brand} and {self.model} honk honk !!"
class Motorcycle (Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand,model)
         
    def rev_engine(self):
        return f"The motocycle is a {self.brand} and {self.model} and it has a rev_engine !!"

car=Car('BMW','Xseries')
motorcycle=Motorcycle("ducati","772")
print(car.hock())
print(motorcycle.rev_engine())

    

#Write a program that takes input of someone's basic salary and benefits, adds them to fin
#d the gross salary then uses  the gross salary to find the NHIF

class Salary :
    def __init__(self,basic_salary,benefits):
        self.bs=basic_salary
        self.bn=benefits
    def gross_salary(self):
        return f"Your  gross salary is {self.bs} + {self.bn}: "
salary=Salary(100000,5000)
print(salary.gross_salary())
        

#TASK 16: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
class NSSF :
    def __init__(self,gross_salary):
        self.gross=gross_salary
    def NSSf_rate(self):
        rate=self.gross*(6/100)
        return f"The NSSF rate is {rate}* "
print(rate.NSSF_rate())
    

#Write a normal program but use functions if you feel comfortable.

#Task 17: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and calculate an individual’s NHDF using:
#i.e NHDF = gross_salary *  0.015
class NHDF:
    def __init__ (self,gross_salary):
     self.gross=gross_salary
    def NHDF(self):
        result=self.gross*0.015
        return f"The NHDF is {result}"
print(result.NHDF())

#Write a normal program but use functions if you feel comfortable.

#Task 18: Using Python or PHP or Java or Ruby or JavaScript
#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
class Taxable_income:
    def __init__ (self,gross_salary,NHDF,NSSF):
        self.gross=gross_salary
        self.NH=NHDF
        self.NS=NSSF
    def taxable_income(self):
        total
    

#Write a normal program but use functions if you feel comfortable.

#TASK 19: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and find the person's PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK
#write a normal program but use functions if you feel comfortable.

#Task 20: Using Python or PHP or Java or Ruby or JavaScript
#Continue with the same program and calculate an individual’s Net Salary using:
#net_salary = gross_salary - (nhif + nhdf +  nssf + payee)

    
    
    
        
        
        
        
  
    
        
    
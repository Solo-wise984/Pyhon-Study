print('Hello word')
fname='Solomon'
lname='Macharia'
full_name=fname+" "+lname
print(full_name)
print(full_name.lower())
print(full_name.upper())
print(full_name.capitalize())
bicycle=['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
(print(bicycle[2]))
message=f"Solomon best bike is {bicycle[1]}"
print(message)
text=f"{full_name} best bike is {bicycle[3]}"
print(text)
print(f"{full_name} best bike is {bicycle[3]}")

#Restaurant: Make a class called Restaurant. The __init__() method for
#Restaurant should store two attributes: a restaurant_name and a cuisine_type.
#Make a method called describe_restaurant() that prints these two pieces of
#information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.rest=restaurant_name
        self.cuis=cuisine_type
    def describe_restaurant(self):
        return f"The name of this restaurant is {self.rest}  and the cuisine is {self.cuis}"
    
    def open_close(self):
        return f"The {self.rest} is open"
restaurant=Restaurant('Mwaka jana','indian')
print(restaurant.describe_restaurant())



#Make a class called User. Create two attributes called first_name
#and last_name, and then create several other attributes that are typically stored
#in a user profile. Make a method called describe_user() that prints a summary
#of the user’s information. Make another method called greet_user() that prints
#a personalized greeting to the user.
#Create several instances representing different users, and call both methods 
class User:
    def __init__ (self,first_name,last_name):
        self.fname=first_name
        self.lname=last_name
        full_name=self.fname+" "+self.lname
    def describe_user(self):
        return f"{full_name}"
    def greet_user(self):
        return f"Hello {full_name } !"
names=User('Solomon','Macharia')
    


        

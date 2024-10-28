msg="Solomon i s good"
print(msg)
#Changing case
print(msg.upper())
print(msg.lower())
print(msg.title())
#concatinating
first_name="Solomon"
last_name="Macharia"
full_name=first_name+" "+last_name
print(full_name)
print("Hello ,"+" "+full_name+"!")

text="      I study at Tech camp    "
print(text.strip())
print(text.lstrip())
print(text.rstrip())

#lists
cars=['subaru','toyota','mazda','vw']
print(cars[1])
print("Solomon favorite car is"+" "+ (cars[2]))
print(cars[1].title())
#modifying  list
bikes=['ducati','kawasaki','yamaha']
bikes[0]='zuzuki'
print(bikes)
#Adding an element use .append
bikes.append('ducati')
print(bikes)
#inserting an element use .inserst and u must use the index
bikes.insert(0,'honda')
print(bikes)
#deleting element on the list we use del
solomon=['music','football','hockey']
del solomon[1]
print (solomon)






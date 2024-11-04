#variables
message ="Solomon can code"
print(message)
#changing case variables
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())
#concatenating
first_name="Solomon"
last_name="Macharia"
full_name=first_name+" "+last_name
print(full_name)
print("Hello"+" "+full_name+" "+"!")
#stripping
message="   Nothing comes before a fall  "
print(message.strip())
print(message.lstrip())
print(message.rstrip())
#using intergers
area="base/2*high"
base=20
high=15
result=20/2*15
print(result)
#list
motobikes=['ducati','yamaha','boxer','zuzuki','honda']
print(motobikes)
print(motobikes[3])
#modifying list
cars=['bmw','toyota','honda','subaru']
cars[2]="nissan"
print(cars)
#adding a element
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('kawasaki')
print(motorcycles)
#inserting an element....we use index
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1,"tuktuk")
print(motorcycles)
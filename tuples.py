#create a tuple

marks=(100,200,300,400,500)
print(type(marks))
print(marks[2])
#converting to a list
marks=list(marks)
print(type(marks))
#converting back to a tuple
marks=tuple(marks)
print(type(marks))

#A tuple is a data structure that is used to hold multiple values but the values can not be changed or removed . We say a tuple is immutable. The data inside the tuple is fixed.
#Defined exactly same way as a list except you use round brackets i.e (2,3,”John”, ['Irene', True, 78, 78.2397]) instead of [2,3,”John”]. 
#days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
#1. Find wednesday using an index
#2. Using a function a find the length of the tuple.
#3. Replace Thursday with Thur

days = ("monday","tuesday","wednesday","thursday", "friday","saturday","sunday")
days=list(days)
print(type(days))
print(days[2])
print (len(days))
days2=days
print(days2)
days=tuple(days)
print(type(days))
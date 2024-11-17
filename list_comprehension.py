even_numbers=[]
for i in range(20,101):
    if i %2==0:
        even_numbers.append(i)
print(even_numbers)


even_numbers=[i for i in range(20,101) if i%2==0]
print(even_numbers)

square_numbers=[]
for i in range(1,21):
    square_numbers.append(1**2)
print(square_numbers)

square_numbers=[i**2 for i in range (1,21)]
print(square_numbers)


x=[i for i in range(10)]
print(x)

num=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[i for i in num %2==0]
print(even_numbers)



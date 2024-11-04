    #fruits=['apple', 'orange','mango','ovacado','bannana']
    # for fruit in fruits:
    #     print(fruit)
    #for fruit in fruits:
     ###
    #iterator numbers 
    #x=list(range(10,101))
    #for i in x:
     #   print(i)
        
    #number=list(range(20,101))

    

y=list(range(1,51))
print(y)


y=list(range(1,50,7))

print(y)    
x=[]
for number in y :
    if number%7==0 or number%5==0:
        x.append(number)
print(x)

v=list(range(10,40))
numeral=sum(v)
print(numeral)

sm=0
for i in v:
    sm=sm+i
average=sm/len(v)
print(sm)
print(average)


x=list(range(10,50))
y=[]
count=0
for i in x:
    if i%2!=0:
        y.append(i)
        count=count+1
        if count==10:
            break
print(y)
        
        
number=int(input('enfoter number: '))
for i in range(10):
    mult=number*i
    print(f'{number} * {i} = {mult}')
    
    
count=0
for i in range(1,51):
    if i%2==0:
        count+=1
print('count')
    
    #total_quantity=ls1[]
ls1=[('jay',20),('mon',10),('mya')]
total_quantity=0
for i in ls1: 
        quantity=i[1]
        total_quantity+=quantity
print('total_quantity')
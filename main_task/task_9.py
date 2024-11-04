#Write a program called stars. It should prompt the user for a number,
# and it should print the number of stars till the number entered.
#Example If rows is 5, it should print the following:
#*
#**
#***
#****
#*****.....
number=5

for i in range(number):
    
    
    print('*' * (i+1))
    
    
    
    #To print the spaces before the stars
    print(' ' * (number - i - 1), end='')
    
    #To print the stars
print('*' * (i+1))

print()
print('*' * (i+1))
    
  

    
  
    


    
    

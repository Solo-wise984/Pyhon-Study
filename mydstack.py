my_ds=[23,"Jane",(560),["Lesson","Maths",{"currency":"KES"}],987,(76,"John")]
#Print KES
print(my_ds[3][2]["currency"])
#print 560
print(my_ds[2])
#print maths
print(my_ds[3][1])
#in dictionary with the key currency ,add another key " amount" with value 90
my_ds[3][2]["amount"] = 90
#reversing 987 to 789
my_ds[4]=str(my_ds[4])
my_ds[4]=(my_ds[4][::-1])
my_ds[4]=int(my_ds[4])
print(my_ds)

my_ds[5]=list(my_ds[5])
my_ds[5][1]='jane'
my_ds[5]=tuple(my_ds[5])
print(my_ds)


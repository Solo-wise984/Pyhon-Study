#Write a program that takes input of someone's
# basic salary and benefits, adds them to find the gross salary
# then uses  the gross salary to find the NHIF. 
#To find the Kenya NHIF Rate using THIS LINK: 
basic_salary=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
def gross_salary (basic_salary,benefits):
    gross=(basic_salary+benefits)
    return gross
print( gross_salary (basic_salary,benefits))

def nhif_contribution(gross):
    if gross < 6000:
        return 150
    elif gross >=6000 and gross== 7999:
        return 300
    elif gross >=8000 and gross ==11999:
        return 400
    elif gross >= 12000 and gross ==14999:
        return 500
    elif gross >=15000 and gross == 19999:
        return 600
    elif gross >=20000 and gross ==24999:
        return 750
    elif gross >=25000 and gross == 29999:
        return 850
    elif gross>=30000 and gross ==34999:
        return 900
    elif gross >= 35000 and gross == 39999:
        return 950
    elif gross >=40000 and gross ==44999:
        return 10000
    elif gross >=45000 and gross ==49999:
        return 1100
    elif gross >= 50000 and gross ==59999:
        return 1200
    elif gross >=60000 and gross== 69999:
        return 1300
    elif gross >=70000 and gross==79999:
        return 1400
    elif gross >=80000 and gross==89999:
        return 1500
    elif gross >= 90000 and gross == 99999:
        return 1600
    else:
        return 1700
    
gross=gross_salary(basic_salary,benefits)
nhif=nhif_contribution(gross)
print("nhif result: ",nhif)
        

#Continue with the program above, then use  the gross salary to find the NSSF. 
#To find the Kenya NSSF Rate  using 6% of the Gross Salary.
#BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
if gross> 18000:
    def NSSF (gross_salary):
        nssf=gross_salary*(6/100)
        return nssf
    print ("NSSF is",NSSF (benefits,basic_salary))
else:
    print("Not enough gross salary")


    

#Continue with the same program and calculate an individual’s NHDF using:
# i.e NHDF = gross_salary *  0.015

def NHDF(basic_salary,benefits):
    nhdf=gross_salary*(0.015)
    return nhdf
print("Your NHDF  is: ",NHDF(basic_salary,benefits))

#Calculate the taxable income.
#i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 

taxable_income=gross_salary-(nhif+nhif+NSSF(basic_salary,benefits))
print("Taxable income is: ",taxable_income)


def taxable_income (gross_salary,NSSF,NHDF,NHIF):
    total=gross_salary+NSSF+NHDF+NHIF
    return total
print ("Your taxable income is: ",taxable_income (gross_salary,NSSF,NHDF,NHDF))



#Continue with the same program and
# find the person's PAYEE using the taxable income above.
#Find the Kenya PAYEE Tax Rate using THIS LINK

#0 – 24,000	10%
#On the next 8,333	=25%
#On the next 467,667 =	30%
#On the next 300,000	 =32.5%
#On amounts over 800,000	 =35%
#Personal Relief: KES 2,400.00 per month
#Minimum Taxable Income: KES 24,001.00 per month

def payee (taxable_income):
    if taxable_income < 24000:
        return ("10%")
    elif taxable_income >=24000 and taxable_income<=32333:
        return ("25%")
    elif taxable_income >=32334 and taxable_income<=500000:
        return ("30%")
    elif taxable_income >=500001 and taxable_income<=800000:
        return ("32.5%")
    elif taxable_income >800000:
        return ("35%")

print("Your payee is: ",payee(taxable_income))


#Continue with the same program and calculate an individual’s Net Salary using:
 #net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def net_salary (gross_salary,NSSF,NHDF,NHIF,payee):
    net=gross_salary-(NSSF+NHDF+payee)
    return net

print("Your net salary is: ",net_salary (gross_salary,NSSF,NHDF,NHIF,payee))
        
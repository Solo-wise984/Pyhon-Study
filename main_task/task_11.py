#Write a program that takes the date of birth of a person and
# the program outputs the age in terms of
# years,months,days TODAY
dob =input("Enter the date of birth  yyyy/mm/dd: ")

import datetime

# Get today's date

today = datetime.date.today()

# Parse the date of birth

dob_date = datetime.datetime.strptime(dob, "%Y/%m/%d").date()

# Calculate the age

age_years = today.year - dob_date.year

age_months = today.month - dob_date.month

age_days = today.day - dob_date.day

# Adjust for leap years

if (dob_date.month, dob_date.day) > (today.month, today.day):

    age_years -= 1

elif (dob_date.month, dob_date.day) == (today.month, today.day):
    if age_days < 0:
        age_months -= 1
    elif age_days == 0:
        age_years -= 1
        age_months = 12
        age_days = 31
        
    

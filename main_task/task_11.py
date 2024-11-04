#Write a program that takes the date of birth of a person and
# the program outputs the age in terms of
# years,months,days TODAY
dob =input("Enter the date of birth  yyyy/mm/dd: ")

# Split the date of birth into year, month, and day

dob_list = dob.split("/")
year = int(dob_list[0])
month = int(dob_list[1])
day = int(dob_list[2])
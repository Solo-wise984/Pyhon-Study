#TASK 5: Using Python or PHP or Java or Ruby or JavaScript
#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
# Return the largest of the three. Do this without using the the inbuilt max () function!

def get_user_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        
#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks=int(input("Enter student marks"))
if marks<0 and marks>100:
    print("invalid marks")
elif marks>79:
    print("A")
elif marks >= 60 and marks < 79:
    print("B")
elif marks >= 49 and marks < 60:
    print("C")
elif marks >= 40 and marks < 50:
    print("D")
else:
    print("E")
    
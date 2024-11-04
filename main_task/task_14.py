while True:
    try:
        value = float(input("Enter first numbers: "))
        value2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid character entered. Please enter a number.")
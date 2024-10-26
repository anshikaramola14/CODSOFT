#Calculator
import math

def add(x, y): #function to add
    return x + y

def subtract(x, y):  #function to subtract
    return x - y

def multiply(x, y):   #function to multiply
    return x * y

def divide(x, y):      #function to divide

    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):       #function to power

    return x ** y

def square_root(x):     #function to find square root

    return math.sqrt(x)

def calculator(): #function to call the functions
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")

    choice = input("Enter choice (1/2/3/4/5/6): ")   #enter choices

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {power(num1, num2)}")
    elif choice == '6':
        num = float(input("Enter number: "))
        print(f"The result is: {square_root(num)}")
    else:
        print("Invalid Input")

if __name__ == "__main__":
    calculator()

# Task 1
import math

def addition(x,y):
    print(f"The answer is {x + y}")
    

def subtraction(x,y):
    print(f"The answer is {x - y}")
   


def multiplication(x,y):
    print(f"The answer is {x * y}")


def division(x,y):
    print(f"The answer is {x / y}")
   
# Task 2 and 3

while True:
    choice = input("""Which operation would you like to perform? 
(add, subtract, multiply, divide, or exit): """)
    if choice == "add": 
        first_add = float(input("Enter the first number you would like to add: "))
        second_add = float(input("Enter the second number you would like to add."))
        addition(first_add,second_add)
    elif choice == "subtract":
        first_sub = float(input("Enter the first number in the subtraction problem: "))
        second_sub = float(input("Enter the number you would like to subtract: "))
        subtraction(first_sub,second_sub)
    elif choice == "multiply":
        first_mult = float(input("Enter the first number you would like to multiply: "))
        second_mult = float(input("Enter the second number you would like to multiply."))
        multiplication(first_mult,second_mult)
    elif choice == "divide":
        first_div = float(input("Enter the dividend: "))
        second_div = float(input("Enter the divisor."))
        if second_div == 0:
            print("You cannot divide a number by 0.")
        else: 
            division(first_div,second_div)
    elif choice == "exit":
        break
    else:
        print("Invalid Response")

"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

def calculate():
    operation = input(""" please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplcation
/ for division
*2 for square
*3 for cube
** for power
& for mod """)

    number_1 = int(input("Enter your first number: "))
    number_2 = int(input("Enter your second number: "))

    if operation == "+":
        print("{} + {} = ".format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == "-":
        print(" {} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == "*":  
        print(" {} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == "/":
        print(" {} / {} = ".format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == "square":
        print(square(float(number_1)))

    elif operation == "cube":
        print("{} *3  {} *3 = ".format(number_1, number_2))
        print(cube(float(number_1), float(number_2)))
    

    elif operation == "pow":
        print(" {} ** {} = ".format(number_1, number_2))
        print(pow(float(number_1), float(number_2)))

    elif operation == "mod":
         print("{} % {} = ".format(number_1, number_2))
         print(mod(float(number_1), float(number_2)))

    else:
        print("You have not typed in a valid operator, try again. ")       

def again():
    calc_again = input(""" Dou you want to calculate again? Please type y for yes and n for no.""")
    
    if calc_again == "y":
        calculate()
    elif calc_again == "n":
        print("See you later. ")
    else:
        again()
            
calculate()
#Simple
# from random import choice
# from tokenize import Number
# from unicodedata import numeric

# one = input("please enter the first number:")
# two = input("please enter the second number:")

# print("Your answer is: " + str((float(one) + float(two))))

#Advanced
# Input 1 = Number 1
# Input 2 = Operator choice
# Input 3 = Number 2

def calculator(num1, operator, num2):
    if operator == "+":
        return(num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "*":
        return(num1 * num2)
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

print(calculator(3.3, "*", 5))

#Here, if the division is in the else clause, and there's no check for whether the second argument is a valid operator or not, it defaults to the else clause and tries to perform division, causing unexpected behavior.








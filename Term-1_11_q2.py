# Class 11, Term 1, Question 1
# Input three numbers and display the largest / smallest number.
# Author: Anoop Verma
# Date written: 17/09/2021
#
# Solved with larger number.

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
num3 = eval(input("Enter third number: "))

print("\nOriginal numbers: ", num1, num2, "and", num3)

if num1>num2 and num2>num3:
    print("\nLargest number: ", num1)
elif num2>num3 and num3>num1:
    print("\nLargest number: ", num2)
else:
    print("\nLargest number: ", num3)
    

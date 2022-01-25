# Class 11, Term 1, Question 1
# Input two numbers and display the larger / smaller number.
# Author: Anoop Verma
# Date written: 17/09/2021
#
# Solved with larger number.

num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))

print("Original numbers: ", num1, "and", num2)

if num1>num2:
    print("\nLarger number: ", num1)
else:
    print("\nLarger number: ", num2)

# Write a program to input the value of x and n and print the sum
# of the following series:
# 1+x+x^2+x^3+x^4+. .......... x^n.
#
# Author: Anoop Verma
# Date written: 13/08/2021

x = int(input("Enter value for x: "))
n = int(input("Enter value for n: "))

sum = 0
for i in range(0,n+1):
    sum = sum+(x**i)

print("Sum =", sum)

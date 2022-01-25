# Write a program to input the value of x and n and print the sum
# of the following series:
# x - (x^2)/2 + (x^3)/3 - (x^4)/4 + ............ (x^n)/n
#
# Author: Anoop Verma
# Date written: 13/08/2021

x = int(input("Enter value for x: "))
n = int(input("Enter value for n: "))

psum = 0
nsum = 0
for i in range(1,n+1,2):
    psum = psum + (x**i)/i
for j in range(2,n+1,2):
    nsum = nsum + (x**j)/j
sum = psum - nsum

print("Sum =", sum)

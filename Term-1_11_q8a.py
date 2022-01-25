# Computer the greatest common divisor, of any two integers.
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 > num1:
   while (num2):
       num1, num2 = num2, num1%num2
   print("GCD = ", num1)
elif num1 == num2:
   print("GCD = 1")
else:
   while(num1):
      num2, num1 = num1, num2%num1
   print("GCD = ", num2)
   


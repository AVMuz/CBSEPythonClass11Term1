# Computer the least common multiple. of two integers.
#
# Author: Anoop Verma
# Date written: 17/09/2021

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# choose the greater number
if num1 > num2:
   greater = num1
else:
   greater = num2

while(True):
   if((greater % num1 == 0) and (greater % num2 == 0)):
      lcm = greater
      break
   greater += 1

print("LCM = ", lcm)

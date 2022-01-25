# Determine whether a number is a perfect number.
#
# A perfect number is a positive integer that is equal to the sum
# of its positive divisors, excluding the number. 
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

while True:
    num = int(input("Enter any number: "))
    if num<0:
        print("Number has to be a positive integer")
    else:
        break
sum = 0
for i in range(1, num):
    if num%i == 0:
        sum = sum + i
if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")

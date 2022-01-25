# Input a number and check if the number is a prime or composite number.
#
# A number is said to be Prime if it has only 2 divisors, 1 and the
# number itself.
# 1 is not a prime number.
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

num = int(input("Enter a number: "))

flag = True

for i in range(2, num):
    if num%i == 0:
        flag = False
        break

if flag == True and num!=1:
    print(num, "is Prime number.")
else:
    print(num, "Not Prime, it is Composite number.")

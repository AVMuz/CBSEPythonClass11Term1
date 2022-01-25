# Determine whether a number is an armstrong number.
#
# A number is said to be Armstrong number if the number and the sum of each of
# its digits raised to the power of the number of digits, are same.
#
# For a three digit number, each digit will be raised to the power of three
# and added. If the result of this sum and the number are same then it is
# Armstrong number.
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

num = int(input("Enter a number: "))

# Changed num variable to string, 
# and calculated the length (number of digits)
no_of_digit = len(str(num))

# initialize sum
sum = 0

# find the sum of each digit raised to the power of no_of_digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** no_of_digit
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

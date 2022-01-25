# Determine whether a number is a palindrome.
#
# A number is said to be Palindrome if the number and number made by
# reversing its digits are same.
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

num = int(input("Enter a number: "))

temp = num

new_num = 0
while temp > 0:
   digit = temp % 10
   new_num = new_num*10 + digit
   temp //= 10

# display the result
if num == new_num:
   print(num,"is a Palindrome")
else:
   print(num,"is not a Palindrome")

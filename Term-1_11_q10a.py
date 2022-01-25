# Input a string and determine whether it is a palindrome or not.
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

str1 = input("Enter the string: ")

str_len = len(str1)

str2 = str1[str_len::-1]

if str1 == str2:
    print("String is Palindrome.")
else:
    print("String is not a Palindrome.")

# Input a string and convert the case of characters in that string.
#
# Author: Anoop Verma
# Date written: 17/09/2021
# version 3.0
#

str1 = input("Enter the string: ")

s_len = len(str1)

str2 = ""

for i in str1:
    if i.isupper():
        str2 += i.lower()
    else:
        str2 += i.upper()

print(str2)
        
        
    

# Input a string and convert the case of characters in that string.
#
# Author: Anoop Verma
# Date written: 17/09/2021
# version 2.0
#

str1 = input("Enter the string: ")

s_len = len(str1)

for i in str1:
    if i.isupper():
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')
        
        
    

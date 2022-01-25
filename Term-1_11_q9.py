# Count and display the number of vowels, consonants, uppercase, lowercase
# characters in string.
#
# Author: Anoop Verma
# Date written: 17/09/2021
#

str = input("Enter the string: ")

vow_ctr = 0
con_ctr = 0
upp_ctr = 0
low_ctr = 0

vow_list = "AEIOUaeiou"
con_list = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
upp_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_list = "abcdefghijklmnopqrstuvwxyz"

for i in str:
    if i in vow_list:
        vow_ctr += 1
    if i in con_list:
        con_ctr += 1
    if i in upp_list:
        upp_ctr += 1
    if i in low_list:
        low_ctr += 1

print("Number of vowels: ", vow_ctr)
print("Number of consonants: ", con_ctr)
print("Number of uppercase: ", upp_ctr)
print("Number of lowercase: ", low_ctr)

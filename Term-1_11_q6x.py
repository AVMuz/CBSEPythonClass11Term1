# Display all prime numbers in a given range.
#
# A number is said to be Prime if it has only 2 divisors, 1 and the
# number itself.
# 1 is not a prime number.
#
# This code is from the official Python documentation.
#
# Typed by: Anoop Verma
# Date typed: 17/09/2021
#

beg_num = int(input("Enter the beginning of range: "))
end_num = int(input("Enter the end of range: "))
for n in range(beg_num, end_num+1):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
        

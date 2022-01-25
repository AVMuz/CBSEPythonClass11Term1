# Class 11, Term 1, Question 1
# Generate the following patterns using nested loop.
#   12345
#   1234
#   123
#   12
#   1
# Author: Anoop Verma
# Date written: 17/09/2021
#

n = int(input("Enter the number of rows to print: "))

print("\nPattern for", n, "rows.\n")

while n>0: 
    for j in range(1,n+1):
        print(j, end=' ')
    n -= 1
    print()
    

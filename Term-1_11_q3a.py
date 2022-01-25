# Class 11, Term 1, Question 1
# Generate the following patterns using nested loop.
#   *
#   **
#   ***
#   ****
#   *****
# Author: Anoop Verma
# Date written: 17/09/2021
#

n = int(input("Enter the rows to print: "))

print("\nPattern for", n, "rows.\n")

for i in range(1, n+1):
    for j in range(1,i+1):
        print('*', end='')
    print()
    

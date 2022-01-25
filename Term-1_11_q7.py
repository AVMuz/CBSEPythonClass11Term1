# Display the terms of a Fibonacci series.
#
# The Fibonacci Sequence is the series of numbers:
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# The next number is found by adding up the two numbers before it.
#
# This code is from the official Python documentation.
#
# Typed by: Anoop Verma
# Date typed: 17/09/2021
#

end_num = int(input("Enter the number upto which you want to see the series: "))
a, b = 0, 1
while a < end_num:
    print(a, end=', ')
    a, b = b, a+b
    

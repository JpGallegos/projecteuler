#! /usr/bin/env python
"""\
Largest palindrome product\
Problem 4\
A palindromic number reads the same both ways. The largest palindrome made \
from the product of two 2-digit numbers is 9009 = 91 x 99.\
\
Find the largest palindrome made from the product of two 3-digit numbers.\
"""

product = ''
greatest_palindrome = '0'

for i in range(100, 1000):
    for j in range(999, 99, -1):
        product = str(i * j)
        middle = int(len(product)/2)
        # If the number of digits in the product is even, then you can cut it right in half.
        # But if the number of digits is odd, the middle digit has to go on both sides.
        middle_digit = (middle, middle) if len(product) % 2 == 0 else (middle + 1, middle)
        if product[:middle_digit[0]] == product[middle_digit[1]:][::-1]:
            if int(product) <= int(greatest_palindrome):
                break
            elif int(product) > int(greatest_palindrome):
                greatest_palindrome = product
print greatest_palindrome
#! /usr/bin/env python
# coding: utf-8

"""\
The sum of the squares of the first ten natural numbers is,\
\
                                                        12 + 22 + ... + 102 = 385\
The square of the sum of the first ten natural numbers is,\

                                                        (1 + 2 + ... + 10)2 = 552 = 3025\
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.\
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\
"""

def sumofsquares(n):
    return (n*(n+1)*(2*n+1))/6

def squareofsum(n):
    return ((n*(n+1))/2)**2

def sumsquaredifference(n):
    return squareofsum(n) - sumofsquares(n)

if __name__ == "__main__":
    n = 100
    print "The difference of between the sum of squares of the first %i natural numbers and the square of the sum is %i - %i = %i" \
         % (n, squareofsum(n), sumofsquares(n), sumsquaredifference(n))
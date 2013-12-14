#! /usr/bin/env python
# conding: utf-8

"""\
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, \
\
a2 + b2 = c2 \
For example, 32 + 42 = 9 + 16 = 25 = 52.\
\
There exists exactly one Pythagorean triplet for which a + b + c = 1000. \
Find the product abc.\

Note that:
a = k * (m**2 - n**2)
b = k * (2 * m * n)
c = k * (m**2 + m**2)
for some positive integers k, m, n. It is also necessary that m > n, m - n odd, and that m and n are coprime. \
k is the greatest common divisor of a, b, and c. \
"""
from eulerutils import coprime
from math import sqrt

triplet_found = False
a, b, c = 0, 0, 0
k, m, n, d = 0, 0, 0, 0
goal = 1000

for m in range(2, int(sqrt(goal/2))):
    print m, (goal/2) % m
    if (goal/2) % m == 0:
        if m % 2 == 0:
            k = m + 1
        else:
            k = m + 2
        while k < (2 * m) and k <= goal/(2*m):
            if (goal/(2 * m)) % k == 0 and coprime(k, m):
                d = (goal/2) / (k * m)
                n = k - m
                a = d * (m**2 - n**2)
                b = d * (2 * m * n)
                c = d * (m**2 + n**2)
                triplet_found = True 
                break
            k += 2
    if triplet_found:
        print "Breaking."
        break

print "The Pythagorean triplet is %i, %i, %i, and the sum is %i" % (a, b, c, a+b+c)
print "The product of Eucledian triplet a + b + c = 1000 is:", a*b*c 
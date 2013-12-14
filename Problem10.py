#! /usr/bin/env python
# coding: utf-8
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.\
\
Find the sum of all the primes below two million. """

from eulerutils import get_primes

if __name__ == "__main__":
    target = 2000000
    sum_of_primes_below_target = 0

    for prime in get_primes():
        if prime < target:
            sum_of_primes_below_target += prime
        else:
            break

    print sum_of_primes_below_target
#! /usr/bin/env python
# coding: utf-8
"""\
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.\
\
What is the 10 001st prime number?\
"""

if __name__ == "__main__":
    from eulerutils import get_primes
    import sys
    prime_goal = 10001
    cntr = 0
    
    for prime in get_primes():
        cntr += 1
        if cntr == prime_goal:
            break
    print cntr, prime

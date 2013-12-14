"""\
This module contains the definition of tools that can be reused \
between the problems found in Project Euler.\
"""
from math import sqrt

class Memoize(object):
    def __init__(self, func):
        self.func = func
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.func(*args)
        return self.memo[args]

@Memoize
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False

def get_primes(n=None):
    """\
    Generates all the primes from 2 to sqrt(n).\
    If no paremeter is passed then iterate through all odd integer numbers.\
    \
    Raises ValueError if n < 2.\
    """
    if n != None and n < 2:
        raise ValueError
    elif n == 2: 
        yield 2
    elif n != None:
        prime_range = int(sqrt(n)) + 1

        yield 2

        # Even numbers > 2 are never prime, don't even bother testing
        for num in range(3, prime_range, 2):
            if is_prime(num):
                yield num 
    elif n == None:
        num = 3
        yield 2

        while 1:
            if is_prime(num):
                yield num
            num += 2

def gcd(a, b):
    m = max(a, b)
    n = min(a, b)
    if m % n == 0:
        return m
    return gcd(n, m%n)

def coprime(a, b):
    return gcd(a, b) == 1
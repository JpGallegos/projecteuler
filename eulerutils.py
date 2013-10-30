"""\
This module contains the definition of tools that can be reused \
between the problems found in Project Euler.\
"""
from math import sqrt

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

def get_primes(n):
	"""\
	Generates all the primes from 2 to sqrt(n).\
	\
	Raises ValueError if n < 2.\
	"""
	if n < 2:
		raise ValueError
	elif n == 2: 
		yield 2
	else:
		prime_range = int(sqrt(n)) + 1

		yield 2

		# Even numbers > 2 are never prime, don't even bother testing
		for num in range(3, prime_range, 2):
			if is_prime(num):
				yield num
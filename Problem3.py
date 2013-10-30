#! /usr/bin/env python

"""\
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?\
""" 
from eulerutils import get_primes

n = 600851475143
greatest_prime = 0

for prime in get_primes(n):
	if n % prime == 0:
		if prime > greatest_prime:
			greatest_prime = prime
		# In order to avoid going through all the primes from
		# 2 to sqrt(n) take advantage of the Fundamental
		# Theorem of Arithmetic, and reduce n by each of its 
		# prime factors as much as possible.
		while n % prime == 0:
			n /= prime
	if n == 1:
		# Since 1 is divisible only by itself, there is no more 
		# work to be done.
		break		
print greatest_prime
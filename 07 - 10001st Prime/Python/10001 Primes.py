#! /usr/bin/env python
#Problem 7 Euler

import math, sys

def main():
	if len(sys.argv) < 2:
		print 'Specify the max'
	else:
		primes = genPrimeTable(int(sys.argv[1]))
		print primes[len(primes)-1]

def genPrimeTable(maxSize):
	knownPrimes = [2, 3]
	i = 3
	while len(knownPrimes) < maxSize:
		i += 1
		if isPrime(i, knownPrimes):
			# print '%d is Prime' % (i)
			knownPrimes.append(i)
	
	print 'There are %d entries in the knownPrimes list' % (len(knownPrimes))
 	# print knownPrimes
	
	return knownPrimes

def isPrime(val, knownPrimes):
	prime = True
	max = int(math.sqrt(val)) + 1
	for i in knownPrimes:
		if i > max:
			break
		if val % i == 0:
			prime = False
			# print '%d is divisible by the prime %d' % (val, i)
			return False
	return prime

if __name__ == "__main__":
	main()

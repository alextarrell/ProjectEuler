#! /usr/bin/env python
#Problem 9 Euler

import math

def main():
	primes = genPrimeTable(int(sys.argv[1]))
	print primes[len(primes)-1]

def isTriplet(val1, val2, val3):
	if (val!**2 + val**2 == val3**2):
		return true
	else:
		return false

if __name__ == "__main__":
	main()

# Project Euler 12 - Highly Divisible Triangular Number

from math import sqrt

def triangleNumbers():
	cur = 0
	idx = 1
	while True:
		cur += idx
		idx += 1
		yield cur

def factors(n):
	results = set()
	for i in xrange(1, int(sqrt(n)) + 1):
		if n % i == 0:
			results.add(i)
			results.add(int(n/i))
	return results

def main():
	print next(v for v in triangleNumbers() if len(factors(v)) > 500)

if __name__ == '__main__':
	main()

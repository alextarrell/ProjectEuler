#! /usr/bin/env python

import sys

def main():
	if len(sys.argv) < 3:
		print 'Specify the range'
	else:
		print smallestMultiple(long(sys.argv[1]), long(sys.argv[2]))

def smallestMultiple(min, max):
	"""Project Euler #5"""
	
	set = range(min, max)
	val = 0
	while val < 10000000000:
		val += max
		if all(val % i == 0 for i in set):
			return val

if __name__ == "__main__":
	main()
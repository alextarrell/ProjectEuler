# Project Euler 14 - Longest Collatz Sequence

def collatz(num):
	yield num
	while num > 1:
		if num % 2 == 0:
			num = num/2
		else:
			num = 3*num + 1
		yield num

def main():
	print "{1} with {0} elements".format(*max((len(list(collatz(i))), i) for i in xrange(1, 999999)))

if __name__ == '__main__':
	main()

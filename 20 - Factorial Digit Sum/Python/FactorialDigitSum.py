# 20 - Factorial Digit Sum

from math import factorial

def main():
	print sum(int(d) for d in str(factorial(100)))

if __name__ == '__main__':
	main()

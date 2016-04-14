# 19 - Counting Sundays

from datetime import date

def main():
	print sum(1 for y in xrange(1901, 2001) for m in xrange(0, 12) if date(y, m+1, 1).weekday() == 6)

if __name__ == '__main__':
	main()

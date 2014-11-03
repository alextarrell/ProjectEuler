# Project Euler - Problem 1

def sumInRange(value, rangeMin, rangeMax):
	return sum([value * i for i in range(rangeMin / value + 1, (rangeMax - 1) / value + 1)])

def main():
	print "Sum: ", sumInRange(3,0,1000) + sumInRange(5,0,1000) - sumInRange(15,0,1000)

if __name__ == "__main__":
	main()
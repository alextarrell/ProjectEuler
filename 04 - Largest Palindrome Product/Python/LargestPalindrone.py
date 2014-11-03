#! /usr/bin/env python

#Problem 4 Euler

def main():
	palindroneList = []
	set = range(100,1000)
	for x in set:
		for y in set:
			if isPalindrone(x*y):
				palindroneList.append(x*y)
	
	palindroneList.sort()
	print palindroneList[len(palindroneList)-1]

def isPalindrone(val):
	first, second = str(val)[:len(str(val))/2], str(val)[len(str(val))/2:]
	second = second[::-1]
	second = second[:len(first)]
	return first == second

if __name__ == "__main__":
	main()
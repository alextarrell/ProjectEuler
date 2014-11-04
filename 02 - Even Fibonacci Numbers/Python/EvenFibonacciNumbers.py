# Project Euler - Problem 2
def fibonacci(max = float('inf')):
	prev = 1
	curr = 1
	while curr < max:
		yield curr
		prev, curr = curr, prev + curr

def main():
	sum = 0
	for x in fibonacci(4000000):
		sum += 0 if x % 2 else x

	print "Sum: ", sum

if __name__ == "__main__":
	main()
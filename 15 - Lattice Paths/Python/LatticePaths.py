# Project Euler 15 - Lattice Paths

def latticePaths(rows, columns):
	grid = list(list(1 for _ in xrange(columns+1)) for _ in xrange(rows+1))
	for x in xrange(1, columns+1):
		for y in xrange(1, rows+1):
			grid[y][x] = grid[y-1][x] + grid[y][x-1]
	return grid[len(grid)-1][len(grid[0])-1]

def main():
	print latticePaths(20, 20)

if __name__ == '__main__':
	main()

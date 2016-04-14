# 17 - Number Letter Counts

singles = [
	'',
	'one',
	'two',
	'three',
	'four',
	'five',
	'six',
	'seven',
	'eight',
	'nine',
	'ten',
	'eleven',
	'twelve',
	'thirteen',
	'fourteen',
	'fifteen',
	'sixteen',
	'seventeen',
	'eighteen',
	'nineteen',
]

tens = [
	'',
	'',
	'twenty',
	'thirty',
	'forty',
	'fifty',
	'sixty',
	'seventy',
	'eighty',
	'ninety',
]

def toFancy(num):
	if num < 0:
		return ['minus'] + toFancy(-num)

	if num < 20:
		return [singles[num]]

	if num < 100:
		return [tens[num / 10]] + toFancy(num % 10)

	if num < 1000:
		return [singles[num / 100]] + ['hundred'] + (['and'] if (0 < num % 100) else []) + toFancy(num % 100)

	if num < 1000000:
		return [singles[num / 1000]] + ['thousand'] + (['and'] if (0 < num % 1000 < 100) else []) + toFancy(num % 1000)

	raise ValueError(num + ' is too large and is unsupported')

def main():
	print sum([len("".join(toFancy(n))) for n in xrange(1,1001)])


if __name__ == '__main__':
	main()

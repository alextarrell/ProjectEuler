object MultiplesOf3And5 {
	def sumInRange(value: Int, maxRange: Int): Int = {
		return (0 to ((maxRange-1) / value)).map(_ * value).sum
	}

	def main(args: Array[String]) {
		println(sumInRange(3, 1000) + sumInRange(5, 1000) - sumInRange(15, 1000))
	}
}
// 21 - Amicable Numbers

object AmicableNumbers extends App {
	def sumFactors(n: Integer): Integer = {
		if (n == 1) 1
		else (1 to (n/2).toInt).filter(n % _ == 0).toList.foldLeft(0)(_ + _)
	}

	val allSums = (1 until 10000).map(n => n -> sumFactors(n)).toMap
	val result = allSums.filter{case (n, s) => n != s && allSums.contains(s) && allSums(s) == n}.foldLeft(0)(_ + _._2)
	println(s"$result")
}

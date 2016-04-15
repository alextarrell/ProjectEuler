// 23 - Non-Abundant Sums

object NonAbundantSums extends App {
	def sumFactors(n: Integer): Integer = {
		if (n == 1) 1
		else (1 to (n/2).toInt).filter(n % _ == 0).toList.foldLeft(0)(_ + _)
	}

	val abundants = (1 to 28123).par.filter(n => n < sumFactors(n)).toSet
	val result = (1 to 28123).par.filter(n => ((0 to (n/2).toInt) zip (n to (n/2).toInt by -1)).forall{
		case (l, h) => !abundants.contains(l) || !abundants.contains(h)
	}).foldLeft(BigInt(0))(_ + _)
	println(s"$result")
}

// Project Euler 16 - Power Digit Sum

object PowerDigitSum extends App {
	val sum = BigInt(2).pow(1000).toString.foldLeft(BigInt(0))(_ + _.asDigit)
	println(s"2^1000 = $sum")
}

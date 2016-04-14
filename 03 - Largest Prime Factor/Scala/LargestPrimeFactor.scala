// Project Euler - Problem 3
// Largest Prime Factor of 600851475143
// Alex Tarrell

import Stream._
import math.pow

object LargestPrimeFactor {
	
	def primeFactors(number: Int, list: List[Int] = List()): List[Int] = {
		println(math.pow(number.toDouble, 0.5).round.toInt)
		for(n <- 2 to math.pow(number.toDouble, 0.5).round.toInt if (number % n == 0)) {
			return primeFactors(number / n, list :+ n)
		}
		list
	}

	def main(args: Array[String]) {
		println(primeFactors(24))
	}
}

// Project Euler - Problem 2
// Alex Tarrell

import Stream._

object EvenFibonacciNumbers {
	val fibonacci: Stream[Int] = 0 #:: fibonacci.scanLeft(1)(_ + _)

	def main(args: Array[String]) {
		println(fibonacci.filter(_ % 2 == 0).takeWhile(_ <= 4000000).sum)
	}
}
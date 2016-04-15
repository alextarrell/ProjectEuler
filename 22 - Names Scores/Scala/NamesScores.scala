// 22 - Names Scores

object NamesScores extends App {
	def alphaValue(str: String): Integer = {
		str.toUpperCase.toCharArray.foldLeft(0)(_ + _ - ('A' - 1))
	}

	val result = io.Source.fromFile("../names.txt")
		.getLines.map(ln => ln.replace("\"", "").split(",").toList)
		.take(1)
		.toList
		.head
		.sorted
		.zipWithIndex
		.foldLeft(BigInt(0))((sum, elm) => sum + alphaValue(elm._1) * (elm._2+1))
	println(s"$result")
}

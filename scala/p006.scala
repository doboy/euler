import scala.math

object p006 {
  def squareOfSums(top: Int): Int = {
    var sum = List.range(0, top).foldLeft(0) {
      _ + _
    }
    sum * sum
  }

  def sumOfSquares(top: Int): Int = {
    List.range(0, top).map( x => x * x ).foldLeft(0) {
      _ + _
    }
  }

  def main(args: Array[String]) {
    println(squareOfSums(101) - sumOfSquares(101))
  }
}

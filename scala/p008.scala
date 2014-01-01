import scala.annotation.tailrec
import scala.math.max
import java.math.BigInteger

object p008 {
  def greatestProductOfFiveConsectiveDigits  (number: java.math.BigInteger): Int = {
    greatestProductOfFiveConsectiveDigitsHelper(number, 0)
  }

  @tailrec
  def greatestProductOfFiveConsectiveDigitsHelper (number: java.math.BigInteger, bestSoFar: Int): Int = {
    if (number == new java.math.BigInteger("0")) {
      bestSoFar
    } else {
      greatestProductOfFiveConsectiveDigitsHelper(number.divide(new java.math.BigInteger("10")),
        scala.math.max((number.mod(new java.math.BigInteger("100000"))).toString().map(_.asDigit).product, bestSoFar))
    }
  }

  def main(args: Array[String]) {
    println(
        greatestProductOfFiveConsectiveDigits(
                new java.math.BigInteger(scala.io.Source.fromFile("txt/p008").mkString)))
  }
}

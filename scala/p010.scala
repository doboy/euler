import java.math.BigInteger

class sievesPrimeGenerator(top: Integer) extends Iterable[Integer] {
  val arr = (new Array [Boolean] (top)).map(_ => true)
  arr(0) = false
  arr(1) = false

  def iterator = new Iterator[Integer] {
    var iter = 2
    var _hasNext = true

    def hasNext() : Boolean = {
      _hasNext && iter < top
    }

    def next() : Integer = {
      val toReturn = iter

      for(i <- iter * 2 until top by iter) {
        arr(i) = false
      }

      iter = arr.indexWhere({ x => x }, iter + 1)
      _hasNext = iter != -1

      toReturn
    }
  }
}

object p010 {
  def main(args: Array[String]) {
    println (new sievesPrimeGenerator(2000000).foldLeft(BigInteger.ZERO) {
      (x, y) => new BigInteger(x.toString).add(new BigInteger(y.toString))
    })
  }
}

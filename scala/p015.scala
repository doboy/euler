import java.math.BigInteger

object p015 {
  var hash : Map[Tuple2 [BigInteger, BigInteger], BigInteger] = Map()

  def ways(w : BigInteger, h : BigInteger): BigInteger = {
    var key = Tuple2(w, h)
    if (w == BigInteger.ONE || h == BigInteger.ONE) {
      return BigInteger.ONE
    } else if (!hash.contains(key)) {
      val value = ways(w, h.subtract(BigInteger.ONE)).add(
                  ways(w.subtract(BigInteger.ONE), h))
      hash += Tuple2(key, value)
    }

    hash.getOrElse(key, BigInteger.ZERO)
  }

  def main(args: Array[String]) {
    val s = new BigInteger("21")
    println(ways(s, s))
  }
}

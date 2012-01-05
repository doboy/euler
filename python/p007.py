from utils import primeGen

p = primeGen()
print [ next( p ) for i in xrange( 10001 ) ][ -1 ]

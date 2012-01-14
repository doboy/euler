from utils import primeGen

p = primeGen()
for i in xrange( 10 ** 4 ):
    next( p )

print next( p )

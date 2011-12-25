from utils import primeGen, isPrime, rotated, baseGen
from math import log10

cps = { 2, 3, 5, 7, 11 }

def isCircular( n ):
    digits = int( log10( n ) )
    for _ in xrange( digits + 1 ):
        if not isPrime( n ):
            return False
        # rotate the number
        n = rotated( n, digits )
    return True

for x in baseGen( goods=( 0, 1, 3, 7, 9 ),
                  start=11,
                  end=10 ** 6 ):
    if isCircular( x ):
        cps.add( x )

print len( cps )

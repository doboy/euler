from utils import fraction
from math import log10
# LCM

def expandGen( end=float("inf") ):
    i = 0
    f = fraction( 3, 2 )
    while i < end:
        yield f
        f += fraction( 1 )
        f = fraction( f.d, f.n )
        f.reduce()
        i += 1

print sum( 1 for n, d in expandGen( 1000 ) if int( log10( n ) ) > int( log10( d ) ) )

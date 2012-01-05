from math import ceil, sqrt

TILES = 10 ** 6

L = {}

for x in xrange( 1, TILES / 4 + 2 ):
    low = int( ceil( sqrt( max( 1, x * x - TILES ) ) ) )
    low += ( x + low ) % 2
    for y in xrange( low, x, 2 ):
        t = x * x - y * y
        L[ t ] = L.get( t, 0 ) + 1

print sum( 1 for t in L if 1 <= L[ t ] <= 10 )    

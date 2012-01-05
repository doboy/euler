from math import sqrt, ceil

TILES = 10 ** 6

print sum( ( x - y ) / 2 for x in xrange( 1, TILES / 4 + 2 )
           for y in ( int( ceil( sqrt( max( 1, x * x - TILES ) ) ) ), ) )

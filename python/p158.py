from utils import choose

print max( choose( 26, x ) * sum( choose( x, d ) - 1 for d in xrange( 1, x ) )
           for x in xrange( 2, 26 + 1 ) )

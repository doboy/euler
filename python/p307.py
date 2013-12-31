from utils import fact, choose
from math import log, exp

def p( k, n ):
    total = 0
    curr = choose( n, k / 2 + k % 2 )

    for r in xrange( k / 2 + k % 2, k + 1 ):
        total += curr
        curr = curr * ( n - r ) / ( r + 1 )

    return total * fact( k )

def logP( k, n ):
    total = 0
    curr = choose( n, k / 2 + k % 2 )

    for r in xrange( k / 2 + k % 2, k + 1 ):
        total += curr
        curr = curr * ( n - r ) / ( r + 1 )

    return log( total ) + log( fact( k ) )

defects, circuits = 2 * 10 ** 4, 10 ** 6
#defects, circuits = 2 * 10 ** 3, 10 ** 4
#print 1 - round( float( p( defects, circuits ) ) / circuits ** defects, 10 )

# print log( p( defects, circuits ) )
# print log(circuits ** defects)
# print defects * ( log( circuits ) )
#print 1 - round( exp( logP( defects, circuits ) - defects * log( circuits ) ), 10 )
#BUG?

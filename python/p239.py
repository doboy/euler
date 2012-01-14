from math import log, exp
from utils import fact, choose, product

def logFact( n ):
    return sum( log( i ) for i in xrange( 1, n + 1 ) )

def logChoose( n, k ):
    if n >= k >= 0:
        return logFact( n ) - logFact( k ) - logFact( n - k )
    else:
        return 0

def do( N ):
    ways = ( choose( 25, N ) 
             * product( xrange( 75, 100 - N ) )
             * fact( 75 ) )

    all = fact( 100 )
    ret = ways * 10 ** 50 / all
    print ret, N
    return ret

print sum( do ( n ) for n in xrange( 25 ) )


'''
    """
    logWays =                           
        # choose N prime numbers out of 25 to be the same
        logChoose( 25, N )
        # preserve the ordering of the N primes
        - logFact( N ) 
        # the combinations for the remaining 25 - N primes can be
        + sum( log( i ) for i in xrange( 75, 100 - N ) ) 
        # the combinations for the remaining composite numbers can be
        + logFact( 75 ) )
        
    logAll = logFact( 100 )
    """
    #print N, round( exp( logWays - logAll ), 12) 
'''

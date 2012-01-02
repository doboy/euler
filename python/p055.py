from utils import isPal

backwards = lambda n : int( str( n )[::-1] )

def isLychrel( n ):
    for i in xrange( 50 ):
        n = n + backwards( n )
        if isPal( str( n ) ):
            return False
    return True

print sum( 1 for x in xrange( 10 ** 4 ) if isLychrel( x ) )

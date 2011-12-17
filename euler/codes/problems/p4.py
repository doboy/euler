from utils import isPal

def pals():
    for i in xrange( 999, 100, -1 ):
        for j in xrange( 999, 100, -1 ):
            if( isPal( str( i * j ) ) ):
                yield i * j

print max( pals() )

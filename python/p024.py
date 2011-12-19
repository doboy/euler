from utils import fact, number

def lexiPerm( n, s ):
    y = sorted( s )
    if not n:
        return str( number( y ) )
    else:
        i = 0
        f = fact( len( s ) - 1 )
        while n - f >= 0:
            n -= f
            i += 1
        x = y[ i ]
        y.remove( y[ i ] )
        return str( x ) + lexiPerm( n, y )

print lexiPerm( 1000000 - 1, set( xrange(10) ) )

next = { 1 : ( None, 1 ) }

def length( i ):
    if i in next:
        return next[ i ][ 1 ]
    else:
        n = 3 * i + 1 if i % 2 else i / 2
        l = length( n ) + 1
        next[ i ] = n, l
        return l

print max( [ length( i ), i ] for i in xrange( 1, 10 ** 6 + 1 ) )[ 1 ]

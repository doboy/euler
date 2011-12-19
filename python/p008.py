def productGen( s ):
    a, b, c, d, e = map( int, s[:5] )
    yield a * b * c * d * e
    for i in xrange( 5, len( s ) ):
        a, b, c, d, e = b, c, d, e, int( s[ i ] )
        yield a * b * c * d * e

print max( productGen( open("../txt/p008" ).read() ) )

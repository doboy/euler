from utils import determinant, replaced

def solve( mapping ):
    """ returns the best polynomail given the mapping  Ax = b"""
    d = len( mapping )
    A, b = [], []
    for _x, _b in sorted( mapping.items() ):
        b.append( _b )
        A.append( [ _x ** i for i in xrange( d ) ] )    
    D = determinant( A )
    x = [ determinant( replaced( A, b, i ) ) / D for i in xrange( d ) ]
    return lambda n : sum( x[ i ] * n ** i for i in xrange( d ) )

u = lambda n : sum( ( -n ) ** i for i in xrange( 11 ) )
print sum( solve( { n : u( n ) for n in xrange( 1, i + 2 ) } )( i + 2 )
           for i in xrange( 10 ) )

# RELOOK, better to do inversion than determinants.
# POSSIBLE TO DO LAGRANGE

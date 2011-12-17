from utils import factors, product

f = {}
for i in xrange( 2, 21 ):
    ifactors = factors( i )
    for k in factors( i ):
        f[ k ] = max( f.get( k, 0 ), 
                      ifactors.get( k, 0 ) )

print product( k ** v for k, v in f.iteritems() )

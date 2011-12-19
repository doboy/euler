chars = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = { chars[ i ] : i for i in xrange( 1, len( chars ) ) }
names = sorted( eval( open( "../txt/p022" ).read() ) )

def score( wd ):
    return sum( map( points.get, wd ) )

print sum( ( i+1 ) * score( name )
           for i, name in enumerate( names ) )
    

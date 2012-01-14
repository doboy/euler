from utils import product

matrix = [ [ int( element ) for element in line.split() ]
           for line in open( "../txt/p011" ) ]

def productGen( matrix ):
    n = 20
    for i in xrange( n ):
        for j in xrange( n ):
            V, Vb = j <= 16, j >= 3
            H, Hb = i <= 16, i >= 3
            if V:
                yield product( matrix[ i ][ j + k ] for k in xrange( 4 ) )
            if H:
                yield product( matrix[ i + k ][ j ] for k in xrange( 4 ) )
            if H and V:
                yield product( matrix[ i + k ][ j + k ] for k in xrange( 4 ) )
            if Hb and V:
                yield product( matrix[ i - k ][ j + k ] for k in xrange( 4 ) )

print max( productGen( matrix ) )


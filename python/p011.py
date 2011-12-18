from utils import product

matrix = [ [ int( element ) for element in line.split() ]
           for line in open( "../txt/p11" ) ]

def productGen( matrix ):
    n = 20
    for i in xrange( n ):
        for j in xrange( n ):
            H = 2 <= j <= 17
            V = 2 <= i <= 17
            if H:
                yield product( matrix[ i ][ jj ] for jj in xrange( j - 2, j + 3 ) )
            if V:
                yield product( matrix[ ii ][ j ] for ii in xrange( i - 2, i + 3 ) )
            if H and V:
                yield product( matrix[ i + k ][ j + k ] 
                               for k in xrange( -2, 3 ) )
                yield product( matrix[ i - k ][ j + k ] 
                               for k in xrange( -2, 3 ) )
                
print max( productGen( matrix ) )
# SKIP

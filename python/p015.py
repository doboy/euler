N = 20

table = [ [ 1 for j in xrange( N+1 ) ] for i in xrange( N+1 ) ]

for i in xrange( 1, N+1 ):
    for j in xrange( 1, N+1 ):
        table[ i ][ j ] = table[ i - 1 ][ j ] + table[ i ][ j - 1 ]

print table[ -1 ][ -1 ]

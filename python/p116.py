def fill_count( n, m ):
    # n, b --> N
    # n blocks
    # has color block
    
    ways = { ( 0, True ) : 0,
             ( 0, False ) : 1 }
    
    for i in xrange( 1, n + 1 ):
        ways[ i, False ] = ways[ i - 1, False ]
        ways[ i, True ] = ways[ i - 1, True ] + \
            ( ways[ i - m, False ] + ways[ i - m, True ] ) if i - m >= 0 else 0

    return ways[ n, True ]


print sum([ fill_count( 50, 2 ), fill_count( 50, 3 ), fill_count( 50, 4 ) ])

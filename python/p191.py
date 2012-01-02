ways = {}
" days, current absents, late already? -> ways "

for a in xrange( 3 ):
    for l in ( True, False ):
        ways[ 0, a, l ] = 0

ways[ 0, 0, False ] = 1

for d in xrange( 1, 30 + 1 ):
    for a in xrange( 2 + 1 ):
        if a:
            # Absence
            ways[ d, a, False ] = ways[ d - 1, a - 1, False ]
            ways[ d, a, True ] = ways[ d - 1, a - 1, True ]
        else:
            # On Time
            ways[ d, 0, False ] = sum( ways[ d - 1, A, False ] for A in xrange( 2 + 1 ) )
            ways[ d, 0, True ] = sum( ways[ d - 1, A, True ] for A in xrange( 2 + 1 ) )

            # Late
            ways[ d, 0, True ] += sum( ways[ d - 1, A, False ] for A in xrange( 2 + 1 ) )

print sum( ways[ 30, a, l ] for a in xrange( 2 + 1 ) for l in ( True, False ) )

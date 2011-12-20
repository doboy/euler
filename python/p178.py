# Tags: Dynamic Programming

ways = {}
# digit, low, high, last -> ways

for last in xrange( 10 ):
    for low in xrange( 10 ):
        for high in xrange( low, 10 ):
            ways[ 1, low, high, last ] = 0

for last in xrange( 10 ):
    ways[ 1, last, last, last ] = 1

for d in xrange( 2, 40 + 1 ):
    for low in xrange( 10 ):
        for high in xrange( low, 10 ):
            for last in xrange( 10 ):
                ways[ d, low, high, last ] = 0
                if last < 9:
                    # plus
                    for higher in xrange( last + 1, 10 ):
                        ways[ d, low, high, last ] += ways[ d - 1, low, higher, last + 1 ]

                if last > 0:
                    # minus
                    for lower in xrange( last - 1 ):
                        ways[ d, low, high, last ] += ways[ d - 1, lower, high, last - 1 ]


print sum( ways[ 40, 2 ** 10 - 1, last ] for last in xrange( 10 ) )

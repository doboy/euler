# Tags: dynamic programming

D = 6

ways = {}
# digit, last -> ways

for last in xrange( 10 ):
    ways[ 1, last ] = 1

# find numbers strictly increasing
for digit in xrange( 2, D + 1 ):
    for last in xrange( 9 + 1 ):
        # Increasing
        ways[ digit, last ] = 0
        for low in xrange( last + 1 ):
            ways[ digit, last ] += ways[ digit - 1, low ]

print 2 * sum( ways[ D, last ] for last in xrange( 9 + 1 ) ) +\
    sum( ways[ digit, 0 ] for digit in xrange( 1, D + 1 ) )


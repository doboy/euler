from operator import mul

def fact( n ):
    return reduce( mul, xrange( n, 1, -1 ), 1 )

def choose(n, k):
    return fact( n )/ ( fact( n - k ) * fact( k ) )

for n in xrange( 150 ):
    import sys
    print >>sys.stderr, n
    for k in xrange( n + 1 ):
        print >>sys.stderr, '.' if choose( n, k ) % 7 else 'F',
    print >>sys.stderr

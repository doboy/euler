# Tags: Dynamic Programming

ways = {}
# digit, l, ll, z

for l in xrange( 10 ):
    for ll in xrange( 10 ):
        for b in True, False:
            ways[ 0, l, ll, b ] = 0

ways[ 0, 0, 0, True ] = 1

for d in xrange( 1, 20 + 1):
    for l in xrange( 10 ):
        for ll in xrange( 10 ):
            ways[ d, l, ll, False ] = sum( ways[ d, ll, lll ] for lll in xrange( 1, 10 )
                                           if l + ll + lll < 9 )
            ways[ d, l, ll, True ] = sum( ways[ d, ll, lll ] for lll in ( 0, )
                                          if l + ll + lll < 9 )
            

print sum( ways[ 20, l, ll, False ] 
           for l in xrange( 10 )
           for ll in xrange( 10 ) )

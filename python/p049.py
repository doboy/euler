from utils import primeGen, digits
from operator import add

s = {}

for prime in primeGen( start=1000, end=10000 ):
    d = tuple( sorted( digits( prime ) ) )
    if d not in s:
        s[ d ] = ()
    s[ d ] += ( prime, )

for d, ps in s.iteritems():
    if len( ps ) >= 3:
        l = len( ps )
        for i in xrange( l ):
            for j in xrange( i + 1, l ):
                for k in xrange( i + j, l ):
                    p1, p2, p3 = ps[ i ], ps[ j ], ps[ k ]
                    if p3 - p2 == p2 - p1 and p1 != 1487:
                        print reduce( add, map( str, ( p1, p2, p3 ) ) )

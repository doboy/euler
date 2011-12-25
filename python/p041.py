from utils import panGen, isPrime, lexiPermGen

m = 0
for n in xrange( 10 ):
    for p in lexiPermGen( vals=xrange( 1, n ) ):
        if isPrime( p ):
            m = max( p, m )

print m

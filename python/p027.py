from utils import primeGen, product, isPrime

def primeLen( a, b ):
    n = 0
    while isPrime( n ** 2 + a * n + b ):
        n += 1
    return n

def quadGen():
    for b in primeGen( 1000 ):
        for a in xrange( 1000 ):
            yield primeLen( a, b ), a, b
            yield primeLen( -a, b ), -a, b

l, a, b = max( quadGen() )
print a * b

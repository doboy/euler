from utils import primeGen, product

def cycle( a, b ):
    n = 0
    while isPrime( n ** 2 + a * n + b ):
        n += 1
    return n

def quadGen():
    for b in primeGen( 1000 ):
        for a in xrange( 1000 ):
            yield cycle( a, b ), a, b
            yield cycle( -a, b ), -a, b

def cycle( a, b ):
    return None

print product( max( quadGen() )[:2] )

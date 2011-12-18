from utils import primeGen

def primeUnderGen( n ):
    p = primeGen()
    o = p.next()
    while o < n:
        print o
        yield o
        o = p.next()
        
# print sum( p for p in primeUnderGen( 2 * 10 ** 6 ) )
# Takes too long

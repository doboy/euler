# Graph
  # MST
  # Clique
  # TSP
  # Independent Set
  # Vertex Cover
  # Max-Flow, Min-Cut
  # 3D Matching
  # Coloring
  # Hamitonian Cycle
  # Domnianting set
  # Exact Cover

# Priority Queue
  # Array 
  # Binary Heap
  # d-ary Heap
  # 
from operator import mul
from itertools import count as irange

def isPal( s ):
    for i in xrange( len( s )/2 ):
        if s[ i ] != s[ -( i + 1 ) ]:
            return False
    return True

# 5
def factors( n ):
    i, ret = 2, {}
    while n > 1:
        while not n % i:
            ret[ i ] = ret.get( i, 0 ) + 1
            n /= i
        i += 1
    return ret

def product( iterable ):
    ret = 1
    for i in iterable:
        ret *= i
    return ret

# 7, 27
def primeGen( max=None ):
    primesSoFar = []
    i = 2
    while True:
        for p in primesSoFar:
            if not i % p:
                break
        else:
            if max and i > max:
                return
            primesSoFar.append( i )
            yield i
        i += 1

# 9
def isSquare( n ):
    if n == 1: return True
    x = n // 2
    seen = set([ n ])
    while x * x != n:
        x = ( x + n // x ) // 2
        if x in seen:
            return False
        seen.add( x )
    return True

def triplesGen():
    for c in irange( 2 ):
        for b in xrange( c - 1, 0, -1 ):
            aSquare = c ** 2 - b ** 2
            if( isSquare( aSquare ) ):
                a = int( aSquare ** .5 )
                yield a, b, c

# 12, 45
def triangleGen():
    i = 1
    while True:
        yield i * ( i + 1 ) / 2
        i += 1

def pentagonGen():
    i = 1
    while True:
        yield i * ( 3 * i - 1 ) / 2
        i += 1

def hexagonGen():
    i = 1
    while True:
        yield i * ( 2 * i - 1 ) / 2
        i += 1

def divisors( n, proper=False ):
    ret = set([1,n]) if not proper else set([1])
    for i in xrange( 2, int( n ** .5 ) + 1 ):
        if not n % i:
            ret.add( i )
            ret.add( n // i )
    if isSquare( n ):
        ret.add( n ** .5 )
    return frozenset( ret )

# 17
def digit( n, i ):
    return n // 10 ** i % 10

def digitsGen( n ):
    while n:
        yield n % 10
        n //= 10


# 25
def fibGen():
    a = 1
    b = 1
    yield 1; yield 1
    while True:
        t = b
        b += a
        a = t
        yield b

# 27
# AKS primality test
def isPrime( n ):
    a = 1
    while a ** 2 <= n:
        b = 2
        while a ** b <= n:
            if a ** 2 == n:
                return False
            b += 1
        a += 1

    r = 1
    while ord( r, n ) <= log10( n ) ** 2:
        r += 1
    for a in xrange( 1, r ):
        if 1 < gcd( a, n ) < n:
            return False
    if n <= r:
        return True
    for a in xrange( 1, sqrt( tot( r ) ) * log( n ) ):
        if ( x+a ) ** n % n != ( X ** n + a ) % n:
            return False
    return True

def ord( n, a ):
    # a ** k = 1 mod n
    for k in xrange( 1, n + 1 ):
        if a ** k % n == 1:
            return k

def tot( n ):
    ret = 1
    return 1

# 31
def change( n, coins ):
    ways = { 0 : 1 }
    for i in xrange( 1, n + 1 ):
        ways[ i ] = sum( ways.get( i - c, 0 ) for c in coins )
    return ways[ n ]

# 45
def argmin( *seq ):
    return min( ( ( i, x ) for i, x in enumerate( seq ) ), key=lambda y: y[1] )[ 0 ]

# 52
def equals( *seq ):
    for x in seq:
        if seq[ 0 ] != x:
            return False
    return True
    

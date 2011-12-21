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
from math import sqrt, log10

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
    yield 2; yield 3
    primesSoFar = set()
    i = 5
    adder = 2
    while True:
        for p in primesSoFar:
            if not i % p:
                break
        else:
            if max and i > max:
                return
            primesSoFar.add( i )
            yield i
        i += adder
        adder = 6 - adder

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
    for i in xrange( 2, int( sqrt( n ) ) + 1 ):
        if not n % i:
            return True
    return isSquare( n )

def isPrimeAKS( n ):
    # STEP 0
    if n == 1:
        return False

    # STEP 1
    a = 2
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

    for a in xrange( 1, int( sqrt( tot( r ) ) * log10( n ) ) + 1 ):
        if ( X + a ) ** n % n != ( X ** n + a ) % n:
            return False
    return True

def ord( n, a ):
    # a ** k = 1 mod n
    for k in xrange( 1, n + 1 ):
        if a ** k % n == 1:
            return k

def tot( n ):
    ret = n
    for p in primeGen( n ):
        if not n % p:
            ret = ret * ( p - 1 ) // p
    return ret

def gcd( a, b ):
    while b:
        a, b = b, a % b
    return a

# 31
def change( n, coins ):
    ''' ways[ a, b ] means there are that many ways to get a amount using
    coins [ 0 .. b ) '''
    ways = {}
    for i in xrange( len( coins ) ):
        ways[ 0, i ] = 1
    for i in xrange( 1, n + 1 ):
        for c, cc in enumerate( coins ):
            ways[ i, c ] = ( ways[ i - cc, c ] if i - cc >= 0 else 0 ) +\
                ( ways[ i, c - 1 ] if c else 0 )
    return ways[ n, len( coins ) - 1 ]

# 45
def argmin( *seq ):
    return min( ( ( i, x ) for i, x in enumerate( seq ) ), key=lambda y: y[1] )[ 0 ]

# 52
def equals( *seq ):
    for x in seq:
        if seq[ 0 ] != x:
            return False
    return True
    
# 19
def dateGen( start, end, delta ):
    n = start
    while n <= end:
        yield n.day
        n += delta
# 24
def fact( n ):
    r = 1
    for i in xrange( 1, n + 1 ):
        r *= i
    return r

def number( seq ):
    r = 0
    for x in seq:
        r = r * 10 + x
    return r

# 63
def count( seq ):
    return sum( 1 for x in seq )

# 83
class Vertex:
    pass

class Edge:
    pass

class Graph:
    
    def __init__( self, E, V ):
        self.Edges = E
        self.Vertices = V

    def shortestPath( self, s ):
        H = [ s ]
        dist = { s : 0 }
        while H:
            e = heapppop( H )
            for e, v in self.edges( e ):
                pass


# 114, 115, 116
def fill_count( n, m ):
    # n, b --> N
    # n blocks used,
    # b ending in red

    ways = { ( 0, True ) : 0,
             ( 0, False ) : 1 }

    for i in xrange( 1, n + 1 ):
        ways[ i, False ] = ways[ i - 1, True ] + ways[ i - 1, False ]
        ways[ i, True ] = 0
        for s in xrange( i - m + 1 ):
            ways[ i, True ] += ways[ s, False ]

    return ways[ n, True ] + ways[ n, False ]

# 188
def hyperexpo( a, b, m ):
    r = a
    while b:
        r = pow( a, r, m )
        b -= 1
    return r

# 36
def isBinaryPal( n ):
    temp = n
    reverse = 0
    while temp:
        reverse <<= 1
        reverse += temp & 1
        temp >>= 1
    return n == reverse
        
def isDecimalPal( n ):
    temp = n
    reverse = 0
    while temp:
        reverse *= 10
        reverse += temp % 10
        temp //= 10
    return n == reverse
        
# 22, 42
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = { chars[ i ] : i + 1 for i in xrange( len( chars ) ) }

# 42

def isTriangle( n ):
    s = int( sqrt( n * 2 ) )
    return 2 * n == s * ( s + 1 )

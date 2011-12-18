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

# 7
def primeGen():
    primesSoFar = []
    i = 2
    while True:
        for p in primesSoFar:
            if not i % p:
                break
        else:
            primesSoFar.append( i )
            yield i
        i += 1

# 9
def isSquare( n ):
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

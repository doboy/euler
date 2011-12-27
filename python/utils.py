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
def primeGen( end=float("inf"), start=0 ):
    yield 2; yield 3
    primesSoFar = set()
    i = 5
    adder = 2
    while True:
        for p in primesSoFar:
            if not i % p:
                break
        else:
            if i > end:
                return
            primesSoFar.add( i )
            if i > start:
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
    # a < b < c
    for c in irange( 2 ):
        for b in xrange( c - 1, c // 2 - 1, -1 ):
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
        yield i * ( 2 * i - 1 )
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

def digits( n ):
    ret = ()
    while n:
        ret = ( n % 10, ) + ret
        n //= 10
    return ret

def number( seq ):
    r = 0
    for x in seq:
        r = r * 10 + x
    return r

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
    if n <= 1:
        return False
    for i in xrange( 2, int( sqrt( n ) ) + 1 ):
        if not n % i:
            return False
    return not isSquare( n )

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

def score( wd ):
    return sum( map( points.get, wd ) )
    
# 42

def isTriangle( n ):
    s = int( sqrt( n * 2 ) )
    return 2 * n == s * ( s + 1 )

# 68

class modList( list ):

    def __init__( self, mod, *vals ):
        self.mod = mod
        list.__init__( self, vals )
        
    def __getitem__( self, i ):
        return list.__getitem__( self, i % mod )

    def __setitem__( self, i, x ):
        return __setitem__( self, i, x )

# Abstract class
class CSP:
    
    def __init__( self ):
        pass

    def getPossibleMoves( self, move ):
        pass

    def doMove( self, move ):
        pass

    def undoMove( self, move ):
        pass
    
    def solve( self ):
        pass

class magic3gon( CSP ):
    
    def __init__( self ):
        # self.positions = { s, i for s in ( "in", "out" ) for i in xrange( 3 ) }
        self.next = "in", 0
        self.moves = []
        self.canUse = set( xrange( 1, 7 ) )
        self.constraints = [ lambda : self.positions[ "in", 0 ] < 8 ]

    def getPositions( self ):
        ''' Even is inside, Odd is outside
        -2, 0, 1 share constraint -1,
        0, 2 , 3 share constraint 0,
        2, 4, 5, share constraint 1,
        In general i, i + 2, i + 3 ( mod N ) share constraint i/2 mod N/2,
        Conversely position i has contraints i/2, '''
        pass
        
    def getConstraints( self ):
        '''Conversly constraint i says ii + ii + 2 + ii + 3 == X '''
        # return modList( 3, [ lambda : not self.positions[ i * 2 ] or not self.positions[ i * 2 + 2 ] or not self.positions[ i * 2 + 3 ] or 
        #                      self.positions[ i * 2 ] + self.positions[ i * 2 + 2 ] + self.positions[ i * 2 + 3 ] == self.X for i in xrange( 3 ) ] )
        pass


    def getPossibleMoves( self ):
        possibleMoves = set()
        for x in self.canUse:
            self.positions[ self.next ] = x
            if isGood( self.next ):
                possibleMoves.add( x )
            self.positions[ self.next ] = None

    @staticmethod
    def opposite( wd ):
        return "in" if word is "out" else "out"

    def setNextMove( self ):
        self.next = opposite( self.next[ 1 ] ), ( self.next[ 1 ] + 1 ) % 3

    def setPrevMove( self ):
        self.next = opposite( self.next[ 1 ] ), ( self.next[ 1 ] - 1 ) % 3

# 98
def mapReduce( elements, 
               mapper,
               reducer=lambda tup, el: tup + ( el, ), 
               base=(),
               keyfilter=lambda _: True, valfilter=lambda _:True ):
    mapped = map( mapper, elements )
    mappee = {}
    for k, v in mapped:
        if keyfilter( k ) and valfilter( v ):
            if k not in mappee:
                mappee[ k ] = []
            mappee[ k ].append( v )
    
    if reducer:
        reducee = {}
        for k, v in mappee.iteritems():
            reducee[ k ] = reduce( reducer, v, base )

    # is filter done on the keys or values? I assume keys
    # makes sense for problem 98
    
    return reducee

# 35
def rotated( n, digits ):
    return n // 10 + ( n % 10 ) * 10 ** digits

def baseGen( goods, start=0, end=float("inf") ):
    def transform( num ):
        ret = 0
        index = 0
        while num:
            ret += goods[ num % len( goods ) ] * 10 ** index
            num //= len( goods )
            index += 1
        return ret

    i = 0
    t = transform( i )
    while t < start:
        i += 1
        t = transform( i )

    while t < end:
        yield t
        i += 1
        t = transform( i )


# 33
def reduceFraction( n, d ):
    g = gcd( n, d )
    return n / g, d / g

# 38
def panGen( n, z=False ):
    pass

def lexiPerm( n, s ):
    y = sorted( s )
    if not n:
        return str( number( y ) )
    else:
        i = 0
        f = fact( len( s ) - 1 )
        while n - f >= 0:
            n -= f
            i += 1
        x = y[ i ]
        y.remove( y[ i ] )
        return str( x ) + lexiPerm( n, y )

def lexiPermGen( vals, start=0, end=None ):
    if not end:
        end = fact( len( vals ) )
    s = start
    while s < end:
        yield int( lexiPerm( s, vals ) )
        s += 1

# 81, 82, 83
import heapq

class graphSearch( object ):

    def __init__( self, fringe, successorFn, goalState, distFn ):
        self.fringe = fringe
        self.successorFn = successorFn
        self.goalState = goalState
        self.distFn = distFn
        self.seen = set()

    def search( self ):
        ''' searches for the goal state '''
        while self.fringe:
            node = self.pop( self.fringe )
            dist = self.getDist( node )
            state = self.getState( node )
            if state not in self.seen:
                self.previsit( node )
                self.seen.add( state )
                if self.goalState( state ):
                    return dist
                for _node in self.expand( node ):
                    self.add( self.fringe, _node )

    @staticmethod
    def getState( node ):
        return node[ 1 ]
    
    @staticmethod
    def getDist( node ):
        return node[ 0 ]

    def add( self, fringe, to ):
        ''' adds a node to the fringe '''

    def pop( self, fringe ):
        ''' returns an element on the fringe to explore'''

    def expand( self, node ):
        ''' given a node it expands the node '''
        dist = self.getDist( node )
        state = self.getState( node )
        for _state in self.successorFn( state ):
            yield dist + self.distFn( state, _state ), _state

    def previsit( self, node ):
        ''' given a node it does some previsit things '''

class bfSearch( graphSearch ):

    def __init__( self, fringe, successorFn, goalStateFn, distFn ):
        graphSearch.__init__( self, fringe, successorFn, goalStateFn, distFn )
        
    def add( self, fringe, to ):
        fringe.append( to )

    def pop( self, fringe ):
        return fringe.pop( 0 )

class dfSearch( graphSearch ):
    def __init__( self, fringe, successorFn, goalStateFn, distFn ):
        graphSearch.__init__( self, fringe, successorFn, goalStateFn, distFn )
        
    def add( self, fringe, to ):
        fringe.append( to )

    def pop( self, fringe ):
        return fringe.pop()

class pqSearch( graphSearch ):
    def __init__( self, fringe, successorFn, goalStateFn, distFn ):
        graphSearch.__init__( self, fringe, successorFn, goalStateFn, distFn )
        heapq.heapify( self.fringe )

    def add( self, fringe, to ):
        heapq.heappush( fringe, to )
    
    def pop( self, fringe ):
        return heapq.heappop( fringe )
    
class primSearch( pqSearch ):
    def __init__( self, fringe, successorFn, distFn, goalStateFn=lambda _: False ):
        pqSearch.__init__( self, fringe, successorFn, goalStateFn, distFn )
        self.prev = {}

    def expand( self, node ):
        ''' given a node it expands the node '''
        state = self.getState( node )
        for _state in self.successorFn( state ):
            if _state not in self.seen:
                yield self.distFn( state, _state ), _state, state

    def previsit( self, node ):
        ''' given a node it does some previsit things '''
        self.prev[ self.getState( node ) ] = self.getPrev( node )

    @staticmethod
    def getPrev( node ):
        return node[ 2 ]

def order( n ):
    ''' return the number of zeros of n '''
    f = 5
    r = 0
    while n and not n % f:
        r += n // f
        f *= f
    return r

def orderC( n, r ):
    ''' return the number of zeros of n choose r '''
    return order( n ) - order( n - r ) - order( r )


def choose( n, r ):
    '''n choose r = n! / r! * ( n-r )! <==> n * n-1 * .. * n-r+1 / r!'''
    return product( xrange( n - r + 1, n + 1 ) ) \
        / product( xrange( 1, r + 1 ) )

# 57
class fraction:

    def __init__( self, n, d=1 ):
        self.n, self.d = n, d

    def reduce( self ):
        g = gcd( self.n, self.d )
        self.n //= g
        self.d //= g

    def __add__( self, other ):
        l = lcm( self.n, self.d )
        return fraction( self.n * self.d / l + other.n * other.d / l,
                         l )

# krustal's

def krustals( graph ):
    weightTotal = [0]
    MST = set()

    def union( edge ):
        e1, e2 = edge
        p1, p2 = find( e1 ), find( e2 )

        if rank[ p1 ] > rank[ p2 ]:
            parent[ p2 ] = p1
        else:
            parent[ p1 ] = p2
            if rank[ p1 ] == rank[ p2 ]:
                rank[ p2 ] += 1

        MST.add( edge )
        weightTotal[ 0 ] += edge.weight

    def find( vertex ):
        if vertex != parent[ vertex ]:
            parent[ vertex ] = find( parent[ vertex ] )
        return parent[ vertex ]

    rank = { vertex : 0 for vertex in graph.vertices }
    parent = { vertex : vertex for vertex in graph.vertices }

    for edge in sorted( graph.edges ):
        vStart, vEnd = edge
        if find( vStart ) != find( vEnd ):
            union( edge )

    return weightTotal[ 0 ], MST

class discreteDist:
    def __init__( self, min, max, values ):
        self.min = min
        self.max = max
        self.values = values
        self.setPdf()
        self.setCdf()

    def setPdf( self ):
        ''' P[ x = i ], calculates the pdf 
        must be implemented by derived class'''
        
    def setCdf( self ):
        ''' P[ x <= i ], calculates the cdf '''
        cdf = 0
        for val in sorted( self.values ):
            cdf += self.pdf[ val ]
            self.cdf[ val ] = cdf
        
    def getPdf( self, val ):
        if min <= val <= max:
            return self.pdf[ val ]

    def getCdf( self, val ):
        if min <= val <= max:
            return self.cdf[ val ]
        else:
            return 0 if val <= min else 1

    def getExpectation( self ):
        return sum( val * prob for val, prob in self.pdf.iteritems() )

from utils import digitsGen, number

g = { 2 : 2, 3 : 3, 4 : 5, 5 : 7, 6 : 11, 7 : 13, 8 : 17 }

def specialGen():
    for i in xrange( 58, 6 - 1, -1 ):
        if len( set( digitsGen( i * 17 ) ) ) == 3:
            for e in explore( i * 17 ):
                yield e

def explore( i ):
    used = tuple( digitsGen( i ) )
    unused = frozenset( xrange( 9 ) ) - set( used )
    fringe = [( 8, used, unused )]
    while fringe:
        node = fringe.pop()
        if goalState( node ):
            yield node; continue
        elif isGood( node ):
            fringe += expand( node )

def goalState( (d, _, __) ):
    return d == 1

def isGood( (d, used, _) ):
    return not ( used[ -1 ] * 100 + used[ -2 ] * 10 + used[ -3 ] ) % g[ d ] 

def expand( (d, used, unused) ):
    return [ ( d - 1, used + ( u, ), unused - { u } ) for u in unused ]

print sum( number( reversed( used ) ) for _, used, _ in specialGen() )
# BUG

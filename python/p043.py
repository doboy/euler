from utils import digits, number

g = { 2 : 2, 3 : 3, 4 : 5, 5 : 7, 6 : 11, 7 : 13, 8 : 17 }
numbers = frozenset( xrange( 10 ) )
fringe = [ ( 8, digits( x * 17 ), numbers - set( digits( x * 17 ) ) )
           for x in xrange( 1000 / 17, 100 / 17, -1 )
           if len( set( digits( x * 17 ) ) ) == 3 ]

def successorFn( (d, used, unused) ):
    return [ ( d - 1, ( u, ) + used, unused - { u } ) for u in unused ]

def goalState( ( d, _, __ ) ):
    return d == 1

def isGood( (d, used, _) ):
    return not number( used[:3] ) % g[ d ] 

def explore( fringe ):
    while fringe:
        node = fringe.pop()
        if goalState( node ):
            yield node; continue
        elif isGood( node ):
            fringe += successorFn( node )

print sum( number( used ) for _, used, _ in explore( fringe ) )

from utils import primSearch
from ast import literal_eval

distanceTable = { }
totalDist = 0

for i, line in enumerate( open( "../txt/p107" ) ):
    for j, num in enumerate( line.split( "," ) ):
        if '-' in num:
            continue
        num = literal_eval( num )
        if i not in distanceTable:
            distanceTable[ i ] = {}
        distanceTable[ i ][ j ] = num
        totalDist += num
totalDist /= 2

fringe = [ ( 0, 0, None ) ]

def successorFn( state ):
    i = state
    for j, distance in distanceTable[ i ].iteritems():
        yield j

def distFn( from_, to_ ):
    return distanceTable[ from_ ][ to_ ]

prim = primSearch( fringe=fringe,
                   successorFn=successorFn,
                   distFn=distFn )

prim.search()


print totalDist
print sum( distFn( k, v ) for k, v in prim.prev.iteritems() if v )
print totalDist - sum( distFn( k, v ) for k, v in prim.prev.iteritems() if v )

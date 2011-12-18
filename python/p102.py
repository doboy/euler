from math import acos, pi
from operator import *

def hasOrigin( vertices ):
    v0 = vertices[ 0 ]
    v1 = vertices[ 1 ]
    v2 = vertices[ 2 ]

    x =  angleBetween( v0, v1 ) + angleBetween( v1, v2 ) + angleBetween( v2, v0 )

    return x > 6.283


def angleBetween( v1, v2 ):
    return acos( dotProduct( v1, v2 ) / (mag( v1 ) * mag( v2 )))

def dotProduct( v1, v2 ):
    return sum( map( mul, v1, v2 ) )

def mag( v1 ):
    return sum( map( lambda x : x ** 2, v1 ) )**.5


total = 0
nontotal = 0
file = open( "triangles.txt" )
for line in file:
    tokens = map( int, line.split(',') )
    v0 = tokens[:2]
    v1 = tokens[2:4]
    v2 = tokens[4:]
    if hasOrigin( (v0, v1, v2 ) ):
        total += 1
    else:
        nontotal += 1

print nontotal
print total

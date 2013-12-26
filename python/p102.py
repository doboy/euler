from math import pi
from utils import angleBetween, dotProduct, mag

def hasOrigin( v0, v1, v2 ):
    return angleBetween( v0, v1 ) + angleBetween( v1, v2 ) + angleBetween( v2, v0 ) > 6.283

triangles = set()
for line in open( "txt/p102" ):
    v0x, v0y, v1x, v1y, v2x, v2y = map( int, line.split( ',' ) )
    triangles.add( ( ( v0x, v0y ), ( v1x, v1y ), ( v2x, v2y ) ) )

print sum( 1 for v0, v1, v2 in triangles if hasOrigin( v0, v1, v2 ) )

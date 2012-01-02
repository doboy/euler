from utils import equals, digits

def isGood( n ):
    return equals( *map( lambda x : frozenset( digits( x ) ),
                        ( n * i for i in xrange( 1, 7 ) ) ) )

i = 1
while True:
    if( isGood( i ) ):
        break
    i += 1

print i

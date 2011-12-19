from utils import digitsGen, equals

def isGood( n ):
    return equals( *map( lambda x : frozenset( digitsGen( x ) ), 
                        ( n * i for i in xrange( 1, 7 ) ) ) )

i = 1
while True:
    if( isGood( i ) ):
        break
    i += 1

print i

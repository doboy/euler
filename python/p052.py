from utils import equals, digits

def isGood( n ):
    return equals( *map( lambda x : sorted( digits( x ) ),
                         ( n * i for i in xrange( 1, 7 ) ) ) )

def find():
    for e in xrange( 1, 10 ):
        for x in xrange( 10 ** e, 10 ** ( e + 1 ) / 6 + 1 ):
            if( isGood( x ) ):
                return x

print find()

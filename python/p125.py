from utils import isPal

squares = [ x * x for x in xrange( 1, 10 ** 4 / 2 ) ]
squareCum = []

cum = 0
for i, suare in enumerate( squares ):
    cum += squares[ i ]
    squareCum.append( cum )

def squarePalGen():
    for i, x in enumerate( squareCum ):
        for j, y in enumerate( squareCum ):
            if i <= j + 1:
                break
            elif isPal( str( x - y ) ):
                yield x - y

print sum( set( squarePalGen() ) )
# URGENT

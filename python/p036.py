from utils import isBinaryPal, isDecimalPal

def palindromGen():
    for x in xrange( 10 ** 6 ):
        if isDecimalPal( x ) and isBinaryPal( x ):
            yield x

print sum( palindromGen() )
# RELOOK

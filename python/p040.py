from utils import product, digits

def d( n ):
    d = 1
    while n - d * ( 10 ** d - 10 ** ( d - 1 ) ) > 0:
        n -= d * ( 10 ** d - 10 ** ( d - 1 ) )
        d += 1

    s = 10 ** ( d - 1 )
    while n - d > 0:
        s += 1
        n -= d

    for digit in digits( s ):
        n -= 1
        if not n:
            return digit

print product( d( 10 ** e ) for e in xrange( 7 ) )


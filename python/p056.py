from utils import digits

def digitsSum():
    for a in xrange( 100 ):
        for b in xrange( 100 ):
            yield sum( digits( a ** b ) )

print max( digitsSum() )

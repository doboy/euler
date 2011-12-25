from utils import digitsGen

def digitsSum():
    for a in xrange( 100 ):
        for b in xrange( 100 ):
            yield sum( digitsGen( a ** b ) )

print max( digitsSum() )

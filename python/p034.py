from utils import fact, digits

LIMIT = 50000

def curiousGen():
    for x in xrange( 10, LIMIT ):
        if x == sum( map( fact, digits( x ) ) ):
            yield x

print sum( curiousGen() )

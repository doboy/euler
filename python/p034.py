from utils import digitsGen, fact

LIMIT = 50000

def curiousGen():
    for x in xrange( 10, LIMIT ):
        if x == sum( map( fact, digitsGen( x ) ) ):
            yield x

print sum( curiousGen() )

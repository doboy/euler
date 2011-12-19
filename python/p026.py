from utils import primeGen

def cycle_len( p ):
    # TODO
    return 1

def cycleGen( d ):
    for p in primeGen( d ):
        yield cycle_len( p )

print max( cycleGen( 1000 ) )

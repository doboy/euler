from utils import primeGen

def cycle_len( p ):
    cycle = {}
    dividand = 1
    while dividand not in cycle:
        while p < dividand:
            dividand *= 10
        cycle[ dividand ] = dividand % p
        dividand %= p
    # TODO
    return 1

def cycleGen( d ):
    for p in primeGen( d ):
        yield cycle_len( p )

# print max( cycleGen( 1000 ) )
# TODO

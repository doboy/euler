from utils import fibGen, isOdd

print sum( x for x in fibGen( 4 * 10 ** 6 ) if not isOdd( x ) )

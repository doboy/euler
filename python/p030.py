from utils import digits

LIMIT = 6 * 9 ** 5

def powerSumGen( p, limit ):
    for i in xrange( 10, limit + 1 ):
        if i == sum( map( lambda x : x ** p, digits( i ) ) ):
            yield i

print sum( powerSumGen( 5, LIMIT ) )

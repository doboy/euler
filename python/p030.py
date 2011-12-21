from utils import digitsGen

LIMIT = 6 * 9 ** 5

def powerSumGen( p, limit ):
    for i in xrange( 10, limit + 1 ):
        if i == sum( map( lambda x : x ** p, digitsGen( i ) ) ):
            yield i

print sum( powerSumGen( 5, LIMIT ) )

# Look Over

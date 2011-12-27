from utils import product, choose

def countGen():
    for n in xrange( 1, 101 ):
        for r in xrange( 1, n // 2 + 1 ):
            if choose( n, r ) > 10 ** 6:
                yield 2 if n - r != r else 1

print sum( countGen() )

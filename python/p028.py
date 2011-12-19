def diagnolGen( diag=1001 ):
    a = 1
    i = 2
    yield 1
    while i < diag:
        for _ in xrange( 4 ):
            a += i
            yield a
        i += 2

print sum( diagnolGen() )

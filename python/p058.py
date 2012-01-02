from utils import isPrime

def layerGen():
    x = 2
    s = 2
    while True:
        yield xrange( x, x + s * 4 + 1 )
        x = x + s * 4
        s += 4

layer = 0
lgen = layerGen()
primes, all = 0., 1
while primes / all > .1:
    for val in next( lgen ):
        if isPrime( val ):
            primes += 1
        all += 1
    layer += 1

# RELOOK


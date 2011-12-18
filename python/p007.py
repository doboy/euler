from utils import primeGen

p = primeGen()
for i in xrange( 10000 ):
    p.next()
print p.next()

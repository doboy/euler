from utils import primeGen

p = primeGen()
for i in xrange( 10000 ):
    p.next()
print p.next()

# print last( next( p ) for p in xrange( 10000 ) )
# RELOOK

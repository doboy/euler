from utils import divisors

a = [] # abundant numbers
c = set(xrange(28124)) # numbers that cant be written as abundant numbers
MAX = 28124

for x in xrange( 1, MAX ):
    if( sum( divisors( x, proper=True ) ) > x ):
        a.append( x )
        for y in a:
            if x + y > MAX:
                break
            elif x + y in c:
                c.remove( x + y )

print sum( c )

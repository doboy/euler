from utils import divisors

pd = {} #properDivisors
a = set() #amicableNumbers

def dpd( n ):
    if n in pd: 
        return pd[ n ]
    else:
        pd[ n ] = sum( divisors( n, proper=True ) )
        return pd[ n ]

for i in xrange( 1, 10001 ):
    if i == dpd( dpd( i ) ) and i != dpd( i ):
        a.add( i )
        a.add( dpd( i ) )

print sum( a )

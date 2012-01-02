''' (a - 1) ** n + (a + 1) ** n % a ** 2 is...
2an when n is odd, and 2 when odd is even '''

rMax = ( lambda a : 
         a ** 2 - a if a % 2 
         else a ** 2 - 2 * a )

print sum( rMax( a ) for a in xrange( 3, 1001 ) )

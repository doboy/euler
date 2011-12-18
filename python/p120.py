''' (a - 1) ** n + (a + 1) ** n % a ** 2 is...
2an when n is odd, and 2 when odd is even '''

def Rmax( a ):
    if a % 2:
        return a**2 - a
    else:
        return a**2 - 2*a
t = 0
for a in xrange( 3, 1001):
    t+=Rmax( a )

print t

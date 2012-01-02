from utils import isPrime

def Goldbach( c ):
    for s in xrange( int( ( c / 2. ) ** .5 + 1 ) ):
        if isPrime( c - 2 * s ** 2 ):
            return True
    print s, c - 2 * s ** 2
    return False

c = 4
while True:
    if not isPrime( c ) and not Goldbach( c ):
        break
    c += 1

print c
# URGENT

s = set()

def isTrunc( n ):
    f = n
    b = 0
    while f:
        b = b * 10 + f % 10
        if not isPrime( f ):
            return False
        f //= 10

    while b:
        if not isPrime( f ):
            return False
        b //= 10
    
    return True

i = 8
while len( s ) < 11:
    if( isTrunc( i ) ):
        s.add( i )
    i += 1

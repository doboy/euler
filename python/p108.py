from Prime import lcm

def diophate( n ):
    t = 0
    for x in xrange( n, 2*n + 1 ):
        l = lcm( n , x )
        if l // n - l // x == 1:
            t += 1
    return t

n = 2
while True:
    if diophate( n ) > 1000:
        break
    print n, diophate( n )
    n+=1

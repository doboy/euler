## FOR EVERY 5, remove a 2 from answer


def func( i, n ):
    f = 0
    while not i % 5:
        f += 1
        i/=5
    return i + n, f

fcount = 0
n = 1
e = 1000000000000
e = 20
for i in xrange( 1, e + 1 ):
    print i
    n, fcount = func( i, n ) 
    while fcount and not n % 2:
        n /= 2
        fcount -= 1
    n = n % 100000
print n

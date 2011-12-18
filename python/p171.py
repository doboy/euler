'''
vals = set()

def digits( sum=0, values=(), digit=0, amount=21 ):
    if isSquare( sum ):
        vals.add( values )
        print "***",values
    if digit == 20:
        return
    else:
        for i in xrange( 1, amount + 1 ):
            digits( sum + i**2, values + (i,), digit + 1, i )

def isSquare( num ):
    x = num // 2
    seen = set([x])
    while x * x != num:
        x = ( x + ( num // 2 ) ) // 2
        if x in seen: return False
        seen.add( x )
    return True

digits()

for val in vals:
    print val
'''

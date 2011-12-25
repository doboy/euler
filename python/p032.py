from utils import digitsGen

s = set()

def digitsUsed( *numbers ):
    ret = []
    for number in numbers:
        for digit in digitsGen( number ):
            if not digit:
                return []
            else:
                ret.append( digit )
    return ret

a = 2
while True:
    b = 2
    if 0 in digitsGen( a ):
        a += 1
        continue

    if len( digitsUsed( a, b, a * b ) ) > 9:
        break

    while True:
        if 0 in digitsGen( b ):
            b += 1
            continue

        used = digitsUsed( a, b, a * b )
        if 9 == len( used ) == len( set( used ) ):
            s.add( a * b )
        elif len( used ) > 9:
            break
        b += 1

    a += 1

print sum( s )

# RELOOK

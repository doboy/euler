from utils import primeGen

def hasFactors( n, m ):
    ''' checks if it has m factors '''
    for x in primeGen( n ):
        if not n % x:
            if not m:
                return False
            m -= 1
    return not m

# a, b, c, d = map( hasFactors, xrange( 1, 5 ), ( 4, ) * 4 )

# print map( hasFactors, xrange( 134043, 134043 + 4 ), ( 4, ) * 4 )
# raw_input()
'''
i = 5
while not a or not b or not c or not d:
    a, b, c, d, = b, c, d, hasFactors( i, 4 )
    if not i % 1000:
        print i
    if i > 134043:
        print "whooa..", i
    i += 1

print i
'''

from utils import fact, digits

ends = { 1: False, 89: True}

def check( n ):
    if n in ends:
        return ends[ n ]
    else:
        ends[ n ] = check( sum( map( lambda x : x * x, 
                                     digits( n ) ) ) )
        return ends[ n ]

# print sum( 1 for i in xrange( 1, 10 ** 7 ) if check( i ) )
# Takes too long 90ish seconds

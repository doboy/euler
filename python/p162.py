def F( k ):
    """ With exactly k digits, return the number of ways 
    to have numbers that do not have 0, 1 or A """
    return (
        # Numbers that dont have 1, A, or 0
        ( 14 + 14 + 15 ) * 15 ** ( k - 1 ) -
        # Numbers that dont have 1 + A, 1 + 0, A + 0
        ( 13 + 14 + 14 ) * 14 ** ( k - 1 ) +
        # Numbers that dont have 1 + A + 0
        13 * 13 ** ( k - 1 ) )

def G( k ):
    """ With exactly k digits, return the number of ways
    to have numbers that have 0, 1 and A """
    return 15 * 16 ** ( k - 1 ) - F( k )

print "%X" % sum( G( k ) for k in xrange( 1, 16 + 1 ) )

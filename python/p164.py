from utils import memoize

@memoize
def ways( d, mid, old ):
    """ Currently on the dth digit how many ways is there to do it if
    the two previous elements are in lastlast and last. Assume d >= 2 """
    if d <= 2:
        return 1 if ( mid and mid + old <= 9 ) else 0
    else:
        return sum( ways( d - 1, new, mid ) 
                    for new in xrange( 10 ) 
                    if new + mid + old <= 9 )

print sum( ways( 20, mid, old ) 
           for mid in xrange( 10 ) 
           for old in xrange( 10 ) )

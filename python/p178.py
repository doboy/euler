from utils import memoize

@memoize
def ways( d, seen=0, last=None ):
    """ d digits left and have seen seen and just seen last. """
    if d == 0:
        return seen == 0b1111111111
    else:
        if last is None:
            return ( sum( ways( d - 1, ( 1 << new ), new ) 
                          for new in xrange( 1, 10 ) )
                     + ways( d - 1 ) )
        else:
            return sum( ways( d - 1, seen | ( 1 << new ), new )
                        for new in ( last - 1, last + 1 )
                        if new > -1 and new < 10 )

print ways( 40 )

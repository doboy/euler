from utils import memoize
from math import log

'''
@memoize
def change( n ):
    """ ways we can get num by using { 1 ** 2 .. pow ** 2 } once or twice """
    if n < 3:
        return n
    else:
        k = n >> 1
        return change( k ) if n % 2 else change( k ) + change( k - 1 )

print change( 10 ** 25 )
'''

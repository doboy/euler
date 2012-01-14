hash = { x : 0 for x in xrange( 250 ) }

for x in xrange( 1, 250250 + 1 ):
    hash[ pow( x, x, 250 ) ] += 1

# DIVIDE AND CONQUER?

singles = { (  x, "S" + str(x)) for x in range( 1, 21 ) + [ 25 ] }
doubles = { (2*x, "D" + str(x)) for x in range( 1, 21 ) + [ 25 ] }
trebles = { (3*x, "T" + str(x)) for x in range( 1, 21 ) }
zeros = { ( 0, "Z0" ) }
all = sorted( zeros | singles | doubles | trebles )

score = lambda x : x[ 0 ]

def outGen():
    for double in doubles:
        for i in xrange( len( all ) ):
            if score( all[ i ] ) + score( double ) >= 100:
                break

            for j in xrange( i + 1 ):
                if score(all[ i ]) + score(all[ j ]) + score( double ) >= 100:
                    break

                yield all[ i ], all[ j ], double

print sum( 1 for x in outGen() )

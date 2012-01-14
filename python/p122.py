"""
inf = float("inf")

bests = { 1 : { frozenset([ 1 ]) } }

total = 0
for x in xrange( 2, 201 ):
    minimal = inf
    minimals = None

    for m in xrange( 1, x ):
        for best0 in bests[ m ]:
            for best1 in bests[ x - m ]:
                s = ( best0 | best1 ) | frozenset([ x ])
                l = len( s )

                if l < minimal:
                    minimal = l
                    minimals = { s }

                elif l == minimal:
                    minimals.add( s )

    bests[ x ] = minimals
    total += minimal - 1

print total
"""

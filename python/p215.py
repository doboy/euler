"""
ways = { 0 : frozenset() }

for width in xrange( 1 , 9 ):
    all = set([ width ])
    for block in ( 2, 3 ):
        if width - block >= 0:
            for way in ways[ width - block ]:
                all.add( way | { width - block } )
    ways[ width ] = frozenset( all )

for k, v in ways.items():
    print k, v
TODO
"""

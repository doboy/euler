s = set()

for a:
    for b:
        y = {}
        for dgs in [ digitsGen( a ), digitsGen( b ), digitsGen( a * b ) ]:
            map( y.add, dgs )
        if len( y ) == 9:
            s.add( y )

print sum( s )

from utils import triangleGen, pentagonGen, hexagonGen, argmin
Z = T, P, H = triangleGen(), pentagonGen(), hexagonGen()
z = t, p, h = map( next, ( T, P, H ) )

while not( z[0] == z[1] == z[2] ) or z[0] in ( 1, 40755 ):
    m = argmin( *z )
    z[ m ] = next( Z[ m ] )

print z[ 0 ]


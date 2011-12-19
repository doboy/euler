from utils import digitsGen

cubes = {}
# digits -> value

i = 1
while True:
    cube = i** 3
    key =  tuple( sorted( digitsGen( i ** 3 ) ) )
    if key not in cubes:
        cubes[ key ] = []
    cubes[ key ].append( cube )
    if len( cubes[ key ] ) == 5:
        print min( cubes[ key ] )
        break
    i += 1

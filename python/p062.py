from utils import digits

cubes = {}
# digits -> value

i = 1
while True:
    cube = i** 3
    key =  tuple( sorted( digits( i ** 3 ) ) )
    if key not in cubes:
        cubes[ key ] = []
    cubes[ key ].append( cube )
    if len( cubes[ key ] ) == 5:
        break
    i += 1

print min( cubes[ key ] )

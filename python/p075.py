from utils import triplesGen

perm = {}
'''
for triple in triplesGen():
    a, b, c = triple
    print c
    if c > 1500000:
        break
    s = sum([ a, b, c ])
    if s <= 1000:
        perm[ s ] = perm.get( s, 0 ) + 1

print sum( 1 for k, v in perm.iteritems() if len( v ) == 1 )
'''

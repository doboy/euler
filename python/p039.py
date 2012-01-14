from utils import triplesGen

perm = {}

for triple in triplesGen():
    a, b, c = triple
    if c > 1000:
        break
    s = sum([ a, b, c ])
    if s <= 1000:
        perm[ s ] = perm.get( s, 0 ) + 1

print max( perm.items(), key=lambda ( k, v ) : v )[ 0 ]

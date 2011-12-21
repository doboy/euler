from math import log

def expoGen():
    for i, line in enumerate( open( "../txt/p099") ):
        base, exp = eval( line )
        yield exp * log( base ), i + 1

print max( expoGen() )[ 1 ]

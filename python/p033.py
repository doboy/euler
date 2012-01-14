from utils import product, reduceFraction, number, digits

def isCurious( n, d ):
    ans = reduceFraction( n, d )
    ndigits = digits( n )
    ddigits = digits( d )
    for i, nd in enumerate( ndigits ):
        for j, dd in enumerate( ddigits ):
            if nd == dd:
                cn = number( ndd for ii, ndd in enumerate( ndigits ) if i != ii )
                cd = number( ddd for jj, ddd in enumerate( ddigits ) if j != jj )
                if ans == reduceFraction( cn, cd ):
                    return True
    return False

def curiousGen():
    for d in xrange( 10, 100 ):
        for n in xrange( 10, d ):
            if d % 10 and isCurious( n, d ):
                yield n, d

nt, dt = 1, 1
for n, d in curiousGen():
    nn, dd = reduceFraction( n, d )
    nt, dt = nt * nn, dt * dd

print reduceFraction( nt, dt )[ 1 ]

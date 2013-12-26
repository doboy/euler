values = [ int( val ) for val in open( "txt/p059" ).read().split( "," ) ]

def language( code ):
    ''' returns a measurement of how intelligent the language is '''
    return code.count( "the" )

def decode( values, decoder ):
    ret = ""
    for i, val in enumerate( values ):
        decodee = decoder[ i % len( decoder ) ]
        ret += chr( decodee ^ val )
    return ret

a, z = ord( 'a' ), ord( 'z' )

def codeGen():
    for l1 in xrange( a, z + 1 ):
        for l2 in xrange( a, z + 1 ):
            for l3 in xrange( a, z + 1 ):
                code = decode( values, decoder=( l1, l2, l3 ) )
                yield language( code ), sum( map( ord, code ) )

print max( codeGen() )[ 1 ]

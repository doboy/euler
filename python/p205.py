from itertools import product

def make_person( dice, amount ):
    ''' pdf <==> P[ x = i ],
        cdf <==> P[ x < i ] '''
    person = { 'min' : min( dice ) * amount,
               'max' : max( dice ) * amount,
               'pdf' : {},
               'cdf' : {} }
       
    for p in product( dice, repeat=amount ):
        person[ 'pdf' ][ sum( p ) ] = person[ 'pdf' ].get( sum( p ), 0 ) + 1./\
            len( dice ) ** amount
            
    cdf = 0
    for val in xrange( min( dice ) * amount, max( dice ) * amount + 1 ):
        person[ 'cdf' ][ val ] = cdf
        cdf += person[ 'pdf' ].get( val, 0 )
    
    return person

def cdf( person, index ):
    if index < person[ 'min' ]:
        return 0
    elif index > person[ 'max' ]:
        return 1
    else:
        return person[ 'cdf' ][ index ]

def pdf( person, index ):
    return person[ 'pdf' ].get( index, 0 )

colin = make_person( xrange( 1, 6 + 1 ), 6 )
peter = make_person( xrange( 1, 4 + 1 ), 9 )

''' We want them sum of colin:P[ x = i ] and peter:P[ x > i ] for all i'''
print "%7f" % sum( pdf( colin, i ) * ( 1 - cdf( peter, i ) - pdf( peter, i ) )
           for i in xrange( colin[ 'min' ], colin[ 'max' ] + 1 ) )

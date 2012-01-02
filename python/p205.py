from itertools import product
from utils import discreteDist

class diceDist( discreteDist ):
    def setPdf( self, dice, amount ):
        for p in product( dice, repeat=amount ):
            self.pdf[ sum( p ) ] = ( self.pdf.get( sum( p ), 0 ) + 
                                     1. / len( dice ) ** amount )

colin = diceDist( dice=xrange( 1, 6 + 1 ), amount=6 )
peter = diceDist( dice=xrange( 1, 4 + 1 ), amount=9 )

''' We want them sum of colin:P[ x = i ] * peter:P[ x > i ] for all i'''
print round( sum( colin.getPdf( i ) * ( 1 - peter.getCdf( i ) )
                 for i in colin.pdf ), 7 )

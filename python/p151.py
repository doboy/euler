from utils import discreteDist
from copy import copy

def taked_out( env, sheet ):
    assert env.sheets[ sheet ]
    new_sheets = copy( env.sheets )
    new_sheets[ sheet ] -= 1
    if not new_sheets[ sheet ]:
        del new_sheets[ sheet ]
    return envelope( new_sheets )

class envelope:
    def __init__( self, sheets=None ):
        self.sheets = sheets if sheets is not None else \
            { i : 1 for i in xrange( 2, 5 + 1 ) }
        self.totalSheets = sum( v for k, v in self.sheets.items() )

    def sheetProb( self, sheet ):
        return float( self.sheets[ sheet ] ) / self.totalSheets

    def __len__( self ):
        return self.totalSheets

    def __str__( self ):
        return str( ( self.totalSheets, self.sheets ) )

class envelopeDist( discreteDist ):
    def setPdf( self ):
        def explore( currentEnv, currentProb, currentVal ):
            if len( currentEnv ) == 1:
                yield currentProb, currentVal
            for sheet in currentEnv.sheets:
                nextVal = currentVal + 1 if sheet is 5 else 0
                for res in explore( taked_out( currentEnv, sheet ), 
                         currentProb * currentEnv.sheetProb( sheet ),
                         nextVal ):
                    yield res

        for prob, val in explore( envelope(), 1, 0 ):
            print prob, val
            raw_input()
            self.pdf[ val ] = self.pdf.get( val, 0 ) + prob

e = envelopeDist()
print e.getExpectation()

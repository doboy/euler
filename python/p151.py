from utils import discreteDist

class envelope:
    def __init__( self, sheets ):
        self.sheets = sheets

def taked_out( sheet, val ):
    pass

class envelopeDist( discreteDist ):
    def setPdf( self ):
        def explore( currentEnv, currentProb, currentVal ):
            if not len( currentEnv ):
                yield currentProb, currentVal - 2
            for sheet in currentEnv.sheets:
                nextVal = currentVal + 1 if sheet is 5 else 0
                yield explore( taked_out( currentEnv, sheet ), 
                         currentProb * currentEnv.sheetProb( sheet ),
                         nextVal )

        for prob, val in explore( envelope(), 1, 0 ):
            self.pdf[ val ] = self.pdf.get( val, 0 ) + prob

e = envelopeDist()
print e.getExpectation()

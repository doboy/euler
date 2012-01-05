from utils import discreteDist
from copy import copy

# # # # # # # # # # 
# 0 #   #         #
# # # 1 #         #
# 0 #   #         #
# # # # #    3    #
#       #         #
#   2   #         #
#       #         #
# # # # # # # # # #

def taked_out( env, sheet ):
    new_env = copy( env )
    new_env[ sheet ] -= 1
    for sheet in xrange( sheet ):
        new_env[ sheet ] += 1
    return new_env

class envelope:
    def __init__( self, sheets=None ):
        self.sheets = sheets if sheets is not None else { 4 : 1 }
        self.totalSheets = sum( v for k, v in self.sheets.items() )

    def sheetProb( self, sheet ):
        return float( self[ sheet ] ) / self.totalSheets

    def __getitem__( self, sheet ):
        return self.sheets[ sheet ] if sheet in self.sheets else 0

    def __setitem__( self, sheet, val ):
        if not val:
            del self.sheets[ sheet ]
        else:
            self.sheets[ sheet ] = val
        self.totalSheets = sum( v for k, v in self.sheets.items() )

    def __len__( self ):
        return self.totalSheets

    def __copy__( self ):
        return envelope( copy( self.sheets ) )

class envelopeDist( discreteDist ):
    def setPdf( self ):
        fringe = [ ( envelope(), 1, 0 ) ]
        while fringe:
            node = env, prob, val = fringe.pop()

            if not env.sheets:
                self.pdf[ val - 2 ] = self.pdf.get( val - 2, 0 ) + prob

            else:
                for sheet in env.sheets:
                    next_val = val + ( len( env ) == 1 )
                    next_prob = prob * env.sheetProb( sheet )
                    fringe.append( 
                        ( taked_out( env, sheet ), next_prob, next_val ) )

e = envelopeDist()
print round( e.getExpectation(), 6 )

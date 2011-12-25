from utils import digitsGen, fact

lengths = {}
cycles = set()

def nextVal( n ):
    return sum( map( fact, digitsGen( n ) ) )

def length( n ):
    if n in lengths:
        return lengths[ n ]
    else:
        seenSet = { n }
        seenList = [ n ]
        next = nextVal( n )
        while next not in seenSet:
            if next in lengths:
                i = -1
                cycleLen = lengths[ next ] + 1
                while i >= -len( seenList ):
                    lengths[ seenList[ i ] ] = cycleLen
                    cycleLen += 1
                    i -= 1
                return lengths[ n ]
            else:
                seenSet.add( next )
                seenList.append( next )
                next = nextVal( next ) 
        else:
            i = -1
            cycleSet = { next }
            while seenList[ i ] != next:
                cycleSet.add( seenList[ i ] )
                i-= 1

            cycleLen = len( cycleSet ) - 1
            for cyclicNumber in cycleSet:
                lengths[ cyclicNumber ] = cycleLen

            while i >= - len( seenList ):
                cycleLen += 1
                lengths[ seenList[ i ] ] = cycleLen
                i -= 1

            return lengths[ n ]

print sum( 1 for i in xrange( 10 ** 6 ) if length( i ) == 60 )

# RELOOK 

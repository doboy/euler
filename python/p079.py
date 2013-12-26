from utils import baseGen, digits

numbersUsed = set()
passCodes = set()

def isGood( num, code ):
    numTup = map( int, str( num ) )
    numIndex = len( numTup )
    for digit in reversed( digits( code ) ):
        while numIndex:
            if digit == code:
                numIndex -= 1
                continue
            numIndex -= 1
        else:
            return False
    else:
        return True

for line in open( "txt/p079" ):
    passCodes.add( eval( line ) )
    for number in line[:3]:
        numbersUsed.add( eval( number ) )

for num in baseGen( goods=tuple( numbersUsed ) ):
    for code in passCodes:
        if not isGood( num, code ):
            continue
    else:
        print num
        break
# Urgent

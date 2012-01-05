from utils import primeGen

# numerator / divisor = remainder + dividee

def cycleLen( divisor ):
    # Values after the decimal
    decimals = []
    
    # The value under the bar
    dividianList = []
    dividianSet = set()

    dividian = 10
    while dividian not in dividianSet:
        dividianList.append( dividian )
        dividianSet.add( dividian )

        dividee = dividian // divisor
        remainder = dividian % divisor
        decimals.append( dividee )

        if not remainder:
            return 0

        dividian = remainder * 10

    i = -1
    count = 1
    while dividianList[ i ] != dividian:
        count += 1
        i -= 1
    return count

print max( ( cycleLen( i ), i ) for i in primeGen( 1000 ) )[ 1 ]

#RELOOK

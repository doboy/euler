from utils import digit

mill = [ '', 'thousand', 'million', 'billion', 'trillion' ]
decade = [ '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety' ]
unit = [ '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
         'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ]

def say( n ):
    if n == 0:
        return "zero"
    elif n < 0:
        return "negative" + say( -n )
    else:
        c = 0
        ret = ""
        while n:
            if n % 1000:
                ret = say3( n % 1000 ) + mill[ c ]
            c += 1
            n //= 1000
        return ret
            
def say3( n ):
    if n >= 100:
        return unit[ n // 100 ] + "hundred" + ( "and" if n % 100 else "" ) + say3( n % 100 )
    elif n >= 20:
        return decade[ digit( n, 1 ) ] + unit[ digit( n, 0 ) ]
    else:
        return unit[ n ]

print sum( map( len, map( say, xrange( 1, 1001 ) ) ) )

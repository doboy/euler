from math import log10

s = sum( int( num ) for num in open( "../txt/p13" ) ) 
digits = int( log10( s ) )

print s // ( 10 ** ( digits - 9 ) )

from utils import isPrime, lexiPermGen

print max( p for n in xrange( 10 )
           for p in lexiPermGen( vals=xrange( 1, n ) ) 
           if isPrime( p ) )

from utils import isTriangle, score

words = eval( open( "txt/p042" ).read() )

print sum( 1 for word in words if isTriangle( score( word ) ) )

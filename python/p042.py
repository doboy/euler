from utils import chars, points, isTriangle

words = eval( open( "../txt/p042" ).read() )

def score( wd ):
    return sum( map( points.get, wd ) )

print sum( 1 for word in words if isTriangle( score( word ) ) )

from utils import score

names = sorted( eval( open( "../txt/p022" ).read() ) )

print sum( ( i+1 ) * score( name ) for i, name in enumerate( names ) )

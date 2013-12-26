from utils import score, isSquare, number
from ast import literal_eval
"""
pairs = set()

for word in literal_eval( open( "txt/p098" ).read() ):
    num = number( map( score, word ) )
    print num, word
    if word == "CARE" or word == "RACE":
        pass
    if isSquare( number( map( score, word ) ) ):
        sorted_word = tuple( sorted( word ) )
        if sorted_word not in words:
            words[ sorted_word ] = []
        words[ sorted_word ].append( word )

print max( filter( lambda ( k, v ) : len( v ) >= 2,
                   words.iteritems() ) )[ 0 ][ 0 ]
"""

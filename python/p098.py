from utils import score, isSquare
from ast import literal_eval

words = {}

for word in literal_eval( open( "../txt/p098" ).read() ):
    if isSquare( score( word ) ):
        word_score, sorted_word = score( word ), tuple( sorted( word ) )
        if ( word_score, sorted_word ) not in words:
            words[ word_score, sorted_word ] = []
        words[ word_score, sorted_word ].append( word )

print max( filter( lambda ( k, v ) : len( v ) >= 2,
                   words.iteritems() ) )[ 0 ][ 0 ]

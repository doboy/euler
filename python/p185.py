"""
guesses = {
    '5616185650518293' : 2 ,
    '3847439647293047' : 1 ,
    '5855462940810587' : 3 ,
    '9742855507068353' : 3 ,
    '4296849643607543' : 3 ,
    '3174248439465858' : 1 ,
    '4513559094146117' : 2 ,
    '7890971548908067' : 3 ,
    '8157356344118483' : 1 ,
    '2615250744386899' : 2 ,
    '8690095851526254' : 3 ,
    '6375711915077050' : 1 ,
    '6913859173121360' : 1 ,
    '6442889055042768' : 2 ,
    '2321386104303845' : 0 ,
    '2326509471271448' : 2 ,
    '5251583379644322' : 2 ,
    '1748270476758276' : 3 ,
    '4895722652190306' : 1 ,
    '3041631117224635' : 3 ,
    '1841236454324589' : 3 ,
    '2659862637316867' : 2
}

def guess():
    def guessHelper( currentGuess, digit ):
        if ( digit == 16 ): 
            return currentGuess 
        for digitGuess in xrange( 10 ):
            digitGuess = str( digitGuess )
            correct = set()
            for guess in guesses:
                if guess[ digit ] == digitGuess and guesses[ guess ] == 0:
                    break # Roll Back
                elif guess[ digit ] == digitGuess:
                    correct.add( guess )
                    guesses[ guess ] -= 1
            else:
                guessHelper( currentGuess + digitGuess, digit + 1 )
            # Rolling Back
            for guess in correct:
                guesses[ guess ] += 1
    guessHelper( '', 0 )
guess()

"""

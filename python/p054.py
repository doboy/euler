# Tags: poker, time consuming
ranks = [ isRoyalFlush, isStraightFlush, isFourofAKind, isFullHouse,
          isFlush, isStraight, isThreeofAKind, isTwoPairs, isOnePair, 
          isHighCard ]

game = []

for line in open( "../txt/p054" ):
    line = line.split()
    hand1, hand2 = line[:5], line[5:]
    game.append( ( hand1, hand2 ) )

def rank( hand ):
    ''' 
    0 : High Card
    1 : One Pair
    2 : Two Pairs
    3 : Three of a Kind
    4 : Straight
    5 : Flush
    6 : Full House
    7 : Four of a Kind
    8 : Straight Flush
    9 : Royal Flush 

    return rank, highest rank card, highest card'''
    for rankFn in rankFns:
        if rankFn( hand ):
            return rankFn( hand )

print sum( 1 for hand1, hand2 in game if rank( hand1 ) > rank( hand2 ) )
    

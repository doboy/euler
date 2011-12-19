from utils import digitsGen, count

def powerGen():
    p = 2
    while count( digitsGen( 2 ** p ) ) <= p:
        b = 2
        while count( digitsGen( b ** p ) ) <= p:
            if count( digitsGen( b ** p ) ) == p:
                yield b ** p
            b += 1
        p += 1
        print count( digitsGen( 2 ** p ) ), p
    
# print count( powerGen() )
# bounds

def powerGen():
    p = 2
    while len( str( 2 ** p ) ) <= p:
        b = 2
        while len( str( b ** p ) ) <= p:
            if len( str( b ** p ) ) == p:
                yield b ** p
            b += 1
        p += 1
        print len( str( 2 ** p ) ), p
    
# print len( powerGen() )
# bounds

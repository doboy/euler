T = 70

f = []
for _1 in xrange( 1, 13 ):
    f.append( _1 )
    for _2 in xrange( 1, min( _1, T - _1 ) + 1 ):
        f.append( _2 )
        for _3 in xrange( 1, min( _2, T - _1 - _2 ) + 1 ):
            f.append( _3 )
            for _4 in xrange( 1, _3 + 1 ):
                f.append( _4 )
                for _5 in xrange( 1, _4 + 1 ):
                    f.append( _5 )
                    for _6 in xrange( 1, _5 + 1 ):
                        f.append( _6 )
                        for _7 in xrange( 1, _6 + 1 ):
                            f.append( _7 )
                            for _8 in xrange( 1, _7 + 1 ):
                                f.append( _8 )
                                for _9 in xrange( 1, _8 + 1 ):
                                    f.append( _9 )  
                                    for _10 in xrange( 1, _9 + 1 ):
                                        f.append( _10 )
                                        for _11 in xrange( 1, _10 + 1 ):
                                            pass

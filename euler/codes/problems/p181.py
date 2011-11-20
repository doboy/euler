hash = {}

def ways( B, W, b, w, t ):
    print B, W, b, w, t
    if ( B, W, b, w, t ) in hash:
        return hash[ B, W, b, w, t ]

    elif B == 0 and W == 0:
        return 1

    elif  B < 0 or W < 0 or ( b == 0 and w == 0 ):
        return 0

    else:
        ret = 0
        for k in xrange( 1, t ):
            for i in xrange( k ):
               ret += ways( B - i, W - k + i, i, k - i, k )
        return ret

print ways( 1, 4, 1 , 4, 6)

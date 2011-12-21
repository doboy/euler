# Tags: Dynamic Programming

ways = {}
# digit, 0, 1, A, last0? -> Ways

for z in True, False:
    for o in True, False:
        for a in True, False:
            for l in True, False:
                ways[ 0, z, o, a, l ] = 0

ways[ 0, False, False, False, False ] = 1

for d in xrange( 1, 16 + 1 ):
    for _0 in True, False:
        for _1 in True, False:
            for _A in True, False:
                # Anything But 0, 1, or A, no restriction on last
                ways[ d, _0, _1, _A, False ] = sum( ways[ d - 1, _0, _1, _A, l ] for l in [ True, False ] ) * 13

                if _0:
                    # 0 now
                    # ways[ d, _0, _1, _A, True ] = sum( ways[ d - 1, 0*, 1, a, l* ] )
                    ways[ d, _0, _1, _A, True ] = sum( ways[ d - 1, __0, _1, _A, l ] for __0 in [ True, False ] for l in [ True, False ] )
                else:
                    # not 0 now
                    # ways[ d, _0, _1, _A, True ] = 0
                    ways[ d, _0, _1, _A, True ] = 0

                if _1:
                    # 1 now
                    # ways[ d, _0, _1, _A, False ] += sum( ways[ d - 1, 0, 1*, a, l* ] )
                    ways[ d, _0, _1, _A, True ] = sum( ways[ d - 1, _0, __1, _A, l ] for __1 in [ True, False ] for l in [ True, False ] )

                if _A:
                    # A now
                    # ways[ d, _0, _1, _A, False ] += sum( ways[ d - 1, 0, 1, a*, l* ] )
                    ways[ d, _0, _1, _A, True ] = sum( ways[ d - 1, _0, _1, __A, l ] for __A in [ True, False ] for l in [ True, False ] )
                
                    
                    
                    

print "%X" % ways[ 16, True, True, True, False ]

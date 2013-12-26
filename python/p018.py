def max_tree_sum( file ):
    t = []
    for line in open( file ):
        t.append( map( int, line.split() ) )
    s = t.pop()
    while t:
        nextS = []
        for i, e in enumerate( t[-1] ):
            nextS.append( e + max( s[i], s[i+1] ) )
        s = nextS
        t.pop()
    return s[ 0 ]

if __name__ == "__main__":
    print max_tree_sum( "txt/p018" )


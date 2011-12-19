
Sum, Tree = {}, {}

def initTree( file ):
    for i, line in enumerate( file ):
        for j, item in enumerate( line ):
            Tree[ i, j ] = 

    for line in file:
        Tree.append( map( int, line.split() ) )

initTree( open( "../txt/p18" ) )

def makeNone( r, c ):
    return r, c

def datum( node ):
    return Tree[ node[0], node[1] ]

def leftBranch( node ):
    return node[ 0 ] + 1, node[ 1 ]

def rightBranch( node ):
    return node[ 0 ] + 1, node[ 1 ] + 1

def isLeaf( node ):
    node[ 0 ] == 15


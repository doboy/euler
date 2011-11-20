################################################
# Graphs
################################################
class Graph:
    def __init__( self ):
        self.edges = set()
        self.vertices = set()

    def addEdge( self, edge ):
        self.edges.add( edge )

    def addVertex( self, vertex ):
        self.vertices.add( vertex )

class Edge:
    def __init__( self, e1, e2, weight=None ):
        self.edge = e1, e2
        self.weight = weight

    def __eq__( self, other ):
        return sorted( self.edge ) == sorted( other.edge ) and \
            self.weight == other.weight

    def __cmp__( self, other ):
        return self.weight.__cmp__( other.weight )

    def __hash__( self ):
        return hash( tuple( sorted( self.edge ) ) ) + self.weight

    def __getitem__( self, index ):
        return self.edge[ index ]

    def __repr__( self ):
        return str( self.edge ) + ":" + str( self.weight ) if self.weight else ""
    
class Vertex:
    def __init__( self, v ):
        self.vertex = v

    def __eq__( self, other ):
        return self.vertex == other.vertex

    def __hash__( self ):
        return hash( self.vertex )

    def __repr__( self ):
        return str( self.vertex )

################################################
# Matrices
################################################
class Matrix:
    def __init__( self, *rows ):
        self.rows = rows

    def __getitem__( self, index ):
        return self.row[ index ]

    # Inefficient determinant
    def determinant( self, index=None, b=None ):
        if len( self ) == 1:
            return self[ 0 ][ 0 ]
        ret = 0
        for i, c in enumerate( xrange( len ( self ) ) ):
            ret += self.but( 0, c ).determinant() * ( -1 )**( i % 2 )
        return ret

    def but( self, r, c ):
        rows = []
        for ri, row in enumerate( self.rows ):
            if ri == r:
                continue
            else:
                rows.append( self.rows[:c] + self.rows[c+1:] )
        return Matrix( rows )

    def len( self ):
        return len( self.rows )

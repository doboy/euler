from utils import Graph, Edge, Vertex

def krustals( graph ):
    weightTotal = [0]
    MST = set()

    def union( edge ):
        e1, e2 = edge
        p1, p2 = find( e1 ), find( e2 )

        if rank[ p1 ] > rank[ p2 ]:
            parent[ p2 ] = p1
        else:
            parent[ p1 ] = p2
            if rank[ p1 ] == rank[ p2 ]:
                rank[ p2 ] += 1

        MST.add( edge )
        weightTotal[ 0 ] += edge.weight

    def find( vertex ):
        if vertex != parent[ vertex ]:
            parent[ vertex ] = find( parent[ vertex ] )
        return parent[ vertex ]

    rank = { vertex : 0 for vertex in graph.vertices }
    parent = { vertex : vertex for vertex in graph.vertices }

    for edge in sorted( graph.edges ):
        vStart, vEnd = edge
        if find( vStart ) != find( vEnd ):
            union( edge )

    return weightTotal[ 0 ], MST

graph = Graph()
totalWeight = 0

with open( "network.txt" ) as network:
    for i, line in enumerate( network ):
        graph.addVertex( Vertex( i ) )
        for j, weight in enumerate( line.split(',') ):
            if i > j and weight != '-':
                totalWeight += int( weight )
                graph.addEdge( Edge( Vertex( i ), Vertex( j ) , int( weight ) ) )

print totalWeight - krustals( graph )[ 0 ]

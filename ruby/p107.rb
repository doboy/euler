class Edge
  attr_accessor :vertices, :cost

  def initialize(vertex_1, vertex_2, cost)
    @vertices = [vertex_1, vertex_2]
    @cost = cost
  end
end

def find_set(parent_map, vertex)
  _vertex = vertex
  while parent_map[_vertex] != _vertex
    _vertex = parent_map[_vertex]
  end

  return _vertex
end

def union(parent_map, vertex_1, vertex_2)
  parent_map[find_set(parent_map, vertex_1)] = find_set(parent_map, vertex_2)
end

def krustal_mst(edges)
  mst_edges = []
  parent_map = Hash.new

  edges.each { |edge|
    vertex_1, vertex_2 = edge.vertices
    parent_map[vertex_1] = vertex_1
    parent_map[vertex_2] = vertex_2
  }

  edges.sort_by { |edge| edge.cost }.each { |edge|
    vertex_1, vertex_2 = edge.vertices
    if find_set(parent_map, vertex_1) != find_set(parent_map, vertex_2)
      mst_edges << edge
      union(parent_map, vertex_1, vertex_2)
    end
  }

  edges.map { |e| e.cost }.reduce(:+) - mst_edges.map { |e| e.cost }.reduce(:+)
end

def main
  edges = []
  lines = File.read("txt/p107").split("\n")
  lines.each_with_index do |line, i|
    line.split(",").each_with_index do |cost, j|
      if i > j and cost != "-"
        edges << Edge.new(i, j, cost.to_i)
      end
    end
  end

  krustal_mst edges
end

puts main

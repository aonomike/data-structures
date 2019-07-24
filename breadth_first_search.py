class Vertex:
    def __init__(self, val, visited = False, adjacent_vertices = None):
        self.val = val
        self.visited = visited
        self.adjacent_vertices = adjacent_vertices

class Edge:
    def __init__(self, start: Vertex, to: Vertex):
        self.start = start
        self.to = to
vertex_2 = Vertex(2)
vertex_0 = Vertex(0)
vertex_1 = Vertex(1)
vertex_3 = Vertex(3)
vertex_0.adjacent_vertices = []
vertices = [vertex_2, vertex_0, vertex_1, vertex_3]
edges = [Edge(vertex_2, vertex_0), Edge(vertex_0, vertex_2), Edge(vertex_2, vertex_3), Edge(vertex_3, vertex_3), Edge(vertex_0, vertex_1), Edge(vertex_1, vertex_2) ]


def bfs(edges, start_vertex):
    start_vertex.visited = True


while len(edges) > 0:



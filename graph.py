class Graph:
    def __init__(self, directed = False):
        self.graph_dict = {}
        self.directed = directed
        
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex
        
    def add_edge(self, from_vertex, to_vertex, weight = 0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def show_edges(self, vertex):
        edge_values = []
        for neighbor in vertex.edges:
            edge_values.append(self.graph_dict[neighbor].value)
        return edge_values

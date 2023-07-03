class Vertex:
    def __init__(self, value) -> None:
        """Constructor for Vertex class

        Args:
            value (any): Any object
        """        
        self.value = value
        self.edges = {}
        
    def add_edge(self, vertex, weight = 0):
        """Adds an edge between 2 vertices.

        Args:
            vertex (Vertex): Vertex to connect to
            weight (int, optional): Edge weight of the path. Defaults to 0.
        """        
        self.edges[vertex] = weight
        
    def get_edges(self):
        """Returns a list of vertices

        Returns:
            list: List of all edges of the vertex
        """        
        return list(self.edges.keys())

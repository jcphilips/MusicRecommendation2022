class Graph:
    def __init__(self, directed = False):
        """Constructor for graph class.

        Args:
            directed (bool, optional): Sets whether graph is directional. Defaults to False.
        """        
        self.graph_dict = {}
        self.directed = directed
        
    def add_vertex(self, vertex):
        """Adds a vertex to the graph.

        Args:
            vertex (Vertex): Object initialised by Vertex class
        """        
        self.graph_dict[vertex.value] = vertex
        
    def add_edge(self, from_vertex, to_vertex, weight = 0):
        """Connects two vertices of a graph to each other.

        Args:
            from_vertex (Vertex): Start vertex
            to_vertex (Vertex): Destination vertex
            weight (int, optional): For path finding. Defaults to 0.
        """        
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
        if not self.directed:
            # for undirected graph, vertices connected vertices can move back and forth
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def show_edges(self, vertex):
        """Returns a dictionary of vertices connected to a singular vertex, 
        similar to an ordered list the key is a number and the value is the vertex itself.

        Args:
            vertex (Vertex): Vertex to find edges of.

        Returns:
            edge_values (dict): Dictionary of connected vertices.
        """        
        edge_values = {}
        count = 1
        for neighbor in vertex.edges:
            edge_values[count] = self.graph_dict[neighbor].value
            count += 1
        return edge_values

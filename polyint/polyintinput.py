class polygon:
    def __init__(self, vertices): 
        # input vertices must be arranged in counterclockwise or clockwise order
        # doesn't matter which order - just stay consistent
        self.vertices = vertices
        self.vertices += self.vertices[0],

        # difference vectors between adjacent vertices
        self.vectors = []
        for x1,x2 in zip(self.vertices[:-1], self.vertices[1:]):
            v=[j-i for i,j in zip(x1,x2)]
            self.vectors += v,

        # first element is a vertex for the location of the tail end of an edge of the polygon
        # second element is a vector for the magnitude and direction of the edge of the polygon
        self.edges = [*zip(self.vertices[:-1], self.vectors)]
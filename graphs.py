import math

from data_structures import LinkedList, Queue
from sort import quicksort

class AMGraph:
    """ Graph represented using an adjacency matrix """

    def __init__(self, vertices, edges, is_directed=True):
        """ Constructor
        
            + vertices: Number of vertices
            + edges: List with pairs (x,y) representing edges, where 0 <= x,y < vertices
            + is_directed: whether the graph is directed or not
        """
        self.v = vertices
        self.graph = [([0]*vertices) for i in range(vertices)]
        self.directed = is_directed
        for edge in edges:
            self.graph[edge[0]][edge[1]] += 1
            if not is_directed:
                self.graph[edge[1]][edge[0]] += 1
    
    def __str__(self):
        s = "["
        for i in range(len(self.graph)):
            s += str(self.graph[i]) 
            if i < len(self.graph) - 1:
                s += "\n"
        s += "]"
        return s


class IMGraph:
    """ Graph represented using an incidence matrix """

    def __init__(self, vertices, edges, is_directed=True):
        """ Constructor
        
            + vertices: Number of vertices
            + edges: List with pairs (x,y) representing edges, where 0 <= x,y < vertices
            + is_directed: whether the graph is directed or not
        """
        self.v = vertices
        self.graph = [([0]*len(edges)) for i in range(vertices)]
        for i in range(len(edges)):
            if not is_directed:
                self.graph[edges[i][0]][i] += 1
                self.graph[edges[i][1]][i] += 1
            else:
                self.graph[edges[i][0]][i] += -1
                self.graph[edges[i][1]][i] += 1
    
    def __str__(self):
        s = "["
        for i in range(len(self.graph)):
            s += str(self.graph[i]) 
            if i < len(self.graph) - 1:
                s += "\n"
        s += "]"
        return s


class Graph:
    """ Graph represented using an adjacency list """

    def __init__(self, vertices, edges=None, is_directed=True):
        """ Constructor
        
            + vertices: Number of vertices
            + edges: List with pairs (x,y) representing edges, where 0 <= x,y < vertices
            + is_directed: whether the graph is directed or not
        """
        self.v = vertices
        self.graph = {node: LinkedList() for node in range(vertices)}
        self.is_directed = is_directed
        if edges:
            for edge in edges:
                w = 1
                if len(edge) > 2: # Has weight associated
                    w = edge[2]
                self.add_edge(edge[0], edge[1], w)
    
    def __str__(self):
        s = ""
        for key in self.graph:
            s += f"{key}: {self.graph[key]}\n"
        return s

    def add_edge(self, src, dest, w=1):
        """ Adds an edge from src to dest """
        self.graph[src].insert((dest, w))
        if (not self.is_directed) and src != dest:
            self.graph[dest].insert((src, w))

    def get_weight(src, dst):
        """ Returns the weight of an edge between src and dst """
        adj = self.graph[src].head
        while adj != None and adj.val[0] != dst: # Adj vertices
            adj = adj.next
        if adj:
            return adj.val[1]
        return math.inf # No edge between nodes

    def BFS(self, src):
        """ Performs Breadth First Search on self.graph from :src: node """
        # Initialization
        visited = [False]*self.v # Whether the node i has been visited or not
        d = [math.inf]*self.v # d[i] is distance from src to node i
        p = [None]*self.v # p[i] is parent of node i in the traversal
        traversal_order = [] # Final traversal order
        q = Queue(self.v)

        visited[src] = True
        d[src] = 0
        q.enqueue(src)

        while not q.is_empty():
            u = q.dequeue()
            traversal_order.append(u)
            adj = self.graph[u].head
            while adj != None: # Adj vertices
                v = adj.val[0] # Vertex
                if not visited[v]:
                    visited[v] = True
                    d[v] = d[u] + 1
                    p[v] = u
                    q.enqueue(v)
                adj = adj.next
        return traversal_order, d, p

    def DFS_Visit(self, src, time, d, f, p, visited, traversal_order, topological_sort):
        """ Helper function for DFS """
        time += 1
        d[src] = time # Discovery time
        visited[src] = True
        traversal_order.append(src)
        adj = self.graph[src].head
        while adj != None: # Adj vertices
            v = adj.val[0] # Vertex
            if not visited[v]:
                p[v] = src
                time = self.DFS_Visit(v, time, d, f, p, visited, traversal_order, topological_sort)
            # For checking cycle of bipartite graph
            # else: # was visited
            #     # To check if there is a cycle
            #     has_cycle = d[adj.val] and not f[adj.val]
            #     # To check if is bipartite
            #     if color[src] == color[adj.val]:
            #         return False # not bipartite
            adj = adj.next
        time += 1
        f[src] = time # Finalization time
        topological_sort.insert(0, src) # Topological sort

        # Tree arc (white) -  not d and not f
        # Back arc (gray): from node to ancestor -  d and not f
        # Forward arc: from node to descendant (black) -  d and f

        # For path finding using a stack, when a node != dst is finalized,
        # its popped from stack. If dst is reached, return stack

        return time

    def DFS(self, order = None):
        """ Performs Depth First Search on self.graph. Modified to return topological sort.

            If a list of the vertices is received in param :order:, that order will be used for DFS
        """
        # Initialization
        visited = [False]*self.v # Whether the node i has been visited or not
        time = 0
        d = [None]*self.v # d[i] is time of discovery of node i
        f = [None]*self.v # f[i] is time of "closing" of node i
        p = [None]*self.v # p[i] is parent of node i in the traversal
        traversal_order = [] # Final traversal order
        topological_sort = []

        if order: # Some order specified of the vertices
            vertices = order
        else: # Normal order
            vertices = range(self.v)

        for i in vertices:
            if not visited[i]:
                time = self.DFS_Visit(i, time, d, f, p, visited, traversal_order, topological_sort)

        return traversal_order, d, f, p, topological_sort

    def transpose(self):
        """ Returns the transpose graph of self.graph """
        edges = []
        for node in self.graph:
            s = self.graph[node].head # Starting node to iterate through list
            while s != None:
                edges.append((s.val[0], node))
                s = s.next
        return Graph(self.v, edges)

    def SCC(self):
        """ Calculates strongly connected components of self.graph. Returns a list of
            parents of nodes of transpose graph, which are SCC """
        dfs = self.DFS()
        T = self.transpose()
        topological_sort = dfs[4] # This is the descending order of vertices by finalization time
        T_dfs = T.DFS(topological_sort) # TODO probar porque esto me faltó ayer
        # sccs = []
        # # TODO Group sccs and return as lists
        # aux = {}
        # parents = T_dfs[3] # Parents of nodes in transpose graph
        # for node in range(self.v): # Group scc
        #     if parents[node] == None: # Is a node of a scc
        #         sccs.append([node])
        return T_dfs[3] # Parents of nodes in transpose graph, which gives sccs

    ##
    # Shortest paths
    ##
    def initialize_src_vertex(self, src):
        """ Initializes vertices  """
        d = [math.inf] * self.v # Distances from src vertex
        p = [None] * self.v # Parents
        d[src] = 0
        return d, p

    def relax(src, dst, w, d, p):
        """ Change the distance between two nodes """
        if d[dst] > d[src] + self.get_weight(src, dst):
            d[dst] = d[src] + self.get_weight(src, dst)
            p[dst] = src


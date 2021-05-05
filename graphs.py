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
                self.add_edge(edge[0], edge[1])
    
    def __str__(self):
        s = ""
        for key in self.graph:
            s += f"{key}: {self.graph[key]}\n"
        return s

    def add_edge(self, src, dest):
        """ Adds an edge from src to dest """
        self.graph[src].insert(dest)
        if (not self.is_directed) and src != dest:
            self.graph[dest].insert(src)

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
                if not visited[adj.val]:
                    visited[adj.val] = True
                    d[adj.val] = d[u] + 1
                    p[adj.val] = u
                    q.enqueue(adj.val)
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
            if not visited[adj.val]:
                p[adj.val] = src
                time = self.DFS_Visit(adj.val, time, d, f, p, visited, traversal_order, topological_sort)
            adj = adj.next
        time += 1
        f[src] = time # Finalization time
        topological_sort.insert(0, src) # Topological sort
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
                edges.append((s.val, node))
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


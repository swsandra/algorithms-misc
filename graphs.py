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

    def DFS(self):
        """ Performs Depth First Search on self.graph. Modified to return topological sort
        """
        # Initialization
        visited = [False]*self.v # Whether the node i has been visited or not
        time = 0
        d = [None]*self.v # d[i] is time of discovery of node i
        f = [None]*self.v # f[i] is time of "closing" of node i
        p = [None]*self.v # p[i] is parent of node i in the traversal
        traversal_order = [] # Final traversal order
        topological_sort = []

        for i in range(self.v):
            if not visited[i]:
                time = self.DFS_Visit(i, time, d, f, p, visited, traversal_order, topological_sort)

        return traversal_order, d, f, p, topological_sort

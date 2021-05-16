import math
from heapq import heappush, heappop

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

    def get_weight(self, src, dst):
        """ Returns the weights of all edges between src and dst """
        adj = self.graph[src].head
        weights = []
        while adj != None: # Adj vertices
            if adj.val[0] == dst:
                weights.append(adj.val[1])
            adj = adj.next
        if not weights:
            weights.append(math.inf) # No edge between node) 
        return weights

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
        """ Initializes vertices from src vertex """
        d = [math.inf] * self.v # Distances from src vertex
        p = [None] * self.v # Parents
        d[src] = 0
        return d, p

    def relax(self, src, dst, w, d, p):
        """ Updates the distance d between two nodes src and dst and parent of dst,
            if the new calculated distance is shorter """
        # weights = self.get_weight(src, dst) # There can be several edges between two same nodes
        # for w in weights:
        if d[dst] > d[src] + w:
            d[dst] = d[src] + w
            p[dst] = src
        return d, p

    def BellmanFord(self, src):
        """ Implements Bellman-Ford algorithm from src vertex. This algorithm
            computes all minimal distances from src to all vertices. Can also detect
            negative-cost cycles """
        d, p = self.initialize_src_vertex(src)
        for i in range(self.v): # V calls
            for node in self.graph: # Check all edges E
                adj = self.graph[node].head
                while adj != None: # Adj vertices
                    d, p = self.relax(node, adj.val[0], adj.val[1], d, p)
                    adj = adj.next
        # Detect negative cost cycle
        for node in self.graph:
            adj = self.graph[node].head
            while adj != None: # Adj vertices
                if d[adj.val[0]] > d[node] + adj.val[1]:
                    return False, d, p
                adj = adj.next
        return True, d, p

    def shortestPathsDAG(self, src):
        """ Computes shortests paths from src vertex on directed acyclic graphs (DAGs). Faster
            than Bellman-Ford """
        topological_sort = self.DFS()[4]
        d, p = self.initialize_src_vertex(src)
        for node in topological_sort: # V calls
            adj = self.graph[node].head
            while adj != None: # Adj vertices
                d, p = self.relax(node, adj.val[0], adj.val[1], d, p)
                adj = adj.next
        return d, p

    def Dijkstra(self, src):
        """ Computes shortest paths using Dijkstra algorithm. All weights must be non-negative """
        d, p = self.initialize_src_vertex(src)
        visited =  [False] * self.v
        # S = set()
        # Without the d array being global, the priority queue cannot be used
        # prio_q = [] # Min priority queue
        # for i in range(self.v):
        #     heappush(prio_q, (d[i], i)) # Pushing distance with associated vertex

        # while prio_q:
        for i in range(self.v):
            # min_dist, node = heappop(prio_q)
            # Get smallest node distance
            min_dist = math.inf
            for i in range(self.v):
                if d[i] < min_dist and not visited[i]:
                    min_dist = d[i]
                    node = i
            # print(min_dist, node)
            # S.add(node)
            visited[node] = True
            adj = self.graph[node].head
            while adj != None: # Adj vertices
                d, p = self.relax(node, adj.val[0], adj.val[1], d, p)
                adj = adj.next
        return d, p

    def weights_matrix(self):
        """ Returns a matrix containing the weights between all vertices """
        w = [([math.inf]*self.v) for i in range(self.v)]
        # Replace weights
        for node in range(self.v):
            w[node][node] = 0 # Main diagonal
            adj = self.graph[node].head
            while adj != None: # Adj vertices
                if node != adj.val[0]:
                    w[node][adj.val[0]] = adj.val[1]
                adj = adj.next
        return w

    def FloydWarshall(self):
        """ Computes shortest paths between all vertices of the graph using Floyd-Warshall algorithm """
        pass

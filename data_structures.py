class Stack:
    
    def __init__(self, n):
        """ Constructor, creates a stack of size n """
        self.top = -1 # Index of top element
        self.length = n
        self.array = [None] * n

    def is_empty(self):
        """ Returns whether the stack is empty or not """
        return self.top == -1

    def push(self, x):
        """ Pushes an element in the stack """
        if self.top+1 == self.length:
            raise Exception("Stack overflow")
        self.top += 1
        self.array[self.top] = x
    
    def pop(self):
        """ Pops last element from the stack """
        if self.top == -1:
            raise Exception("Stack underflow")
        self.top -= 1
        return self.array[self.top+1]

    def __str__(self):
        return str(self.array[:self.top+1])


class Queue:

    def __init__(self, n):
        """ Constructor, creates a queue of size n """
        self.head = 0
        self.tail = 0
        self.nelements = 0 # Number of elements
        self.length = n
        self.array = [None] * n

    def is_empty(self):
        """ Returns whether the queue is empty or not """
        return self.nelements == 0

    def enqueue(self, x):
        """ Enqueues element x """
        if self.nelements == self.length:
            raise Exception("Queue overflow")
        self.array[self.tail] = x
        self.tail = (self.tail+1)%self.length
        self.nelements += 1

    def dequeue(self):
        """ Dequeues an element """
        if self.is_empty():
            raise Exception("Queue underflow")
        x = self.array[self.head]
        self.head = (self.head+1)%self.length
        self.nelements -= 1
        return x

    def __str__(self):
        if self.nelements == 0:
            return str([])
        if self.head >= self.tail: # To show in correct queue order
            return str(self.array[self.head:]+self.array[:self.tail])
        return str(self.array[self.head:self.tail])


class SimpleNode:

    def __init__(self, x):
        """ Constructor, creates a new simple node with element x """
        self.val = x
        self.next = None

    def __str__(self):
        return f"Node {self.val}"


class LinkedList:
    
    def __init__(self):
        """ Constructor, creates a new empty list """
        self.head = None

    def is_empty(self):
        """ Returns whether the list is empty or not """
        return self.head == None

    def insert(self, x):
        """ Inserts an node with value x in the list """
        node = SimpleNode(x)
        node.next = self.head
        self.head = node

    def search(self, x):
        """ Finds the node with value x or None if not present """
        node = self.head
        while node != None and node.val != x:
            node = node.next
        return node

    def delete(self, node):
        """ Deletes a node from the list """
        if not node:
            return None
        if node != self.head:
            before = self.head
            while before != None and before.next != node: # Node before the one we want to delete
                before = before.next
            if before:
                before.next = node.next
        else:
            self.head = node.next
        return node

    def __str__(self):
        node = self.head
        s = "["
        while node != None:
            if node == self.head:
                s += f"{node.val}"
            else:
                s += f", {node.val}"
            node = node.next
        s += "]"
        return s


class DoublyNode:

    def __init__(self, x):
        """ Constructor, creates a new doubly node with element x """
        self.val = x
        self.prev = None
        self.next = None

    def __str__(self):
        return f"Doubly node {self.val}"


class DoublyLinkedList(LinkedList):
    
    def insert(self, x):
        """ Inserts an node with value x in the list """
        node = DoublyNode(x)
        node.next = self.head
        if self.head != None:
            self.head.prev = node
        self.head = node

    def delete(self, node):
        """ Deletes a node from the list """
        if node.prev != None:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next != None:
            node.next.prev = node.prev
        return node


class OrderedLinkedList(DoublyLinkedList):

    def insert(self, x):
        """ Inserts an node with value x in the ordered list """
        node = DoublyNode(x)
        if self.head == None:
            self.head = node
            return
        after = self.head # Node which goes after new node
        while after != None and after.next != None and after.val < x:
            after = after.next

        if after.val >= x:
            if after.prev != None:
                after.prev.next = node
                node.prev = after.prev
            else:
                self.head = node
            node.next = after
            after.prev = node
        else: # Last node and val is less than x
            after.next = node
            node.prev = after

    def print_reverse(self):
        """ Prints list in reverse """
        node = self.head
        s = "["
        while node != None and node.next != None:
            node = node.next
        while node != None:
            if node == self.head:
                s += f"{node.val}"
            else:
                s += f"{node.val}, "
            node = node.prev
        s += "]"
        print(s)


class CircularList(DoublyLinkedList):
    
    def __init__(self):
        """ Constructor, creates a new empty list """
        self.nil = DoublyNode(None) # Sentinel
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def search(self, x):
        """ Finds the node with value x or None if not present """
        node = self.nil.next
        while node != self.nil and node.val != x:
            node = node.next
        return node

    def insert(self, x):
        """ Inserts an node with value x in the list """
        node = DoublyNode(x)
        node.next = self.nil.next
        self.nil.next.prev = node
        self.nil.next = node
        node.prev = self.nil

    def delete(self, node):
        """ Deletes a node from the list """
        node.prev.next = node.next
        node.next.prev = node.prev

    def __str__(self):
        node = self.nil.next
        s = "["
        while node != self.nil:
            if node.prev == self.nil:
                s += f"{node.val}"
            else:
                s += f", {node.val}"
            node = node.next
        s += "]"
        return s

    def print_reverse(self):
        """ Prints list in reverse """
        node = self.nil.prev
        s = "["
        while node != self.nil:
            if node.prev == self.nil:
                s += f"{node.val}"
            else:
                s += f"{node.val}, "
            node = node.prev
        s += "]"
        print(s)


class Heap:
    """ Max heap data structure implementation """

    def __init__(self, arr=None):
        """ Constructor """
        self.heap = arr
        self.size = len(arr)
        for i in range(self.size//2, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, x):
        """ Restores heap property at position x
        
            O(log(n))
        """
        left = 2*x # Left tree
        right = 2*x + 1 # Right tree
        largest_index = x
        if left < self.size and self.heap[left] > self.heap[x]:
            largest_index = left
        if right < self.size and self.heap[right] > self.heap[largest_index]:
            largest_index = right
        if largest_index != x:
            self.heap[largest_index], self.heap[x] = self.heap[x], self.heap[largest_index]
            self.max_heapify(largest_index)

    def maximum(self):
        """ Returns max element """
        if self.heap:
            return self.heap[0]
        return None

    def extract_max(self):
        """ Extracts maximum element from heap """
        maximum = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        del self.heap[self.size-1]
        self.size -= 1
        self.max_heapify(0)
        return maximum

    def increase_key(self, x, key):
        """ Increases key of element at position x to value key

            Edge case with 0 and 1
        """
        self.heap[x] = key
        while x > 0 and self.heap[x//2] < self.heap[x]: # Check parent
            self.heap[x//2], self.heap[x] = self.heap[x], self.heap[x//2]
            x = x//2

    def insert(self, key):
        """ Inserts element with priority key inside heap """
        self.size += 1
        self.heap.append(-math.inf)
        self.increase_key(self.size-1, key)


class HashTable:

    def __init__(self, n):
        """ Constructor, creates a hash table of size n """
        self.n = n
        self.bucket =  [None] * n

    def h(self, key):
        """ Hash function, using mod """
        return key%self.n

    def chained_insert(self, x):
        """ Inserts element inside hash table """
        k = self.h(x)
        if not self.bucket[k]:
            self.bucket[k] = DoublyLinkedList()
        self.bucket[k].insert(x)
    
    def chained_search(self, x):
        """ Searches element inside hash table """
        k = self.h(x)
        if self.bucket[k]:
            return self.bucket[k].search(x)
        return None

    def chained_delete(self, node):
        """ Deletes element from hash table """
        k = self.h(node.val)
        if self.bucket[k]:
            self.bucket[k].delete(node)
        return node
    
    def __str__(self):
        s = ""
        for i in range(self.n):
            s += f"Bucket {i}: "
            if self.bucket[i]:
                s += f"{self.bucket[i]}"
            else:
                s += "[]"
            if i != self.n-1:
                s += "\n"
        return s


class BinaryTreeNode:

    def __init__(self, x):
        """ Constructor, creates a new tree node with value x """
        self.val = x
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"Tree node {self.val}"


class BinaryTree:

    def __init__(self):
        """ Constructor """
        self.root = None

    def search(self, node, x):
        """ Searches value x inside the tree """
        if node == None or node.val == x:
            return node
        if x < node.val:
            return self.search(node.left, x)
        return self.search(node.right, x)

    def minimum(self, node=None):
        """ Returns minimum of the tree """
        if node == None:
            node = self.root
        while node != None and node.left != None:
            node = node.left
        return node

    def maximum(self, node=None):
        """ Returns maximum of the tree """
        if node == None:
            node = self.root
        while node != None and node.right != None:
            node = node.right
        return node

    def predecessor(self, node):
        """ Returns predecessor of the node """
        if node.left != None:
            return self.maximum(node.left)
        # Left subtree not empty
        parent = node.parent
        while parent and node == parent.left: # If its the left child, parent > node
            node = parent
            parent = node.parent
        return parent

    def successor(self, node):
        """ Returns successor of the node """
        if node.right != None:
            return self.minimum(node.right)
        # Right subtree not empty
        parent = node.parent
        while parent and node == parent.right: # If its the right child, parent <= node
            node = parent
            parent = node.parent
        return parent

    def insert(self, x):
        """ Inserts a new node in the tree """
        new = BinaryTreeNode(x)
        if self.root == None:
            self.root = new
            return
        parent = None
        node = self.root
        # Search for parent node
        while node != None:
            parent = node 
            if x < node.val:
                node = node.left
            else:
                node = node.right
        # Update nodes' pointers
        new.parent = parent
        if x < parent.val:
            parent.left = new
        else:
            parent.right = new

    def transplant(self, u, v):
        """ Replaces node u with node v inside the tree """
        if u.parent == None:
            self.root = v
        elif u.parent.left == u:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def delete(self, node):
        """ Deletes a node from the tree """
        if node.left == None:
            self.transplant(node, node.right)
        elif node.right == None:
            self.transplant(node, node.left)
        else: # Node has both children
            s = self.minimum(node.right) # Successor
            if s.parent != node:
                self.transplant(s, s.right)
                s.right = node.right
                s.right.parent = s
            self.transplant(node, s)
            s.left = node.left
            s.left.parent = s
        return node

    def inorder_tree_walk(self, node, s=""):
        """ Returns a string of the inorder traversal of the tree """
        if node != None:
            s += self.inorder_tree_walk(node.left)
            s += str(node.val)
            s += self.inorder_tree_walk(node.right)
        return s + " "

    def __str__(self):
        """ Prints in order traversal """
        return self.inorder_tree_walk(self.root, "")


class TreeNode:

    def __init__(self, x):
        """ Constructor, creates a new tree node with value x """
        self.val = x
        self.parent = None
        self.left_child = None
        self.next_sibling = None

    def __str__(self):
        return f"Tree node {self.val}"


class Node:
    """ Graph Node """

    def __init__(self, x):
        """ Constructor, creates a new graoh node with value x """
        self.vertex = x
    
    def __str__(self):
        return f"Graph node {self.vertex}"


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
        return str(self.graph)
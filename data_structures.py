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

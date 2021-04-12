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
    pass

class SimpleNode:
    pass

class LinkedList:
    pass

class OrderedLinkedList:
    pass

class DoublyNode:
    pass

class DoublyLinkedList:
    pass

class CircularList:
    pass

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
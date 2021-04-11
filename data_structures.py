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
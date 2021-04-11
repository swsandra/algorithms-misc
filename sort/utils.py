import math
import random

def insertion_sort(arr):
    """ Implements in-place insertion sort

        O(n**2)
    """
    if not arr or len(arr) == 1: # Base case
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

def merge(arr, start, middle, end):
    """ Merges ordered subarrays inside an array (for mergesort)
    
        start: left subarray first element's index
        middle: left subarray last element's index
        end: right subarray last element's index
    """
    n = middle - start + 1 # First subarray size
    m = end - middle # Secund subarray size
    left = []
    right = []
    for i in range(n): # start, middle+1
        left.append(arr[start+i])
    for i in range(m): # middle+1, end+1
        right.append(arr[(middle+1)+i])
    left.append(math.inf)
    right.append(math.inf)
    i = 0 # Left subarray pointer
    j = 0 # Right subarray pointer
    for k in range(start, end+1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

def mergesort(arr, start, end):
    """ Implements in-place mergesort

        start: array first element's index
        end: array last element's index
    
        O(n*log(n))
    """
    if start < end:
        middle = (start + end)//2
        mergesort(arr, start, middle)
        mergesort(arr, middle+1, end)
        merge(arr, start, middle, end)

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

def heapsort(arr):
    """ Implements heapsort
    
        O(n*log(n))
    """
    heap = Heap(arr)
    for i in range(heap.size-1, 0, -1):
        heap.heap[0], heap.heap[heap.size-1] = heap.heap[heap.size-1], heap.heap[0]
        heap.size -= 1
        heap.max_heapify(0)
    return heap.heap # Ordered array

def partition(arr, start, end):
    """ Partitions an array between indexes start and end for quicksort """
    x = arr[end]
    i = start-1 # Pointer for minor elements
    for j in range(start, end):
        if arr[j] <= x:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[end], arr[i+1] = arr[i+1], arr[end] # Position partition number in its place
    return i+1

def quicksort(arr, start, end):
    """ Implements in-place quicksort
    
        prom O(n*log(n))
    """
    if start < end:
        partition_index = partition(arr, start, end)
        quicksort(arr, start, partition_index-1)
        quicksort(arr, partition_index+1, end)

def randomized_partition(arr, start, end):
    """ Implements a randomized index selection when partitioning for quicksort """
    i = random.randint(start, end)
    arr[i], arr[end] = arr[end], arr[i]
    return partition(arr, start, end)

def randomized_quicksort(arr, start, end):
    """ Implements randomized quicksort
    
        prom O(n*log(n))
    """
    if start < end:
        partition_index = randomized_partition(arr, start, end)
        randomized_quicksort(arr, start, partition_index-1)
        randomized_quicksort(arr, partition_index+1, end)

def bubble_sort(arr):
    """ Implements bubble sort
    
        O(n**2)
    """
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1): # Last i elements are ordered (-1 to stay in range)
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def counting_sort(arr, max_number):
    """ Implements counting sort for an array with elements between 0 and max_number
    
        O(n)
    """
    count_dict = {}
    out = arr.copy()

    for i in range(max_number+1):
        count_dict[i] = 0

    for i in range(len(arr)): # Count elements
        count_dict[arr[i]] += 1
    
    for i in range(1, max_number+1): # Count elements before i
        count_dict[i] += count_dict[i-1]

    for i in range(len(arr)-1, -1, -1):
        out[count_dict[arr[i]]-1] = arr[i] # -1 in out position bc in count_dict there is the total of numbers
        count_dict[arr[i]] -= 1

    return out

def bucket_sort(arr):
    """ Implements bucket sort
    
        O(n)
    """
    n = len(arr)
    buckets = []
    
    for i in range(n):
        buckets.append([])

    for x in arr:
        buckets[math.floor(x*n)].append(x)

    for bucket in buckets:
        insertion_sort(bucket)

    out = []
    for bucket in buckets: # Concatenate buckets
        out += bucket

    return out

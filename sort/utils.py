import math

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
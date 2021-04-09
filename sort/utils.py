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

def mergesort(arr):
    """ Implements mergesort """
    pass
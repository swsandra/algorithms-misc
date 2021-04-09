def binary_search(arr, x):
    """ Implements binary search 
    
        O(log(n))
    """
    if not arr:
        return None
    start = 0
    end = len(arr)-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid+1
        else:
            end = mid-1
    if arr[start] == x:
        return start
    return None
from search.utils import *
from sort.utils import *

def main():
    A = [3,1,7,12,67,45,8,2,10]
    print("A:", A)
    # insertion_sort(A)
    # print("Sorting A using insertion sort: ", A)
    # x = 38
    # print("Index of ", x, "in A ", A, " using binary search: ", binary_search(A, x))
    mergesort(A, 0, len(A)-1)
    print("Sorting A using mergesort: ", A)

main()
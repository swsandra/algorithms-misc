from search import *
from sort import *
from data_structures import *

def sort_tests():
    A = [3,1,7,12,67,45,8,2,10,6,3]
    print("A: ", A)
    # insertion_sort(A)
    # print("Sorting A using insertion sort: ", A)
    # x = 38
    # print("Index of ", x, "in A ", A, " using binary search: ", binary_search(A, x))
    # mergesort(A, 0, len(A)-1)
    # print("Sorting A using mergesort: ", A)
    # heap = Heap(A)
    # print("Heap from A: ", heap.heap)
    # print("Max extraction: ", heap.extract_max())
    # print("Heap now: ", heap.heap)
    # print("Sorting A using heapsort: ", heapsort(A))
    # quicksort(A, 0, len(A)-1)
    # print("Sorting A using quicksort: ", A)
    # randomized_quicksort(A, 0, len(A)-1)
    # print("Sorting A using randomized quicksort: ", A)
    # bubble_sort(A)
    # print("Sorting A using bubble sort: ", A)
    # print("Sorting A using counting sort: ", counting_sort(A, max(A)))
    print("Sorting A using bucket sort: ", bucket_sort(list(map((lambda x: x/100), A))))

def data_structures_test():
    # Stack
    # s = Stack(4)
    # s.push(2)
    # s.push(-1)
    # s.push(6)
    # s.push(21)
    # try:
    #     s.push(1)
    # except Exception as e:
    #     print(e)
    # print(s)
    # print("Popping: ", s.pop(), "from ", s)
    # print("Popping: ", s.pop(), "from ", s)
    # print("Popping: ", s.pop(), "from ", s)
    # print("Popping: ", s.pop(), "from ", s)
    # try:
    #     print("Popping: ", s.pop(), "from ", s)
    # except Exception as e:
    #     print(e)
    # print(s)

    # Queue
    # s = Queue(2)
    # s.enqueue(2)
    # print(s)
    # print("Dequeue: ", s.dequeue(), "from ", s)
    # s.enqueue(-1)
    # s.enqueue(6)
    # try:
    #     s.enqueue(21)
    # except Exception as e:
    #     print(e)
    # print(s)
    # print("Dequeue: ", s.dequeue(), "from ", s)
    # s.enqueue(1)
    # print(s)
    # print("Dequeue: ", s.dequeue(), "from ", s)
    # print("Dequeue: ", s.dequeue(), "from ", s)
    # try:
    #     print("Dequeue: ", s.dequeue(), "from ", s)
    # except Exception as e:
    #     print(e)
    # print(s)

    # Linked list
    # L = LinkedList()
    # L.insert(2)
    # L.insert(-1)
    # L.insert(6)
    # print(L)
    # print("Searching 2 in ", L, ". Found:", L.search(2))
    # print("Searching 6 in ", L, ". Found:", L.search(6))
    # print("Searching 10 in ", L, ". Found:", L.search(10))
    # print("Deleted ", L.delete(L.search(-1)), "from ", L)
    # print("Deleted ", L.delete(L.search(6)), "from ", L)
    # node = SimpleNode(2)
    # L.delete(node)
    # print("Tried deleting newly created", node, "from ", L)
    # L.delete(None)
    # print("Tried deleting empty node from", L)

    # Doubly linked list
    # L = DoublyLinkedList()
    # L.insert(2)
    # L.insert(-1)
    # L.insert(6)
    # print(L)
    # print("Searching 2 in ", L, ". Found:", L.search(2))
    # print("Searching 6 in ", L, ". Found:", L.search(6))
    # print("Searching 10 in ", L, ". Found:", L.search(10))
    # print("Deleted ", L.delete(L.search(-1)), "from ", L)
    # print("Deleted ", L.delete(L.search(6)), "from ", L)

    L = OrderedLinkedList()
    L.insert(2)
    L.insert(-1)
    L.insert(6)
    L.insert(3)
    print(L)
    L.print_reverse()
    print("Searching 2 in ", L, ". Found:", L.search(2))
    print("Searching 6 in ", L, ". Found:", L.search(6))
    print("Searching 10 in ", L, ". Found:", L.search(10))
    print("Deleted ", L.delete(L.search(-1)), "from ", L)
    L.print_reverse()
    print("Deleted ", L.delete(L.search(3)), "from ", L)
    L.print_reverse()
    print("Deleted ", L.delete(L.search(6)), "from ", L)
    L.print_reverse()

# sort_tests()
data_structures_test()
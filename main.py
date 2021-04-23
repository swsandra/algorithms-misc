from search import *
from sort import *
from data_structures import *
from graphs import *

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

    # L = OrderedLinkedList()
    # L.insert(2)
    # L.insert(-1)
    # L.insert(6)
    # L.insert(3)
    # print(L)
    # L.print_reverse()
    # print("Searching 2 in ", L, ". Found:", L.search(2))
    # print("Searching 6 in ", L, ". Found:", L.search(6))
    # print("Searching 10 in ", L, ". Found:", L.search(10))
    # print("Deleted ", L.delete(L.search(-1)), "from ", L)
    # L.print_reverse()
    # print("Deleted ", L.delete(L.search(3)), "from ", L)
    # L.print_reverse()
    # print("Deleted ", L.delete(L.search(6)), "from ", L)
    # L.print_reverse()

    # Circular linked list
    # L = CircularList()
    # L.insert(2)
    # L.insert(-1)
    # L.insert(6)
    # print(L)
    # L.print_reverse()
    # print("Searching 2 in ", L, ". Found:", L.search(2))
    # print("Searching 6 in ", L, ". Found:", L.search(6))
    # print("Searching 10 in ", L, ". Found:", L.search(10))
    # print("Deleted ", L.delete(L.search(-1)), "from ", L)
    # L.print_reverse()
    # print("Deleted ", L.delete(L.search(6)), "from ", L)
    # L.print_reverse()

    # Hash table
    # H = HashTable(2)
    # print(H)
    # H.chained_insert(2)
    # print(H)
    # H.chained_insert(-1)
    # print(H)
    # H.chained_insert(5)
    # print(H)
    # print("Searching 2 in ", H, "Found:", H.chained_search(2))
    # print("Searching 5 in ", H, "Found:", H.chained_search(5))
    # print("Searching 10 in ", H, "Found:", H.chained_search(10))
    # print("Deleted ", H.chained_delete(H.chained_search(-1)), "from ", H)
    # print("Deleted ", H.chained_delete(H.chained_search(5)), "from ", H)

    # Binary Tree
    # T = BinaryTree()
    # T.insert(12)
    # T.insert(5)
    # T.insert(18)
    # T.insert(2)
    # T.insert(9)
    # T.insert(15)
    # T.insert(20)
    # T.insert(19)
    # T.insert(17)
    # T.insert(13)
    # print(T)
    # print("Minimum of the tree", T.minimum())
    # print("Maximum of the tree", T.maximum())
    # node = T.search(T.root, 15)
    # print("Searching 15 in tree. Found:", node,
    #       "Predeccesor:", T.predecessor(node), "Successor:", T.successor(node))
    # node = T.search(T.root, 19)
    # print("Searching 19 in tree. Found:", node,
    #       "Predeccesor:", T.predecessor(node), "Successor:", T.successor(node))
    # node = T.search(T.root, 9)
    # print("Searching 9 in tree. Found:", node,
    #       "Predeccesor:", T.predecessor(node), "Successor:", T.successor(node))
    # node = T.search(T.root, 2)
    # print("Searching 2 in tree. Found:", node,
    #       "Predeccesor:", T.predecessor(node), "Successor:", T.successor(node))
    # print("Searching 10 in tree. Found:", T.search(T.root, 10))
    # print("Deleted leaf", T.delete(T.search(T.root, 19)), "from ", T)
    # print("Deleted node with only left child", T.delete(T.search(T.root, 18)), "from ", T)
    # print("Deleted leaf", T.delete(T.search(T.root, 2)), "from ", T)
    # print("Deleted node with only right child", T.delete(T.search(T.root, 5)), "from ", T)
    # print("Deleted node with both children", T.delete(T.search(T.root, 18)), "from ", T)

    # Graph represented using adjacency matrix
    V = 6
    E = [(0,0), (0,1), (0,4), (1,4), (1,2), (2,1), (3,5), (5,3), (3,2), (4,3), (4,3)]
    is_directed = False
    # G = AMGraph(V, E, is_directed)
    # G = IMGraph(V, E, is_directed)
    G = Graph(V, E, is_directed)
    # TODO test undirected graphs for previous implementations
    print(G)



# sort_tests()
data_structures_test()
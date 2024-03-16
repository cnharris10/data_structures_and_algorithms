from bfs.iterative import BFSIterative
from cache.lru_cache import LRUCache
from dfs.inorder_recursive import DFSInorderRecursive
from dfs.iterative import DFSIterative
from dfs.preorder_recursive import DFSPreorderRecursive
from dfs.postorder_recursive import DFSPostorderRecursive
from heap.heap import Heap
from search.bfs.search import BFSSearch
from search.binary_search import BinarySearch
from set.hashset import HashSet
from sorting.quicksort import QuickSort
from sorting.topological import TopologicalSort
from utils.queue import Queue
from utils.stack import Stack

classes = [
    BFSIterative,
    LRUCache,
    DFSInorderRecursive,
    DFSIterative,
    DFSPreorderRecursive,
    DFSPostorderRecursive,
    Heap,
    BFSSearch,
    BinarySearch,
    HashSet,
    QuickSort,
    TopologicalSort,
    Queue,
    Stack,
]
for cls in classes:
    print(f"***** {cls.name} Demo *****")
    cls.demo()
    print(f"**** End {cls.name} Demo *****\n")

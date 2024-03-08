from bfs.iterative import BFS
from cache.lru_cache import LRUCache
from dfs.inorder_recursive import DFSInorderRecursive
from dfs.iterative import DFS
from dfs.preorder_recursive import DFSPreorderRecursive
from dfs.postorder_recursive import DFSPostorderRecursive
from heap.heap import Heap
from search.bfs.bfs import BFSSearch
from search.binary_search import BinarySearch
from set.hashset import HashSet
from sorting.quicksort import QuickSort
from utils.queue import Queue
from utils.stack import Stack

classes = [
    BFS,
    LRUCache,
    DFSInorderRecursive,
    DFS,
    DFSPreorderRecursive,
    DFSPostorderRecursive,
    Heap,
    BFSSearch,
    BinarySearch,
    HashSet,
    QuickSort,
    Queue,
    Stack,
]
for cls in classes:
    print(f"***** {cls.name} Demo *****")
    cls.demo()
    print(f"**** End Demo *****\n")

# Data Structures & Algorithms
A collection of various data structures and algorithms built from the ground up.

Requires Python 3.10+

# Execution

## Execute a demo of all data structures and algorithms
```
python all.py
```

## Execute a single module
```
(python -m <path>.<to>.<module>)
```

**Example**
```
python -m bfs.iterative
```

## Demo Examples

### Linked lists
`LinkedList.demo()` builds `1..9`, removes three values, re-adds them at the tail, then clears:
```
$ python -m utils.graph.linked_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 5, 6, 7, 8, 9]
[2, 5, 6, 7, 8, 9, 1, 3, 4]
[]
```

`DoublyLinkedList` runs the same sequence without the final clear (it has no `clear()`):
```
$ python -m utils.graph.doubly_linked_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 5, 6, 7, 8, 9]
[2, 5, 6, 7, 8, 9, 1, 3, 4]
```

### Concurrency
Each concurrent list adds `1..100` and removes all 100 values from a thread pool, so a
correct run always ends with an empty list. The classes differ in *how* they stay correct.

`MutexLinkedList` guards every operation with a `threading.Lock` and prints after each one,
so you can watch the list grow and drain (201 lines):
```
$ python -m concurrency.mutex_linked_list
[]
[1]
[1, 2]
...
[]
```

`ConditionalLockLinkedList` uses a `threading.Condition`. Its `remove()` blocks and retries
until the value it wants has been added, which is what lets adds and removes safely share a
single pool. It prints only the final result:
```
$ python -m concurrency.conditional_lock_linked_list
[]
```

`ConditionalProducerConsumerQueue` runs 3 producers and 3 consumers against a bounded
`deque`, producing 100 items. Producers block while the queue is full, consumers block while
it is empty, and `close()` lets the consumers drain and exit:
```
$ python -m concurrency.conditional_producer_consumer_queue
[0]
[0, 1]
[0, 1, 2]
...
3 producers spawned.
3 consumers spawned.
```

## Current Classes
- Breadth-First Search (BFS)
  - `BFSIterative`
  - `BFSSearch`
- Cache
  - `LRUCache`
- Collections
  - `Queue`
  - `Stack`
  - `LinkedList`
  - `DoublyLinkedList`
- Concurrency
  - `MutexLinkedList`
  - `ConditionalLockLinkedList`
  - `ConditionalProducerConsumerQueue`
- Depth-First Search (DFS)
  - `DFSInorderRecursive`
  - `DFSIterative`
  - `DFSPreorderRecursive`
  - `DFSPostorderRecursive`
- Heap
  - `Heap`
- Search
  - `BinarySearch`
  - `BFSSearch`
- Set
  - `HashSet`
- Sorting
  - `QuickSort`
  - `TopologicalSort`

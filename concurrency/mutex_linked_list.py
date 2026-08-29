import threading
from typing import List
from utils.graph.list_node import ListNode
from utils.graph.linked_list import LinkedList
from concurrent.futures import ThreadPoolExecutor


class MutexLinkedList(LinkedList):
    name = "Concurrent Linked List with Mutex"

    @classmethod
    def demo(cls):
        linked_list = cls.build(list(range(1, 101)))
        linked_list.print()

    @classmethod
    def build(cls, node_values: List):
        linked_list = cls()
        adds = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for value in node_values:
                adds.append(executor.submit(linked_list.add, ListNode(value)))

        # Pool has shut down and joined; .result() re-raises any worker exception.
        for f in adds:
            f.result()

        removes = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            for value in node_values:
                removes.append(executor.submit(linked_list.remove, value))

        for f in removes:
            # Single-shot remove(), and the add pool has fully joined, so every
            # value is guaranteed present -- False means a real bug.
            if not f.result():
                raise RuntimeError("remove() failed for a value known to be present")
        return linked_list

    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()

    def add(self, node: ListNode) -> bool:
        with self.lock:
            self.print()
            return super().add(node)

    def remove(self, value: int) -> bool:
        with self.lock:
            self.print()
            return super().remove(value)


if __name__ == "__main__":
    MutexLinkedList.demo()

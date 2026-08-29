import threading
import time
from typing import List
from utils.graph.list_node import ListNode
from utils.graph.linked_list import LinkedList
from concurrent.futures import ThreadPoolExecutor


class ConditionalLockLinkedList(LinkedList):
    name = "Concurrent Linked List with Conditional Lock"

    @classmethod
    def demo(cls):
        linked_list = cls.build(list(range(1, 101)))
        linked_list.print()

    @classmethod
    def build(cls, node_values: List):
        linked_list = cls()
        futures, removes = [], []
        # Adds and removes share one pool. This is safe ONLY because this class's
        # remove() below blocks and retries until the value shows up.
        with ThreadPoolExecutor(max_workers=2) as executor:
            for value in node_values:
                futures.append(executor.submit(linked_list.add, ListNode(value)))
                r = executor.submit(linked_list.remove, value)
                futures.append(r)
                removes.append(r)

        # Drain after the pool joins -- draining inside the loop would serialize
        # add/remove so remove() never exercises its blocking-retry path.
        for f in futures:
            f.result()

        timed_out = [r for r in removes if r.result() is False]
        if timed_out:
            print(f"{len(timed_out)} remove() call(s) timed out after max_wait")
        return linked_list

    def __init__(self):
        super().__init__()
        self.condition = threading.Condition()

    def add(self, node: ListNode) -> bool:
        # Add node then notify threads
        with self.condition:
            val = super().add(node)
            self.condition.notify_all()
            return val

    def remove(self, value: int, max_wait: float = 10) -> bool:
        with self.condition:
            deadline = time.monotonic() + max_wait
            while True:
                # Value at head, return
                if self.head and self.head.value == value:
                    self.head = self.head.next
                    return True

                # Find node before node with value
                prev = self.head
                while prev and prev.next and prev.next.value != value:
                    prev = prev.next

                # If previous node to found value found, remove found node and return True
                if prev and prev.next and prev.next.value == value:
                    prev.next = prev.next.next
                    return True

                # If not found, timeout after `max_wait` seconds
                remaining = deadline - time.monotonic()
                if remaining <= 0 or not self.condition.wait(timeout=remaining):
                    return False

if __name__ == "__main__":
    ConditionalLockLinkedList.demo()

from typing import Optional
from utils.graph.list_node import ListNode


class LRUCache:
    name = "LRU Cache"

    @classmethod
    def demo(cls):
        cache = cls.create(3)
        cache.get(1, True)
        cache.get(2, True)
        cache.get(3, True)
        cache.get(4, True)
        cache.get(5, True)
        cache.get(2, True)
        cache.get(4, True)
        cache.get(6, True)

    @classmethod
    def create(cls, max_count: int = 3) -> "LRUCache":
        return cls(max_count)

    def __init__(self, max_count: int) -> "LRUCache":
        self._validate_params(max_count)
        self._max_count = max_count
        self._hash = {}
        self._head = None

    def get(self, value: int, summarize: bool = False) -> Optional[ListNode]:
        if value in self._hash:
            self._promote(value)
            return self._hash[value]
        else:
            self._add(value)

        if summarize:
            self.summarize()

    def summarize(self) -> None:
        hash_to_str = "{" + ", ".join([f"{k}" for k, v in self._hash.items()]) + "}"
        print("---------------------------------")
        print(f"Hash: {hash_to_str}")
        iterator, temp_list = self._head, []
        while iterator:
            temp_list.append(iterator.value)
            iterator = iterator.next
        print(f"List: {temp_list}")
        print("---------------------------------")

    def _add(self, value: int) -> None:
        self._add_value_to_head(value)
        self._remove_last_value()

    def _add_value_to_head(self, value: int) -> None:
        node = ListNode(value)
        if self._head:
            node.next = self._head
        self._head = node
        self._hash[value] = node

    def _remove_last_value(self) -> None:
        count = 0
        iterator = self._head

        #  Remove all nodes past max_count (i.e. if 3, then remove 4th+ nodes)
        while iterator:
            next_node = iterator.next
            if count >= self._max_count - 1 and next_node:
                del self._hash[next_node.value]
                iterator.next = None
            count += 1
            iterator = iterator.next

    def _promote(self, value: int) -> None:
        # Already at head, do nothing
        if self._head.value == value:
            return

        # Iterate to value
        iterator = self._head
        parent = iterator
        while iterator and iterator.value != value:
            parent = iterator
            iterator = iterator.next

        # Move value to head and set as head
        parent.next = iterator.next
        iterator.next = self._head
        self._head = iterator
        self.summarize()

    @staticmethod
    def _validate_params(max_count: int):
        if not isinstance(max_count, int) or max_count <= 0:
            raise ValueError("Must supply a positive integer 'max_count' value")


if __name__ == "__main__":
    LRUCache.demo()

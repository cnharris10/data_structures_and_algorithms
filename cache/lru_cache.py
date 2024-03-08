from typing import Optional

from utils.list.list_node import ListNode


class LRUCache:
    @classmethod
    def create(cls, max_count: int = 3) -> "LRUCache":
        return cls(max_count)

    def __init__(self, max_count: int) -> "LRUCache":
        self._validate_params(max_count)
        self._max_count = max_count
        self._hash = {}
        self._head = None

    def get(self, value: int, summarize: bool = False) -> None:
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
        while iterator:
            next_node = iterator.next
            if count >= self._max_count - 1 and next_node:
                del self._hash[next_node.value]
                iterator.next = None
            count += 1
            iterator = iterator.next

    def _promote(self, value: int) -> None:
        iterator = self._head
        parent = iterator
        while iterator and iterator.value != value:
            parent = iterator
            iterator = iterator.next

        parent.next = iterator.next if iterator.next else None
        iterator.next = self._head
        self._head = iterator
        self.summarize()

    @staticmethod
    def _validate_params(max_count: int):
        try:
            isinstance(max_count, int)
            if int(max_count) <= 0:
                raise
        except ValueError:
            raise ValueError("Must supply a positive integer 'max_count' value")


if __name__ == "__main__":
    cache = LRUCache.create(3)
    cache.get(1, True)
    cache.get(2, True)
    cache.get(3, True)
    cache.get(4, True)
    cache.get(5, True)
    cache.get(2, True)
    cache.get(4, True)
    cache.get(6, True)

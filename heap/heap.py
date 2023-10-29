import math
from random import seed, randint
from typing import List


class Heap:
    values: List[int] = []

    def __init__(self, print_after_operation: bool = True):
        self.print_after_operation = print_after_operation

    def insert(self, value: int) -> None:
        if not self.values:
            self.values = [value]
            return

        self.values.append(value)
        self._heapify(len(self.values) - 1)
        if self.print_after_operation:
            self._print_heap()

    def remove(self, value: int) -> None:
        if value in self.values:
            idx = self.values.index(value)
        else:
            raise ValueError(f"Value: {value} does not exist")

        # Swap index of found value and last node
        self._swap(idx, len(self.values) - 1)

        # Delete last node
        del self.values[-1]

        # Heapify all node elements
        for i in range(len(self.values)):
            self._heapify(i)

        if self.print_after_operation:
            self._print_heap()

    def size(self):
        return len(self.values)

    def value_at(self, idx: int):
        return self.values[idx]

    def _heapify(self, pos: int) -> None:
        values_length = len(self.values)
        parent_pos = self._get_parent_pos(pos)
        while parent_pos >= 0:
            left_pos = self._left_pos(parent_pos)
            right_pos = self._right_pos(parent_pos)
            left = self.values[left_pos] if left_pos < values_length else -math.inf
            right = self.values[right_pos] if right_pos < values_length else -math.inf

            if left > right and left > self.values[parent_pos]:
                self._swap(parent_pos, left_pos)

            if right > left and right > self.values[parent_pos]:
                self._swap(parent_pos, right_pos)

            parent_pos = self._get_parent_pos(parent_pos)

    def _swap(self, parent_pos: int, child_pos: int) -> None:
        self.values[parent_pos], self.values[child_pos] = (
            self.values[child_pos],
            self.values[parent_pos],
        )

    def _print_heap(self) -> None:
        print(self.values)

    @staticmethod
    def _get_parent_pos(pos: int) -> int:
        return (pos // 2 - 1) if pos % 2 == 0 else (pos // 2)

    @staticmethod
    def _left_pos(pos: int) -> int:
        return pos * 2 + 1

    @staticmethod
    def _right_pos(pos: int) -> int:
        return pos * 2 + 2


if __name__ == "__main__":
    size = 20
    heap = Heap()
    for i in range(size):
        heap.insert(randint(0, size * 10))

    while heap.values:
        heap.remove(heap.value_at(randint(0, heap.size() - 1)))

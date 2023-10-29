from typing import Any, List, Optional


class Queue:
    list: List[Any] = []

    def __init__(self, _max_size: int):
        if int(_max_size) <= 0:
            raise ValueError("Must enter a max size greater than 0.")
        self.max_size = _max_size

    def enqueue(self, element: Any) -> bool:
        if self.size() >= self.max_size:
            return False

        self.list.append(element)
        return True

    def dequeue(self) -> Optional[Any]:
        if self.size() == 0:
            return

        element = self.list[0]
        del self.list[0]
        return element

    def size(self) -> int:
        return len(self.list)

    def empty(self) -> int:
        return self.size() == 0

    def print(self) -> None:
        print(self.list)


if __name__ == "__main__":
    max_size = 5
    queue = Queue(max_size)
    for i in range(max_size + 1):
        queue.enqueue(i)
        queue.print()
    queue.print()
    for i in range(max_size + 1):
        print(queue.dequeue())
    queue.print()

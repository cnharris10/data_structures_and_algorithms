from typing import Any, List, Optional


class Stack:
    name = "Stack"
    list: List[Any] = []

    @classmethod
    def demo(cls):
        max_size = 5
        stack = cls(max_size)
        for i in range(max_size + 1):
            stack.push(i)
            stack.print()
        stack.print()
        for i in range(max_size + 1):
            print(stack.pop())
        stack.print()

    def __init__(self, _max_size: int):
        if int(_max_size) <= 0:
            raise ValueError("Must enter a max size greater than 0.")
        self.max_size = _max_size

    def push(self, element: Any) -> bool:
        if self.size() >= self.max_size:
            return False

        self.list.insert(0, element)
        return True

    def pop(self) -> Optional[Any]:
        if self.empty():
            return

        element = self.list[0]
        del self.list[0]
        return element

    def size(self) -> int:
        return len(self.list)

    def empty(self) -> bool:
        return self.size() == 0

    def print(self) -> None:
        print(self.list)


if __name__ == "__main__":
    Stack.demo()

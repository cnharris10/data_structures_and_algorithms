from typing import Optional


class ListNode:

    def __init__(self, value: int):
        self.value = value
        self.prev: Optional["ListNode"] = None
        self.next: Optional["ListNode"] = None

    def print(self):
        print(f"Value: {self.value}, Prev: {self.prev}, Next: {self.next}")

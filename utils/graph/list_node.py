from typing import Optional, List


class ListNode:
    prev: Optional["ListNode"] = None
    next: Optional["ListNode"] = None

    def __init__(self, value: int):
        self.value = value

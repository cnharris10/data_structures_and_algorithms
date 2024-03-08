from typing import Optional


class ListNode(object):
    next: Optional["ListNode"] = None

    def __init__(self, value: int):
        self.value = value

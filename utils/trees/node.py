from typing import Optional


class Node(object):
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __init__(self, value: int):
        self.value = value

from typing import Optional


class TreeNode:
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    def __init__(self, value: int):
        self.value = value

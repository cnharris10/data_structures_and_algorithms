from copy import deepcopy
from typing import List, Tuple

from search.bfs.utils.position import Position


class TreeNode:
    @classmethod
    def clone(cls, position: Position, path: List[Tuple[int, int]]) -> "TreeNode":
        return deepcopy(cls(position, path))

    def __init__(self, position, path=None):
        if path is None:
            path = []
        self.position = position
        self.path = path
        self._path_set = set(self.path)

    def add_to_path(self, position):
        self.path.append((position.x, position.y))

    def __str__(self):
        return f"position: {self.position}, path: {self.path}"

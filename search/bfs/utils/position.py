from random import shuffle
from typing import List


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def surrounding_positions(self) -> List["Position"]:
        position_list = [
            Position(self.x - 1, self.y),
            Position(self.x, self.y - 1),
            Position(self.x, self.y + 1),
            Position(self.x + 1, self.y),
        ]
        shuffle(position_list)
        return position_list

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"x={self.x}, y={self.y}"

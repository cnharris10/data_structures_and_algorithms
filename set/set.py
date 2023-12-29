from typing import Optional

from search.binary_search import BinarySearch


class Set:
    list = []

    @classmethod
    def create(cls):
        return cls()

    def add(self, value: int):
        pos = self.contains(value)
        if pos is None:
            self.list.append(value)
            return True

        return False

    def remove(self, value: int) -> bool:
        pos = self.contains(value)
        if pos is None:
            return False

        del self.list[pos]
        return True

    def contains(self, value: int) -> Optional[int]:
        pos = BinarySearch.algorithm(self.list, 0, len(self.list) - 1, value)
        if pos is None:
            return None

        return pos

    def __str__(self):
        joined_list = ",".join([str(i) for i in self.list])
        return f"Set contains: [{joined_list}]"


if __name__ == "__main__":
    size = 20
    set = Set.create()
    set.add(1)
    set.add(1)
    print(set)
    set.remove(1)
    set.add(3)
    set.add(4)
    set.remove(1)
    set.remove(2)
    print(set)

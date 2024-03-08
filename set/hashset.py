from typing import Optional


class HashSet:
    @classmethod
    def create(cls, values: list = None) -> "HashSet":
        if values is None:
            values = []
        _set = cls()
        for value in values:
            _set.add(value)
        return _set

    def __init__(self):
        self._hash = {}

    def add(self, value: int) -> None:
        self._hash[value] = True

    def remove(self, value: int) -> Optional[int]:
        if self.contains(value):
            del self._hash[value]
            return value

    def contains(self, value: int) -> bool:
        return value in self._hash

    def size(self) -> int:
        return len(self._hash)

    def isEmpty(self) -> int:
        return self.size() == 0

    def values(self) -> list:
        return list(self._hash.keys())

    def union(self, other: "HashSet") -> "HashSet":
        _set = HashSet.create()
        for value in self.values() + other.values():
            _set.add(value)
        return _set

    def intersect(self, other: "HashSet") -> "HashSet":
        hsh = self._tally(other)
        _set = HashSet.create()
        for key, val in hsh.items():
            if val > 1:
                _set.add(key)
        return _set

    def difference(self, other: "HashSet") -> "HashSet":
        hsh = self._tally(other)
        _set = HashSet.create()
        for key, val in hsh.items():
            if val == 1:
                _set.add(key)
        return _set

    def _tally(self, other: "HashSet") -> dict:
        hsh = {}
        for value in self.values() + other.values():
            if value in hsh:
                hsh[value] += 1
            else:
                hsh[value] = 1
        return hsh

    def __eq__(self, other: "HashSet") -> bool:
        return len(self._hash) == len(other._hash) and self._hash == other._hash

    def __str__(self) -> str:
        joined_list = ",".join([str(i) for i in self.values()])
        return f"[{joined_list}]"


if __name__ == "__main__":
    myset = HashSet.create([1, 1])
    print(f"Initial Set: {myset}")
    myset.add(3)
    print(f"Add 3: {myset}")
    myset.add(4)
    print(f"Add 4: {myset}")
    print(f"Remove 1: {myset}")
    myset.remove(1)
    myset.remove(1)
    myset.remove(2)
    print(f"Equality: {HashSet.create([1]) == HashSet.create([1])}")
    print(f"Union: {myset.union(HashSet.create([4, 5]))}")
    print(f"Intersection: {myset.intersect(HashSet.create([4, 5]))}")
    print(f"Difference: {myset.difference(HashSet.create([4, 5]))}")

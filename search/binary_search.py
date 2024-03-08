from typing import Optional


class BinarySearch(object):
    name = "Binary Search"

    @classmethod
    def demo(cls):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        cls.algorithm(l, 0, 8, 2)
        cls.algorithm(l, 0, 8, 1)
        cls.algorithm(l, 0, 8, 9)
        cls.algorithm(l, 0, 8, 19)

    @staticmethod
    def algorithm(
        l: list, start: int, end: int, value: int, last_pos=None
    ) -> Optional[int]:
        print(f"Searching for: {value}")
        if not l:
            print("Result: Not in list")
            return

        pos = round((start + end) / 2)
        current = l[pos]
        if pos == last_pos:
            print("Result: Not in list")
            return

        if value == current:
            print(f"Found: {current}")
            return pos
        if current < value:
            print(f"Narrowing to greater window")
            return BinarySearch.algorithm(l, pos + 1, end, value, pos)
        else:
            print(f"Narrowing to lesser window")
            return BinarySearch.algorithm(l, start, pos - 1, value, pos)


if __name__ == "__main__":
    BinarySearch.demo()

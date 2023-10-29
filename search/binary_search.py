class BinarySearch(object):
    def run(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.algorithm(l, 0, 8, 2)
        self.algorithm(l, 0, 8, 1)
        self.algorithm(l, 0, 8, 9)
        self.algorithm(l, 0, 8, 19)

    def algorithm(self, l, start, end, value, last_pos=None):
        print(f"Searching for: {value}")
        pos = round((start + end) / 2)
        current = l[pos]
        if pos == last_pos:
            print("Result: Not in list")
            return

        if value == current:
            print(f"Found: {current}")
            return current
        if current < value:
            print(f"Narrowing to greater window")
            return self.algorithm(l, pos + 1, end, value, pos)
        else:
            print(f"Narrowing to lesser window")
            return self.algorithm(l, start, pos - 1, value, pos)


if __name__ == "__main__":
    BinarySearch().run()

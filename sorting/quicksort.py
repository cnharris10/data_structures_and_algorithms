class QuickSort:
    name = "QuickSort"

    @classmethod
    def demo(cls):
        num_list = [4, 7, 5, 2, 3, 8, 9, 1, 9, 6, 8]
        print(f"Original List: {num_list}")
        instance = cls()
        instance.algorithm(num_list, 0, len(num_list) - 1)
        print(f"Sorted List: {num_list}")

    def algorithm(self, l, start, end):
        if start >= end:
            return

        pivot = self.partition(l, start, end)
        self.algorithm(l, start, pivot - 1)
        self.algorithm(l, pivot + 1, end)

    @staticmethod
    def partition(l, start, end):
        pivot = l[start]
        i = start + 1
        j = end
        while True:
            while i <= j and l[i] <= pivot:
                i += 1

            while i <= j and l[j] >= pivot:
                j -= 1

            if i >= j:
                break

            l[i], l[j] = l[j], l[i]

        l[start], l[j] = l[j], l[start]
        return j


if __name__ == "__main__":
    QuickSort.demo()

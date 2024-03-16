from functools import cached_property
from typing import List


class TopologicalSort:
    name = "Topological Sort"

    @classmethod
    def demo(cls) -> None:
        print("Topological Sort")
        print(TopologicalSort({1: [2, 7], 2: [3, 8, 9], 4: [5], 5: [6], 9: [10]}).run())

        print("Topological Sort (with cycle)")
        print(
            TopologicalSort(
                {1: [2, 7], 2: [3, 8, 9], 3: [1], 4: [5], 5: [6], 9: [10]}
            ).run()
        )

    def __init__(self, edges: dict[int, List[int]]) -> "TopologicalSort":
        self.output: List[int] = []
        self.edges: dict[int, List[int]] = edges

    def run(self) -> List[int]:
        count = 0
        while self.edges:
            if count > self.total_size:
                print("Cycle detected! Returning None.")
                self.output = []
                break

            nodes = self._find_zero_degree_nodes()
            self.output += nodes
            self._adjust(nodes)
            count += 1
        return self.output

    def _find_zero_degree_nodes(self) -> set[int]:
        concat_values = []
        for val in self.edges.values():
            concat_values += val
        return set(self.edges.keys()).difference(set(concat_values))

    @cached_property
    def total_size(self) -> int:
        count = len(self.edges.keys())
        for vals in self.edges.values():
            count += len(vals)
        return count

    def _adjust(self, nodes: List[int]) -> None:
        for key in nodes:
            values = self.edges[key]
            for val in values:
                if val not in self.edges:
                    self.edges[val] = []
            del self.edges[key]


if __name__ == "__main__":
    TopologicalSort.demo()

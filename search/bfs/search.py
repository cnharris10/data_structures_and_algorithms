from threading import Thread, active_count, Lock
from typing import List

from search.bfs.utils.node import TreeNode
from search.bfs.utils.matrix import Matrix
from search.bfs.utils.position import Position
from utils.queue import Queue


class BFSSearch:
    name = "Breadth-First Search"

    @classmethod
    def demo(cls):
        cls.run(
            rows=20,
            columns=20,
            start=Position(4, 4),
            target=Position(18, 19),
            barriers={
                (1, 1),
                (2, 2),
            },
            strategy=False,
            concurrent=True,
            max_threads=20,
        )

    @classmethod
    def run(
        cls,
        rows: int,
        columns: int,
        start: Position,
        target: Position,
        barriers: set = None,
        strategy: bool = True,
        concurrent: bool = True,
        max_threads: int = 10,
    ):
        if barriers is None:
            barriers = {}
        matrix = Matrix.build(rows=rows, columns=columns, barriers=barriers)
        instance = BFSSearch(
            matrix=matrix,
            start=start,
            target=target,
            strategy=strategy,
            concurrent=concurrent,
            max_threads=max_threads,
        )
        instance.algorithm()

    def __init__(
        self, matrix: Matrix, start, target, strategy, concurrent, max_threads
    ):
        self.queue = Queue(9999999)
        self.matrix: Matrix = matrix
        self.start: Position = start
        self.target: Position = target
        self.strategy: bool = strategy
        self.max_threads = max_threads
        self.lock = Lock()
        self.found = False
        self.concurrent = concurrent

    def algorithm(self):
        print(
            f"Find path to target: {self.target} in a {self.matrix.rows}x{self.matrix.columns} matrix with barriers: {self.matrix.barriers}"
        )
        self.queue.enqueue(TreeNode(self.start))
        while self.queue and not self.found:
            if not self.concurrent:
                self.evaluate()
            elif active_count() > self.max_threads:
                continue
            else:
                Evaluator(self).start()

    def evaluate(self):
        current_node = self.queue.dequeue()
        current_position = current_node.position
        if current_position == self.target:
            self.found = True
            current_position = current_node.position
            print(
                f"Found target: ({current_position.x}, {current_position.y}) with: \n"
                f"  - Distance: {len(current_node.path)}\n"
                f"  - Barriers: {self.matrix.barriers}\n"
                f"  - Remaining Queue Nodes: {self.queue.size()}\n"
                f"  - Path: {current_node.path}\n"
            )
            return

        with self.lock:
            if self.matrix.position_was_visited(current_position):
                return

        self.matrix.mark_position_visited(current_position)
        self.add_to_node_path_and_queue(current_node)

    def add_to_node_path_and_queue(self, current_node: TreeNode):
        candidates = []
        for possible_position in current_node.position.surrounding_positions():
            copied_node = TreeNode.clone(possible_position, current_node.path)
            position = copied_node.position
            if not self.matrix.within_bounds(copied_node) or self.matrix.is_barrier(
                position
            ):
                continue
            with self.lock:
                if not self.matrix.position_was_visited(position):
                    candidates.append(copied_node)

        for node in (
            [self.pick_best_euclidian_distance(candidates, self.target)]
            if self.strategy
            else candidates
        ):
            node.add_to_path(node.position)
            with self.lock:
                self.queue.enqueue(node)

    @staticmethod
    def pick_best_euclidian_distance(
        candidates: List[TreeNode], target: Position
    ) -> (TreeNode, int):
        scores = [
            (
                candidate,
                (
                    (target.x - candidate.position.x) ** 2
                    + (target.y - candidate.position.y) ** 2
                ),
            )
            for candidate in candidates
        ]
        return min(scores, key=lambda x: x[1])[0]


class Evaluator(Thread):
    def __init__(self, caller):
        super().__init__()
        self.caller = caller

    def run(self):
        self.caller.evaluate()


if __name__ == "__main__":
    BFSSearch.demo()

from utils.queue import Queue
from utils.trees.balanced_tree import BalancedTree
from utils.trees.node import Node
from utils.trees.unbalanced_tree import UnbalancedTree


class BFS(object):
    def run(self):
        print("Running with a balanced tree")
        self.algorithm(BalancedTree.build())
        print("Running with an unbalanced tree")
        self.algorithm(UnbalancedTree.build())

    def __init__(self):
        self.queue = Queue(99999)

    def algorithm(self, node: Node):
        self.queue.enqueue(node)
        while not self.queue.empty():
            item = self.queue.dequeue()
            if item:
                if item.left:
                    self.queue.enqueue(item.left)
                if item.right:
                    self.queue.enqueue(item.right)
                print(item.value)


if __name__ == "__main__":
    BFS().run()

from utils.queue import Queue
from utils.trees.balanced_tree import BalancedTree
from utils.trees.tree_node import TreeNode
from utils.trees.unbalanced_tree import UnbalancedTree


class BFSIterative:
    name = "Iterative Breadth-First Search"

    @classmethod
    def demo(cls):
        print("Running with a balanced tree")
        cls().algorithm(BalancedTree.build())
        print("Running with an unbalanced tree")
        cls().algorithm(UnbalancedTree.build())

    def __init__(self):
        self.queue = Queue(99999)

    def algorithm(self, node: TreeNode):
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
    BFSIterative().demo()

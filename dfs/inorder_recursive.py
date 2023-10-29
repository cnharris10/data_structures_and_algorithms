from utils.trees.balanced_tree import BalancedTree
from utils.trees.node import Node
from utils.trees.unbalanced_tree import UnbalancedTree


class DFSInorderRecursive(object):
    def algorithm(self, node: Node):
        if not node:
            return

        if node.left:
            self.algorithm(node.left)
        print(node.value)
        if node.right:
            self.algorithm(node.right)


if __name__ == "__main__":
    instance = DFSInorderRecursive()
    print("Running with a balanced tree")
    instance.algorithm(BalancedTree.build())
    print("Running with an unbalanced tree")
    instance.algorithm(UnbalancedTree.build())

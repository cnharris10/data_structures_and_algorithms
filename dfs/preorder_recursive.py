from utils.trees.balanced_tree import BalancedTree
from utils.trees.node import Node
from utils.trees.unbalanced_tree import UnbalancedTree


class DFSPreorderRecursive(object):
    def algorithm(self, node: Node):
        if not node:
            return

        print(node.value)
        if node.left:
            self.algorithm(node.left)

        if node.right:
            self.algorithm(node.right)


if __name__ == "__main__":
    instance = DFSPreorderRecursive()
    print("Running with a balanced tree")
    instance.algorithm(BalancedTree.build())
    print("Running with an unbalanced tree")
    instance.algorithm(UnbalancedTree.build())

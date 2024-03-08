from utils.trees.balanced_tree import BalancedTree
from utils.trees.tree_node import TreeNode
from utils.trees.unbalanced_tree import UnbalancedTree


class DFSPreorderRecursive(object):
    name = "Depth-First Search - Recursive Preorder"

    @classmethod
    def demo(cls):
        instance = cls()
        print("Running with a balanced tree")
        instance.algorithm(BalancedTree.build())
        print("Running with an unbalanced tree")
        instance.algorithm(UnbalancedTree.build())

    def algorithm(self, node: TreeNode):
        if not node:
            return

        print(node.value)
        if node.left:
            self.algorithm(node.left)

        if node.right:
            self.algorithm(node.right)


if __name__ == "__main__":
    DFSPreorderRecursive.demo()

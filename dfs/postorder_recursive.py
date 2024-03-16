from utils.trees.balanced_tree import BalancedTree
from utils.trees.tree_node import TreeNode
from utils.trees.unbalanced_tree import UnbalancedTree


class DFSPostorderRecursive:
    name = "Depth-First Search - Recursive Postorder"

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

        if node.left:
            self.algorithm(node.left)
        if node.right:
            self.algorithm(node.right)
        print(node.value)


if __name__ == "__main__":
    DFSPostorderRecursive.demo()

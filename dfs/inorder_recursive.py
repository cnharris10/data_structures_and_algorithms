from utils.trees.balanced_tree import BalancedTree
from utils.trees.tree_node import TreeNode
from utils.trees.unbalanced_tree import UnbalancedTree


class DFSInorderRecursive:
    name = "Depth-First Search - Recursive Inorder"

    @classmethod
    def demo(cls):
        instance = DFSInorderRecursive()
        print("Running with a balanced tree")
        instance.algorithm(BalancedTree.build())
        print("Running with an unbalanced tree")
        instance.algorithm(UnbalancedTree.build())

    @classmethod
    def algorithm(cls, node: TreeNode):
        if not node:
            return

        if node.left:
            cls().algorithm(node.left)
        print(node.value)
        if node.right:
            cls().algorithm(node.right)


if __name__ == "__main__":
    DFSInorderRecursive.demo()

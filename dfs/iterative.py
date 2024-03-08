from utils.stack import Stack
from utils.trees.balanced_tree import BalancedTree
from utils.trees.tree_node import TreeNode
from utils.trees.unbalanced_tree import UnbalancedTree


class DFS(object):
    def __init__(self, _max_size=100):
        self.stack = Stack(_max_size)

    def algorithm(self, node: TreeNode):
        self.stack.push(node)
        while not self.stack.empty():
            item = self.stack.pop()
            if item:
                print(item.value)
                if item.right:
                    self.stack.push(item.right)
                if item.left:
                    self.stack.push(item.left)


if __name__ == "__main__":
    instance = DFS()
    print("Running with a balanced tree")
    instance.algorithm(BalancedTree.build())
    print("Running with an unbalanced tree")
    instance.algorithm(UnbalancedTree.build())

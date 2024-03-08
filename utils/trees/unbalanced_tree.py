from utils.trees.tree_node import TreeNode


class UnbalancedTree(object):
    @staticmethod
    def build():
        root_node = TreeNode(1)

        level_2_nodes = [TreeNode(2), TreeNode(3)]
        root_node.left = level_2_nodes[0]
        root_node.right = level_2_nodes[1]

        level_3_nodes = [TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)]
        level_2_nodes[0].left = level_3_nodes[0]
        level_2_nodes[0].right = level_3_nodes[1]
        level_2_nodes[1].left = level_3_nodes[2]
        level_2_nodes[1].right = level_3_nodes[3]

        level_4_nodes = [TreeNode(8), TreeNode(9), TreeNode(10), TreeNode(11)]
        level_3_nodes[0].left = level_4_nodes[0]
        level_3_nodes[0].right = level_4_nodes[1]
        level_3_nodes[1].left = level_4_nodes[2]
        level_3_nodes[1].right = level_4_nodes[3]

        level_5_nodes = [TreeNode(12), TreeNode(13)]
        level_4_nodes[0].left = level_5_nodes[0]
        level_4_nodes[0].right = level_5_nodes[1]

        level_6_nodes = [TreeNode(14), TreeNode(15)]
        level_5_nodes[0].left = level_6_nodes[0]
        level_5_nodes[0].right = level_6_nodes[1]

        return root_node

from utils.trees.node import Node


class UnbalancedTree(object):
    @staticmethod
    def build():
        root_node = Node(1)

        level_2_nodes = [Node(2), Node(3)]
        root_node.left = level_2_nodes[0]
        root_node.right = level_2_nodes[1]

        level_3_nodes = [Node(4), Node(5), Node(6), Node(7)]
        level_2_nodes[0].left = level_3_nodes[0]
        level_2_nodes[0].right = level_3_nodes[1]
        level_2_nodes[1].left = level_3_nodes[2]
        level_2_nodes[1].right = level_3_nodes[3]

        level_4_nodes = [Node(8), Node(9), Node(10), Node(11)]
        level_3_nodes[0].left = level_4_nodes[0]
        level_3_nodes[0].right = level_4_nodes[1]
        level_3_nodes[1].left = level_4_nodes[2]
        level_3_nodes[1].right = level_4_nodes[3]

        level_5_nodes = [Node(12), Node(13)]
        level_4_nodes[0].left = level_5_nodes[0]
        level_4_nodes[0].right = level_5_nodes[1]

        level_6_nodes = [Node(14), Node(15)]
        level_5_nodes[0].left = level_6_nodes[0]
        level_5_nodes[0].right = level_6_nodes[1]

        return root_node

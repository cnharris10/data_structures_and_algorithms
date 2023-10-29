from utils.trees.node import Node


class BalancedTree(object):
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

        level_4_nodes = [
            Node(8),
            Node(9),
            Node(10),
            Node(11),
            Node(12),
            Node(13),
            Node(14),
            Node(15),
        ]
        level_3_nodes[0].left = level_4_nodes[0]
        level_3_nodes[0].right = level_4_nodes[1]
        level_3_nodes[1].left = level_4_nodes[2]
        level_3_nodes[1].right = level_4_nodes[3]
        level_3_nodes[2].left = level_4_nodes[4]
        level_3_nodes[2].right = level_4_nodes[5]
        level_3_nodes[3].left = level_4_nodes[6]
        level_3_nodes[3].right = level_4_nodes[7]

        return root_node

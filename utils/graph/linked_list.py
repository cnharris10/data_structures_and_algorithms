from typing import List
from utils.graph.list_node import ListNode


class LinkedList:
    name = "Linked List"

    @classmethod
    def demo(cls):
        full_list = [1,2,3,4,5,6,7,8,9]
        linked_list = cls.build(full_list)
        linked_list.print()
        linked_list.remove(1)
        linked_list.remove(3)
        linked_list.remove(4)
        linked_list.print()
        linked_list.add(ListNode(1))
        linked_list.add(ListNode(3))
        linked_list.add(ListNode(4))
        linked_list.print()
        linked_list.clear()
        linked_list.add(ListNode(1))
        linked_list.remove(1)
        linked_list.print()

    def __init__(self):
        self.head = None

    @classmethod
    def build(cls, node_values: List):
        linked_list = cls()
        for value in node_values:
            linked_list.add(ListNode(value))
        return linked_list

    def add(self, node: ListNode) -> bool:
        # Empty List
        if not self.head:
            node.next = None
            self.head = node
            return True

        # Go to end of list
        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        # Add to end of list
        ptr.next = node
        node.next = None
        return True

    def remove(self, value: int) -> bool:
        # Empty List
        if not self.head:
            print("Empty list")
            return False

        # Found at head
        if self.head.value == value:
            self.head = self.head.next
            return True

        # Find possible node before node with matching value
        prev = self.head
        while prev.next and prev.next.value != value:
            prev = prev.next

        # If not found, return false
        if not prev.next:
            return False

        # Previous node is found, so remove and return True
        prev.next = prev.next.next
        return True

    def clear(self):
        self.head = None

    def print(self):
        l = []
        if not self.head:
            print(l)
            return

        ptr = self.head
        while ptr:
            l.append(ptr.value)
            ptr = ptr.next
        print(l)

if __name__ == "__main__":
    LinkedList.demo()

from typing import List
from utils.graph.list_node import ListNode


class DoublyLinkedList:
    name = "Doubly Linked List"

    @classmethod
    def demo(cls):
        linked_list = cls.build([1,2,3,4,5,6,7,8,9])
        linked_list.print()
        linked_list.remove(1)
        linked_list.remove(3)
        linked_list.remove(4)
        linked_list.print()
        linked_list.add(ListNode(1))
        linked_list.add(ListNode(3))
        linked_list.add(ListNode(4))
        linked_list.print()

    def __init__(self):
        self.head = None
        self.tail = None

    @classmethod
    def build(cls, node_values: List):
        linked_list = cls()
        for value in node_values:
            linked_list.add(ListNode(value))
        return linked_list

    def add(self, node: ListNode) -> bool:
        if not self.head:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = self.head
            return True

        ptr = self.head
        while ptr.next:
            ptr = ptr.next

        ptr.next = node
        node.next = None
        node.prev = ptr
        self.tail = node
        return True

    def remove(self, value: int) -> bool:
        # Empty List
        if not self.head:
            print("Empty list")
            return False

        # Search for value
        ptr = self.head
        while ptr and ptr.value != value:
            ptr = ptr.next

        # Value not found, return False
        if not ptr:
            return False

        # Value not found at head
        if ptr.prev:
            ptr.prev.next = ptr.next
        # Value found at head
        else:
            self.head = ptr.next

        # Value not found at tail
        if ptr.next:
            ptr.next.prev = ptr.prev
        # Value found at tail
        else:
            self.tail = ptr.prev
        return True

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
    DoublyLinkedList.demo()

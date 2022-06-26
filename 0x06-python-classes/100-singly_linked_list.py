#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return (self.__data)
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")
        
        
class SinglyLinkedList:
    """Singly linked list class."""

    def __init__(self):
        """__init__ method for singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """ sorted_insert method - inserts node in order
    ii    Args:
            value (int): data of new node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
        else:
            curr = self.__head
            while curr.next_node:
                if new.data >= curr.data and new.data <= curr.next_node.data:
                    new.next_node = curr.next_node
                    curr.next_node = new
                    break
                elif new.data < curr.data:
                    new.next_node = curr
                    self.__head = new
                    break
                curr = curr.next_node
            if new.data >= curr.data:
                curr.next_node = new
            else:
                new.next_node = curr
                self.__head = new

    def __str__(self):
        """string representation of singly linked list
        Returns:
            llstr: new-line separated list string
        """
        curr = self.__head
        llstr = ''
        if curr is None:
            llstr = ''
        elif curr.next_node is None:
            llstr += str(curr.data)
        else:
            while curr.next_node:
                llstr += str(curr.data) + '\n'
                curr = curr.next_node
            llstr += str(curr.data)
        return llstr 
			 
if __name__ == '__main__':
    sll = SinglyLinkedList()

    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)

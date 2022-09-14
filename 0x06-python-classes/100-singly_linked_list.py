#!/usr/bin/python3
"""A linked list Node class"""


class Node:
    """A linked list node class"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Property getter for the node data"""
        return self.__data

    @property
    def next_node(self):
        """Property getter for the next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Setter for the next node"""
        if value is not None:
            if not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = value
        else:
            self.__next_node = value

"""A singly linked list class"""


class SinglyLinkedList:
    """Singly linked list class"""
    def __init__(self):
        self.__head = None
    
    def sorted_insert(self, value):
        """Inserts linked list values in sorted order"""
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            temp = Node(value)
            temp.next_node = self.__head
            self.__head = temp
        else:
            top = self.__head
            while top.next_node:
                if value <= top.next_node.data:
                    node = top.next_node
                    top.next_node = Node(value)
                    top.next_node.next_node = node
                    return self.__head
                top = top.next_node
            top.next_node = Node(value)
        return self.__head

    def __str__(self):
        """Method to print the linked list"""
        top = self.__head
        res = ""
        while top.next_node:
            res += "{:d}\n".format(top.data)
            top = top.next_node
        res += "{:d}".format(top.data)
        return res

#!/usr/bin/python3
"""Insertion of a node into a sorted linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """
        magic function that initializes the moment an instance is created
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieves the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """modifies the data"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        """retrieves next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """modifies next node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """magic function that initializes"""
        self.__head = None

    def __str__(self):
        """returns string version of linked list"""
        strings = []
        temp = self.__head
        while temp is not None:
            strings.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(strings)

    def sorted_insert(self, value):
        """
         inserts a new Node into the correct sorted position
         in the list (increasing order)
         """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = self.__head
            self.__head = new_node
        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and current.next_node.data
                   < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

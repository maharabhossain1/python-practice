class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
        self.size= 0

    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.size += 1
            self.tail = node
            node.prev = self.head

    def __remove_node(self ,node):
        if node.pres is Node:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev
        self.size -= 1

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.__remove_node(node)
            node= node.next

    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)

    def back(self):
        return self.tail.value

    def front(self):
        return self.head.value
    def __str__(self):
        vals=[]
        node = self.head
        while node is not None:
            vals.append(node.value) 
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


my_list = DoubleLinkedList()
# my_list.add(3)
# my_list.add(3)
# my_list.add(3)
# my_list.add(3)
# print(my_list)
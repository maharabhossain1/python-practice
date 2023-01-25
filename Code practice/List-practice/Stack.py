from LinkList import DoubleLinkedList

class Stack:
    def __init__(self):
        self.__list = DoubleLinkedList()
    def push(self, value):
        self.__list.add(value)
    def pop(self):
        val = self.__list.back()
        self.__list.remove_last()
        return val
    def is_empty(self):
        return self.__list.size==0
    def peek(self):
        return self.__list.back()
    def __len__(self):
        return self.__list.size




my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print (my_stack.peek())
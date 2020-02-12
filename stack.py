from node import Node

class Stack():

    def __init__(self):
        self.stack = None

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.stack

    def is_empty(self):
        return True if (self.stack == None) else False

    def get_last_node(self):
        if self.is_empty():
            return None
        else:
            node = self.stack
            while node.get_next() != None:
                node = node.get_next()
            return node

    def push(self,value):
        if self.is_empty():
            self.stack = Node()
            self.stack.set_value(value)
            return True
        else:
            new = Node()
            new.set_value(value)
            new.set_next(self.get_top())
            self.stack = new
            return True

    def pop(self,value):
        if self.is_empty():
            return False
        else:
            node = self.stack
            last = Node()
            if node.get_next() == None:
                del node
                return True
            stack = node.get_next()
            del node
            return True

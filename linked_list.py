from node import Node

class LinkedList():

    def __init__(self):
        self.list = None

    def get_head(self):
        if self.is_empty():
            return None
        else:
            return self.list

    def is_empty(self):
        return True if (self.list == None) else False

    def get_last_node(self):
        if self.is_empty():
            return None
        else:
            node = self.list
            while node.get_next() != None:
                node = node.get_next()
            return node

    def append(self,value):
        if self.is_empty():
            self.list = Node()
            self.list.set_value(value)
            return True
        else:
            new = Node()
            new.set_value(value)
            self.get_last_node().set_next(new)
            return True

    def remove(self,value):
        if self.is_empty():
            return False
        else:
            node = self.list
            last = Node()
            while node.get_value() != value:
                if node.get_next() == None:
                    return False
                last = node
                node = node.get_next()
            last.set_next(node.get_next())
            del node
            return True

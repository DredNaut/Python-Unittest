from node import Node

class Queue():

    def __init__(self):
        self.queue = None

    def get_back(self):
        if self.is_empty():
            return None
        else:
            return self.queue

    def is_empty(self):
        return True if (self.queue == None) else False

    def get_front(self):
        if self.is_empty():
            return None
        else:
            node = self.queue
            while node.get_next() != None:
                node = node.get_next()
            return node

    def enqueue(self,value):
        if self.is_empty():
            self.queue = Node()
            self.queue.set_value(value)
            return True
        else:
            new = Node()
            new.set_value(value)
            new.set_next(self.get_back())
            return True

    def dequeue(self,value):
        if self.is_empty():
            return False
        else:
            node = self.get_front()
            last = Node()
            if node.get_next() != None:
                del node
                return True
            while node.get_next() != None:
                last = node
            last.next = None
            del node
            return True

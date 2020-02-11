class Node():

    def __init__(self):
        self.value = None
        self.next = None

    def set_value(self,value):
        self.value = value

    def set_next(self,next_node):
        self.next = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

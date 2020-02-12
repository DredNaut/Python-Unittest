import unittest

from stack import Stack
from node import Node

class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        test = Stack()
        self.assertTrue(test.is_empty())

    def test_not_empty(self):
        test = Stack()
        test.push(5)
        self.assertFalse(test.is_empty())


class TestPush(unittest.TestCase):

    def test_push_string(self):
        test = Stack()
        test.push("test")
        self.assertEqual(test.stack.get_value(), "test")

    def test_push_int(self):
        test = Stack()
        test.push(5)
        self.assertEqual(test.stack.get_value(), 5)

    def test_push_float(self):
        test = Stack()
        test.push(5.12)
        self.assertEqual(test.stack.get_value(), 5.12)

    def test_push_bool(self):
        test = Stack()
        test.push(False)
        self.assertFalse(test.stack.get_value())

    def test_non_singleton(self):
        test = Stack()
        test.push(4.12)
        test.push(5.12)
        self.assertEqual(test.get_top().get_value(), 5.12)

class TestGetLastNode(unittest.TestCase):

    def test_empty_stack(self):
        test = Stack()
        self.assertEqual(test.get_last_node(), None)

    def test_singleton_stack(self):
        test = Stack()
        test.push(4.12)
        self.assertEqual(test.get_last_node(), test.stack)

    def test_longer_stack(self):
        test = Stack()
        test.push(4.12)
        test.push(6.12)
        test.push(5.12)
        self.assertEqual(test.get_top().get_value(), 5.12)

class TestGetTop(unittest.TestCase):

    def test_empty_stack(self):
        test = Stack()
        self.assertEqual(test.get_top(), None)

    def test_singleton_stack(self):
        test = Stack()
        test.push(4.12)
        self.assertEqual(test.get_top().get_value(), 4.12)

    def test_longer_stack(self):
        test = Stack()
        test.push(4.12)
        test.push(6.12)
        test.push(5.12)
        self.assertEqual(test.get_top().get_value(), 5.12)


class TestPop(unittest.TestCase):

    def test_empty_stack(self):
        test = Stack()
        self.assertFalse(test.pop(5))

    def test_singleton_stack(self):
        test = Stack()
        test.push(4.12)
        self.assertTrue(test.pop(4.12))

    def test_longer_stack(self):
        test = Stack()
        test.push(4.12)
        test.push(6.12)
        test.push(5.12)
        self.assertTrue(test.pop(4.12))

if __name__ == '__main__':
    unittest.main()

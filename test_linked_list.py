import unittest

from linked_list import LinkedList
from node import Node

class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        test = LinkedList()
        self.assertTrue(test.is_empty())

    def test_not_empty(self):
        test = LinkedList()
        test.append(5)
        self.assertFalse(test.is_empty())


class TestAppend(unittest.TestCase):

    def test_append_string(self):
        test = LinkedList()
        test.append("test")
        self.assertEqual(test.list.get_value(), "test")

    def test_append_int(self):
        test = LinkedList()
        test.append(5)
        self.assertEqual(test.list.get_value(), 5)

    def test_append_float(self):
        test = LinkedList()
        test.append(5.12)
        self.assertEqual(test.list.get_value(), 5.12)

    def test_append_bool(self):
        test = LinkedList()
        test.append(False)
        self.assertFalse(test.list.get_value())

    def test_non_singleton(self):
        test = LinkedList()
        test.append(4.12)
        test.append(5.12)
        self.assertEqual(test.list.get_value(), 4.12)
        self.assertEqual(test.get_last_node().get_value(), 5.12)

class TestGetLastNode(unittest.TestCase):

    def test_empty_list(self):
        test = LinkedList()
        self.assertEqual(test.get_last_node(), None)

    def test_singleton_list(self):
        test = LinkedList()
        test.append(4.12)
        self.assertEqual(test.get_last_node(), test.list)

    def test_longer_list(self):
        test = LinkedList()
        test.append(4.12)
        test.append(6.12)
        test.append(5.12)
        self.assertEqual(test.get_last_node().get_value(), 5.12)

class TestGetHead(unittest.TestCase):

    def test_empty_list(self):
        test = LinkedList()
        self.assertEqual(test.get_head(), None)

    def test_singleton_list(self):
        test = LinkedList()
        test.append(4.12)
        self.assertEqual(test.get_head().get_value(), 4.12)

    def test_longer_list(self):
        test = LinkedList()
        test.append(4.12)
        test.append(6.12)
        test.append(5.12)
        self.assertEqual(test.get_head().get_value(), 4.12)


class TestRemove(unittest.TestCase):

    def test_empty_list(self):
        test = LinkedList()
        self.assertFalse(test.remove(5))

    def test_singleton_list(self):
        test = LinkedList()
        test.append(4.12)
        self.assertTrue(test.remove(4.12))

    def test_longer_list(self):
        test = LinkedList()
        test.append(4.12)
        test.append(6.12)
        test.append(5.12)
        self.assertTrue(test.remove(4.12))

if __name__ == '__main__':
    unittest.main()

import unittest
from node import Node

class TestSetValue(unittest.TestCase):

    def test_string(self):
        test = Node()
        test.set_value("test")
        self.assertEqual(test.value, "test")

    def test_int(self):
        test = Node()
        test.set_value(468)
        self.assertEqual(test.value, 468)

    def test_float(self):
        test = Node()
        test.set_value(2.34)
        self.assertEqual(test.value, 2.34)

    def test_bool(self):
        test = Node()
        test.set_value(False)
        self.assertFalse(test.value)


class TestGetValue(unittest.TestCase):

    def test_string(self):
        test = Node()
        test.set_value("test")
        self.assertEqual(test.get_value(), "test")

    def test_int(self):
        test = Node()
        test.set_value(468)
        self.assertEqual(test.get_value(), 468)

    def test_float(self):
        test = Node()
        test.set_value(2.34)
        self.assertEqual(test.get_value(), 2.34)

    def test_bool(self):
        test = Node()
        test.set_value(False)
        self.assertFalse(test.get_value())

if __name__ == '__main__':
    unittest.main()

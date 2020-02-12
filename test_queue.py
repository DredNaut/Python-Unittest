import unittest

from queue import Queue
from node import Node

class TestIsEmpty(unittest.TestCase):

    def test_empty(self):
        test = Queue()
        self.assertTrue(test.is_empty())

    def test_not_empty(self):
        test = Queue()
        test.enqueue(5)
        self.assertFalse(test.is_empty())


class TestEnqueue(unittest.TestCase):

    def test_enqueue_string(self):
        test = Queue()
        test.enqueue("test")
        self.assertEqual(test.queue.get_value(), "test")

    def test_enqueue_int(self):
        test = Queue()
        test.enqueue(5)
        self.assertEqual(test.queue.get_value(), 5)

    def test_enqueue_float(self):
        test = Queue()
        test.enqueue(5.12)
        self.assertEqual(test.queue.get_value(), 5.12)

    def test_enqueue_bool(self):
        test = Queue()
        test.enqueue(False)
        self.assertFalse(test.queue.get_value())

    def test_non_singleton(self):
        test = Queue()
        test.enqueue(4.12)
        test.enqueue(5.12)
        self.assertEqual(test.queue.get_value(), 5.12)
        self.assertEqual(test.get_front().get_value(), 4.12)

class TestGetFront(unittest.TestCase):

    def test_empty_queue(self):
        test = Queue()
        self.assertEqual(test.get_front(), None)

    def test_singleton_queue(self):
        test = Queue()
        test.enqueue(4.12)
        self.assertEqual(test.get_front(), test.queue)

    def test_longer_queue(self):
        test = Queue()
        test.enqueue(4.12)
        test.enqueue(6.12)
        test.enqueue(5.12)
        self.assertEqual(test.get_back().get_value(), 5.12)

class TestGetBack(unittest.TestCase):

    def test_empty_queue(self):
        test = Queue()
        self.assertEqual(test.get_back(), None)

    def test_singleton_queue(self):
        test = Queue()
        test.enqueue(4.12)
        self.assertEqual(test.get_back().get_value(), 4.12)

    def test_longer_queue(self):
        test = Queue()
        test.enqueue(4.12)
        test.enqueue(6.12)
        test.enqueue(5.12)
        self.assertEqual(test.get_back().get_value(), 5.12)


class TestDequeue(unittest.TestCase):

    def test_empty_queue(self):
        test = Queue()
        self.assertFalse(test.dequeue(5))

    def test_singleton_queue(self):
        test = Queue()
        test.enqueue(4.12)
        self.assertTrue(test.dequeue(4.12))

    def test_longer_queue(self):
        test = Queue()
        test.enqueue(4.12)
        test.enqueue(6.12)
        test.enqueue(5.12)
        self.assertTrue(test.dequeue(4.12))

if __name__ == '__main__':
    unittest.main()

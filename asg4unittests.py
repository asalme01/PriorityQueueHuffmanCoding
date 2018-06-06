from priorityqueue import *


import unittest


class Asg4(unittest.TestCase):
    def test_priorityqueue_1(self):
        pq = PriorityQueue()
        pq.enqueue('a', 0)
        self.assertEqual(pq.front(), 'a')
        pq.enqueue('b', 5)
        self.assertEqual(pq.front(), 'b')
        pq.enqueue('z', 100)
        self.assertEqual(pq.front(), 'z')
        pq.enqueue('ZZ', -1)
        self.assertEqual(pq.front(), 'z')

    def test_priorityqueue_2(self):
        pq = PriorityQueue()
        pq.enqueue('a', 0)
        self.assertEqual(pq.front(), 'a')
        pq.enqueue('b', 5)
        self.assertEqual(pq.front(), 'b')
        pq.enqueue('z', 100)
        self.assertEqual(pq.front(), 'z')
        pq.enqueue('ZZ', -1)
        self.assertEqual(pq.front(), 'z')
        pq.enqueue('ZZZZ', -10)
        self.assertEqual(pq.front(), 'z')

    def test_priorityqueue_3(self):
        pq = PriorityQueue()
        pq.enqueue('a', 0)
        self.assertEqual(pq.front(), 'a')
        pq.enqueue('b', 5)
        self.assertEqual(pq.front(), 'b')
        pq.enqueue('z', 100)
        self.assertEqual(pq.front(), 'z')
        pq.enqueue('ZZ', -1)
        self.assertEqual(pq.front(), 'z')
        pq.enqueue('ZZZZ', 1000)
        self.assertNotEqual(pq.front(), 'ZZ')

    def test_priorityqueue_4(self):
        pq = PriorityQueue()
        pq.enqueue('ZZ', -1)
        self.assertEqual(pq.front(), 'ZZ')
        pq.enqueue('ZZZZ', 1000)
        self.assertEqual(pq.dequeue(), 'ZZZZ')

    def test_priorityqueue_5(self):
        pq = PriorityQueue()
        pq.enqueue(list(), -1)
        self.assertEqual(pq.front(), [])
        pq.enqueue(tuple([1, 2, 3]), 1000);
        pq.enqueue('bbc', 1000)
        pq.enqueue(int('78'), 1000000)
        self.assertEqual(pq.dequeue(), 78)


if __name__ == "__main__":
    unittest.main()
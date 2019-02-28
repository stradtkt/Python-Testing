import unittest
def min(l):
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min


def sum_list(l):
    total = 0
    for val in l:
        total += val
    return total


def less_than(a):
    return a < 100

class MainTest(unittest.TestCase):
    
    def test_min(self):
        self.assertEqual(min([1,2,3,4,5]), 1)
        self.assertEqual(min([1,2,3,4,5,6,7,8,9]), 1)
        self.assertEqual(min([2,4,6,8,10]), 2)

    def test_sum_list(self):
        self.assertEqual(sum_list([1,1,1,1,1]), 5)
        self.assertGreater(sum_list([2,2,2,2,2]), 9)
        self.assertGreaterEqual(sum_list([2,2,2,2,2,2,2]), 14)

    def test_less_than(self):
        self.assertLessEqual(less_than(9), 10)
        self.assertLess(less_than(10), 11)
        self.assertLess(less_than(12), 14)
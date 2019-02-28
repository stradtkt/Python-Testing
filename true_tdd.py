import unittest
# return the product of two given numbers
def multiply(a,b):
    return a * b
# return a boolean of whether every value in a given list is positive
def all_positive(l):
    
# return the average value of a given list
def average(l):
    pass
# add the largest and smallest values in a list and return the sum
def add_min_max(l):
    pass
class MainTest(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(5,4), 20)
        self.assertEqual(multiply(0,100), 0)
        self.assertEqual(multiply(-5,5), -25)
        self.assertEqual(multiply(-5,-5), -25)
    
    def test_all_positive(self):
        self.assertTrue(all_positive([1,2,3,4]))
        self.assertTrue(all_positive([1234]))
        self.assertFalse(all_positive([1,-2,3,4]))
        self.assertTrue(all_positive([]))

    def test_average(self):
        self.assertEqual(average([1,2,3,4,5]), 3)
        self.assertEqual(average([100]), 100)
        self.assertEqual(average([-100,100]), 0)
        # Notice that we can even create an assert to see if a specific error is raised by our function
        self.assertRaises(ZeroDivisionError, average, [])

    def test_add_minmax(self):
        self.assertEqual(average([1,2,3,4,5]), 6)
        self.assertEqual(average([0,0,0,0]), 0)
        self.assertEqual(average([10,5,0,-5]), 5)
        # Does this give us a hint as to how a specific case should be handled by our function?
        self.assertIsNone(average([]))
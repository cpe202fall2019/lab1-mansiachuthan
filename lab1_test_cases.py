import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # attempts to test all possible scenarios for the method
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 2, 5, 6, 3]), 6)
        self.assertEqual(max_list_iter([3, 3, 3]), 3)
        self.assertEqual(max_list_iter([3, 2, 3]), 3)
        self.assertEqual(max_list_iter([3, 3, 2]), 3)
        self.assertEqual(max_list_iter([2, 3, 3]), 3)
        self.assertEqual(max_list_iter([-1, 0, -5]), 0)
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([5, 9, 2, 3]), [3, 2, 9, 5])
        self.assertEqual(reverse_rec([5]), [5])
        self.assertEqual(reverse_rec([]), [])
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_num = [3, 3, 3]
        list_even = [1, 2, 3, 4]
        list_one = [5]
        list_empty = []
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)
        self.assertEqual(bin_search(5, 0, len(list_val) - 1, list_val), None)
        self.assertEqual(bin_search(3, 0, len(list_num) - 1, list_num), 1)
        self.assertEqual(bin_search(3, 0, len(list_even) - 1, list_even), 2)
        self.assertEqual(bin_search(5, 0, len(list_one) - 1, list_one), 0)
        self.assertEqual(bin_search(3, 0, len(list_empty) - 1, list_empty), None)


if __name__ == "__main__":
    unittest.main()

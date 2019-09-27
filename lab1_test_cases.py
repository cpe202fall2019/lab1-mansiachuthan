import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # attempts to test all possible scenarios for the method

        # test 1: check that ValueError is raised if list is None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        # test 2: testing a normal case --> finds max in a list
        self.assertEqual(max_list_iter([1, 2, 5, 6, 3]), 6)

        # test 3: testing a list of all same numbers
        self.assertEqual(max_list_iter([3, 3, 3]), 3)

        # test 4: multiple numbers are equal/max in the list (in different positions)
        self.assertEqual(max_list_iter([3, 2, 3]), 3)
        self.assertEqual(max_list_iter([3, 3, 2]), 3)
        self.assertEqual(max_list_iter([2, 3, 3]), 3)

        # test 5: testing with negative numbers
        self.assertEqual(max_list_iter([-1, 0, -5]), 0)

        # test 6: checking that an empty list returns None
        self.assertEqual(max_list_iter([]), None)

    def test_reverse_rec(self):
        # test 1: check that ValueError is raised if list is None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

        # test 2: tests simple cases and reverses the list
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_rec([5, 9, 2, 3]), [3, 2, 9, 5])

        # test 3: checks that the method returns original list if list only contains one number
        self.assertEqual(reverse_rec([5]), [5])

        # test 4: checks that methods returns empty list if given empty list
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        # test 1: check that ValueError is raised if list is None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(None, None, None, tlist)

        # different lists for different cases
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        list_num = [3, 3, 3]
        list_even = [1, 2, 3, 4]
        list_one = [5]
        list_empty = []
        list_negative = [-3,-2,-1]

        # what the values in the parameters mean/stand for:
        # low = 0
        # high = len(list_val) - 1

        # test 2: if the target is in the middle of an odd list
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)

        # test 3: if the target is in the "higher" half of the list
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)

        # test 4: if the target is not found in the list
        self.assertEqual(bin_search(5, 0, len(list_val) - 1, list_val), None)

        # test 5: if target is found at first instance even if it is found multiple times in list
        self.assertEqual(bin_search(3, 0, len(list_num) - 1, list_num), 1)

        # test 6: if target is in middle and in an even list
        self.assertEqual(bin_search(3, 0, len(list_even) - 1, list_even), 2)

        # test 7: if target is found and is in a list with a length of 1
        self.assertEqual(bin_search(5, 0, len(list_one) - 1, list_one), 0)

        # test 8: if list is empty --> should return None since target obviously not there
        self.assertEqual(bin_search(3, 0, len(list_empty) - 1, list_empty), None)

        # test 9: if list contains negative numbers
        self.assertEqual(bin_search(-3, 0, len(list_negative) - 1, list_negative), 0)


if __name__ == "__main__":
    unittest.main()

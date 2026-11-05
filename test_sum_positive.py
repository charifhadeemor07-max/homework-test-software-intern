import unittest
from solution import sum_positive


class TestSumPositive(unittest.TestCase):
    def test_example_from_homework(self):
        data = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, -10]
        self.assertEqual(sum_positive(data), 45)

    def test_empty_list(self):
        self.assertEqual(sum_positive([]), 0)

    def test_all_negative(self):
        self.assertEqual(sum_positive([-5, -1, -100]), 0)

    def test_all_positive(self):
        self.assertEqual(sum_positive([1, 2, 3]), 6)

    def test_zero_is_not_counted(self):
        self.assertEqual(sum_positive([0, 0, 0]), 0)

    def test_single_positive(self):
        self.assertEqual(sum_positive([7]), 7)

    def test_decimals(self):
        self.assertAlmostEqual(sum_positive([1.5, -2.5, 2.25]), 3.75)


if __name__ == "__main__":
    unittest.main()
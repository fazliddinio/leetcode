import unittest
from two_sum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_base_case(self):
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_different_positions(self):
        result = self.solution.twoSum([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])

    def test_negative_numbers(self):
        result = self.solution.twoSum([-2, -4, -5, -8], -9)
        self.assertEqual(result, [1, 2])

    def test_large_numbers(self):
        result = self.solution.twoSum([1_000_000, 2_000_000, 4_000_000], 5_000_000)
        self.assertEqual(result, [0, 2])

    def test_same_number_twice(self):
        result = self.solution.twoSum([5, 5], 10)
        self.assertEqual(result, [0, 1])

    def test_with_zeros(self):
        result = self.solution.twoSum([2, 0, 4, 0, 4], 0)
        self.assertEqual(result, [1, 3])

        

if __name__ == '__main__':
    unittest.main()
import unittest
from solution import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests the standard case [2,7,11,15], target=9."""
        nums = [2,7,11,15]
        target = 9
        expected = [0, 1]
        self.assertEqual(sorted(self.solution.twoSum(nums, target)), sorted(expected))

    def test_example_2(self):
        """Tests a case with repeated numbers [3,2,4], target=6."""
        nums = [3,2,4]
        target = 6
        expected = [1, 2]
        self.assertEqual(sorted(self.solution.twoSum(nums, target)), sorted(expected))

    def test_example_3(self):
        """Tests a case with two identical numbers [3,3], target=6."""
        nums = [3,3]
        target = 6
        expected = [0, 1]
        self.assertEqual(sorted(self.solution.twoSum(nums, target)), sorted(expected))

    def test_no_solution(self):
        """Tests a case where no solution exists (though problem constraints usually guarantee one)."""
        nums = [1, 2, 3]
        target = 7
        expected = []
        self.assertEqual(self.solution.twoSum(nums, target), expected)

if __name__ == '__main__':
    unittest.main()

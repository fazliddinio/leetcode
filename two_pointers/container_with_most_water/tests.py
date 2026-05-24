import unittest
from solution import Solution

class TestContainerWithMostWater(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests the first example case with various heights."""
        height = [1,8,6,2,5,4,8,3,7]
        expected = 49
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_example_2(self):
        """Tests a simple case with two elements."""
        height = [1,1]
        expected = 1
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_decreasing_heights(self):
        """Tests a case where heights are decreasing."""
        height = [5,4,3,2,1]
        expected = 6
        self.assertEqual(self.solution.maxArea(height), expected)

    def test_increasing_heights(self):
        """Tests a case where heights are increasing."""
        height = [1,2,3,4,5]
        expected = 6
        self.assertEqual(self.solution.maxArea(height), expected)

if __name__ == '__main__':
    unittest.main()

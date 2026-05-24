import unittest
from solution import Solution

class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests a case with duplicates present."""
        nums = [1,2,3,1]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_example_2(self):
        """Tests a case with no duplicates."""
        nums = [1,2,3,4]
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_example_3(self):
        """Tests a case with multiple duplicates."""
        nums = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(self.solution.containsDuplicate(nums))

    def test_empty_list(self):
        """Tests an empty list, which should not contain duplicates."""
        nums = []
        self.assertFalse(self.solution.containsDuplicate(nums))

    def test_single_element(self):
        """Tests a list with a single element, which should not contain duplicates."""
        nums = [1]
        self.assertFalse(self.solution.containsDuplicate(nums))

if __name__ == '__main__':
    unittest.main()

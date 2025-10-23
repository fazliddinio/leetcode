import unittest
from contains_duplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_contains_duplicate_basic(self):
        """Test case with obvious duplicates"""
        nums = [1, 2, 3, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_no_duplicates(self):
        """Test case with no duplicates"""
        nums = [1, 2, 3, 4]
        self.assertFalse(self.solution.containsDuplicate(nums))
    
    def test_all_duplicates(self):
        """Test case where all elements are the same"""
        nums = [1, 1, 1, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_empty_list(self):
        """Test case with empty list"""
        nums = []
        self.assertFalse(self.solution.containsDuplicate(nums))
    
    def test_single_element(self):
        """Test case with single element"""
        nums = [1]
        self.assertFalse(self.solution.containsDuplicate(nums))
    
    def test_two_elements_duplicate(self):
        """Test case with two identical elements"""
        nums = [1, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_two_elements_no_duplicate(self):
        """Test case with two different elements"""
        nums = [1, 2]
        self.assertFalse(self.solution.containsDuplicate(nums))
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        nums = [-1, -2, -3, -1]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_negative_numbers_no_duplicate(self):
        """Test case with negative numbers without duplicates"""
        nums = [-1, -2, -3, -4]
        self.assertFalse(self.solution.containsDuplicate(nums))
    
    def test_mixed_positive_negative(self):
        """Test case with mixed positive and negative numbers"""
        nums = [1, -1, 2, -2, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_zero_with_duplicates(self):
        """Test case with zeros"""
        nums = [0, 1, 2, 0]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_large_list_with_duplicate(self):
        """Test case with large list containing duplicates"""
        nums = list(range(1000)) + [500]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_large_list_no_duplicate(self):
        """Test case with large list without duplicates"""
        nums = list(range(1000))
        self.assertFalse(self.solution.containsDuplicate(nums))
    
    def test_duplicate_at_end(self):
        """Test case where duplicate is at the end"""
        nums = [1, 2, 3, 4, 5, 1]
        self.assertTrue(self.solution.containsDuplicate(nums))
    
    def test_consecutive_duplicates(self):
        """Test case with consecutive duplicate elements"""
        nums = [1, 2, 2, 3]
        self.assertTrue(self.solution.containsDuplicate(nums))


if __name__ == '__main__':
    unittest.main()
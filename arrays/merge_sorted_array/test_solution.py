from solution import Solution
import unittest


class TestMerge(unittest.TestCase):
    """Essential tests for merge sorted arrays."""
    
    def setUp(self):
        self.solution = Solution()
    
    def test_basic_merge(self):
        """Happy path: normal merge."""
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [2, 5, 6]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])
    
    def test_empty_nums2(self):
        """Edge: nums2 is empty."""
        nums1 = [1, 2, 3]
        nums2 = []
        self.solution.merge(nums1, 3, nums2, 0)
        self.assertEqual(nums1, [1, 2, 3])
    
    def test_empty_nums1(self):
        """Edge: nums1 is empty."""
        nums1 = [0, 0, 0]
        nums2 = [1, 2, 3]
        self.solution.merge(nums1, 0, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3])
    
    def test_nums2_all_smaller(self):
        """Edge: all nums2 elements come first."""
        nums1 = [4, 5, 6, 0, 0, 0]
        nums2 = [1, 2, 3]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
    
    def test_nums2_all_larger(self):
        """Edge: all nums1 elements come first."""
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [4, 5, 6]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])
    
    def test_negative_numbers(self):
        """Edge: negative numbers."""
        nums1 = [-3, -1, 0, 0]
        nums2 = [-2, 1]
        self.solution.merge(nums1, 2, nums2, 2)
        self.assertEqual(nums1, [-3, -2, -1, 1])
    
    def test_duplicates(self):
        """Edge: duplicate values."""
        nums1 = [1, 2, 2, 0, 0, 0]
        nums2 = [2, 2, 3]
        self.solution.merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 2, 2, 2, 3])
    
    def test_single_element(self):
        """Edge: single element arrays."""
        nums1 = [2, 0]
        nums2 = [1]
        self.solution.merge(nums1, 1, nums2, 1)
        self.assertEqual(nums1, [1, 2])


if __name__ == '__main__':
    unittest.main(verbosity=2)
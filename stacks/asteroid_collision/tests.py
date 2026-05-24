import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """
        Test typical collision scenario.
        Input: [5, 10, -5]
        Expected Output: [5, 10]
        Explanation: 
        10 and -5 collide resulting in 10. The 5 and 10 never collide.
        """
        self.assertEqual(self.solution.asteroidCollision([5, 10, -5]), [5, 10])

    def test_example_2(self):
        """
        Test equal size collision.
        Input: [8, -8]
        Expected Output: []
        Explanation: The 8 and -8 collide exploding each other.
        """
        self.assertEqual(self.solution.asteroidCollision([8, -8]), [])

    def test_example_3(self):
        """
        Test multiple collisions.
        Input: [10, 2, -5]
        Expected Output: [10]
        Explanation: 
        2 and -5 collide resulting in -5. Then 10 and -5 collide resulting in 10.
        """
        self.assertEqual(self.solution.asteroidCollision([10, 2, -5]), [10])

    def test_no_collision_moving_away(self):
        """
        Test asteroids moving away from each other.
        Input: [-2, -1, 1, 2]
        Expected Output: [-2, -1, 1, 2]
        Explanation: 
        -2 and -1 move left, 1 and 2 move right. They never meet.
        """
        self.assertEqual(self.solution.asteroidCollision([-2, -1, 1, 2]), [-2, -1, 1, 2])

    def test_all_negative(self):
        """
        Test all asteroids moving left.
        Input: [-2, -2, -2]
        Expected Output: [-2, -2, -2]
        Explanation: No right-moving asteroid to collide with.
        """
        self.assertEqual(self.solution.asteroidCollision([-2, -2, -2]), [-2, -2, -2])

if __name__ == '__main__':
    unittest.main()

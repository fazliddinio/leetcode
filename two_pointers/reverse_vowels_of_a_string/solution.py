"""
Reverse Vowels of a String
LeetCode 345

Approach: Two Pointers
Time: O(n) — single pass from both ends
Space: O(n) — converting string to list of characters
Brute: O(n) — collect vowels in list, reverse, rebuild string in two passes
"""


class Solution:

    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        chars = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1

            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

        return ''.join(chars)

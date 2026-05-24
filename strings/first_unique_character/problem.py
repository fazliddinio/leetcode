"""
==========================================
  First Unique Character in a String (LeetCode 387)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1: Input: s = "leetcode", Output: 0
Example 2: Input: s = "loveleetcode", Output: 2
Example 3: Input: s = "aabb", Output: -1

Constraints: 1 <= s.length <= 10^5, s consists of only lowercase English letters.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the very first letter in a word that ONLY appears once in the entire word.

    s = "loveleetcode"
    l -> appears twice
    o -> appears twice (no it doesn't wait, actually 'o' appears once! Wait, yes 'o' is once in loveleetcode? No, 'loveleetcode' has two 'e', two 'l', two 'o'. Wait, 'l' is twice. 'o' is twice. 'v' is once! Let's trace it carefully!)
    
    Actually: 'l' x2, 'o' x2, 'v' x1, 'e' x4, 't' x1, 'c' x1, 'd' x1
    First one that is a 1 is 'v' at index 2!

Method: Hash Map / Frequency Array
  1. Go through the string and count how many times each letter appears. Store in a dictionary or array `count[char]`.
  2. Go through the string AGAIN from the beginning.
  3. The first letter you see that has `count == 1` is your answer! Return its index.
"""

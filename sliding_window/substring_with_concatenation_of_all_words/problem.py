"""
==========================================
  Substring with Concatenation of All Words (LeetCode 30)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Example 1: Input: s = "barfoothefoobarman", words = ["foo","bar"], Output: [0,9]
Explanation: Since words.length == 2 and words[i].length == 3, the concatenated substring has to be of length 6.
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"].
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"].

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find all the starting spots where you can pull out exactly ALL the words in the list, back-to-back, in any order.

    words: ["foo", "bar"]
    s: "barfoothefoobarman"
    Idx 0: "barfoo" -> "bar" + "foo". MATCH!
    Idx 9: "foobar" -> "foo" + "bar". MATCH!

Method: Hash Map & Chunked Sliding Window
  Let `N` be the length of one word, `K` be the number of words. The window size is fixed at `N * K`.
  1. Build a hash map of the required words and their counts.
  2. Because words are length `N`, you can start the window at offset `0`, `1`, up to `N-1`.
  3. Slide the window forward by chunks of `N`. Maintain a hash map of words seen in the current window!
"""

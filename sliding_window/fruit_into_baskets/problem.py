"""
==========================================
  Fruit Into Baskets (LeetCode 904)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You have two baskets, and each basket can hold only a single type of fruit. 
Starting from any tree, you must pick exactly one fruit from every tree while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Return the maximum number of fruits you can pick.

Example 1: Input: fruits = [1,2,1], Output: 3
Example 2: Input: fruits = [1,2,3,2,2], Output: 4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
This is literally "Longest Substring with At Most 2 Distinct Characters", disguised as a farming problem!

    fruits = [1, 2, 3, 2, 2]
    Pick [2, 3, 2, 2] -> two types of fruits (2 and 3). Max = 4.

Method: Sliding Window + Hash Map
  Use a hash map to count the frequency of each fruit in your window.
  While your hash map has MORE than 2 types of fruit:
     - The window is invalid. Shrink `Left`.
     - Remove `fruits[Left]` from the map.
  Update the max window size!
"""

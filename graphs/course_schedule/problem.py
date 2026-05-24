"""
==========================================
  Course Schedule (LeetCode 207)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
There are numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
Return true if you can finish all courses. Otherwise, return false.

Example 1: Input: numCourses = 2, prerequisites = [[1,0]], Output: true

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Are there any impossible Catch-22 dependencies in your class schedule?
Cannot take Course 1 without Course 0. But what if Course 0 needs Course 1? (Cycle!)

Method: Topological Sort (Kahn's) or Cycle Detection (DFS)
  Track indegrees (how many prerequisites a course has).
  Start with courses that have 0 prerequisites. Every time you "take" a course, reduce indegrees of courses that depend on it!
  If all courses get to 0, success! Otherwise, there's a loop.
"""

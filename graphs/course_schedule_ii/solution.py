# LeetCode 210: Course Schedule II
# Time: O(V + E), Space: O(V + E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = [0] * numCourses
        result = []
        
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == 2:
                return True
            
            visited[course] = 1
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visited[course] = 2
            result.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result

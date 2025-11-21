# LeetCode 207: Course Schedule
# Time: O(V + E), Space: O(V + E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
        
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
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

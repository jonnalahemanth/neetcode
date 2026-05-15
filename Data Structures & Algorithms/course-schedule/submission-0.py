class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_graph = [[] for _ in range(numCourses)]

        visited = [0]*numCourses

        for cour, pre in prerequisites:
            adj_graph[pre].append(cour)

        def dfs(j):
            if visited[j] == 1:
                return False
            
            if visited[j] == 2:
                return True

            visited[j] = 1

            for pre in adj_graph[j]:
                if not dfs(pre):
                    return False

            visited[j] = 2

            return True
        

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False

        return True
        
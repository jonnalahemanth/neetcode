class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_graph = [[] for _ in range(numCourses)]

        visited = [0]*numCourses

        for cource, pre in prerequisites:
            adj_graph[pre].append(cource)

        def dfs(node):
            if visited[node] == 1:
                return False
            
            if visited[node] == 2:
                return True

            visited[node] = 1        

            for pre in adj_graph[node]:
                if not dfs(pre):
                    return False

            visited[node] = 2
            order.append(node)

            return True


        order = []
        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return []
        return order[::-1]
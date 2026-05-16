class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj_graph = [[] for _ in range(n)]

        visited = [False]*n

        for src, dst in edges:
            adj_graph[src].append(dst)
            adj_graph[dst].append(src)

        
        def dfs(node):
            visited[node] = True

            for nei in adj_graph[node]:
                if not visited[nei]:
                    dfs(nei)



        components = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                components += 1

        return components
        
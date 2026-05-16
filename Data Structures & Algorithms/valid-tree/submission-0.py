class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj_graph = [[] for _ in range(n)]

        for src, dst in edges:
            adj_graph[src].append(dst)
            adj_graph[dst].append(src)


        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj_graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True



        if not dfs(0, -1):
            return False

        return len(visited) == n
        
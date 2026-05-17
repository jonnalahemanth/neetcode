class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            while x != parent[x]:
                x = parent[x]
            
            return x

        
        def union(x, y):

            px = find(x)
            py = find(y)

            if px ==py:
                return False

            parent[py] = px

            return True

        for u, v in edges:
            if not union(u,v):
                return [u, v]
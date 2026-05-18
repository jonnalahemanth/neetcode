from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort(reverse=True)

        res = []

        def dfs(airport):

            while graph[airport]:
                nxt = graph[airport].pop()
                dfs(nxt)
            
            res.append(airport)

        dfs('JFK')

        return res[::-1]
        
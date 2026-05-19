from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, price in flights:
            graph[u].append((v, price))
        
        min_cost = [float('inf')]*n
        min_cost[src] = 0

        q = deque()
        q.append((src, 0))

        stops = 0

        while q and stops<=k:
            size = len(q)

            temp = min_cost[:]

            for _ in range(size):
                node, cost = q.popleft()

                for nei, price in graph[node]:
                    new_cost = cost+price

                    if new_cost < temp[nei]:
                        temp[nei] = new_cost
                        q.append((nei, new_cost))
            min_cost = temp
            stops += 1
        return min_cost[dst] if min_cost[dst] != float('inf') else -1    
        
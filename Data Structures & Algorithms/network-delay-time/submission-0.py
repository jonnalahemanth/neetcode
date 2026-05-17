import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for src, dst, time in times:
                graph[src].append((dst, time))

        minHeap = [(0, k)]
        visited = set()
        max_time = 0

        while minHeap:
                curr_time, node = heapq.heappop(minHeap)

                if node in visited:
                        continue
                visited.add(node)

                max_time = max(max_time, curr_time)

                for nei, weight in graph[node]:
                        if nei not in visited:
                                heapq.heappush(minHeap, (curr_time+weight, nei))

        
        return max_time if len(visited) == n else -1

        